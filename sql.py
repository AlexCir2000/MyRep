import psycopg2, io
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from Captcha import get_captcha
import tkinter
from tkinter import *
from PIL import Image
def create_db(db_name):
    try:
        # Подключение к существующей базе данных
        connection = psycopg2.connect(user="postgres",
                                      # пароль, который указали при установке PostgreSQL
                                      password="sql",
                                      host="127.0.0.1",
                                      port="5433")
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        # Курсор для выполнения операций с базой данных
        cursor = connection.cursor()
        sql_create_database = 'create database ' + db_name
        cursor.execute(sql_create_database)
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")
# create_db('Test1')

def create_table(table_name):
    try:
        # Подключение к существующей базе данных
        connection = psycopg2.connect(user="postgres",
                                      # пароль, который указали при установке PostgreSQL
                                      password="sql",
                                      host="127.0.0.1",
                                      port="5433",
                                      database = "test1")
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        # Курсор для выполнения операций с базой данных
        cursor = connection.cursor()
        sql_create_table = 'CREATE TABLE IF NOT EXISTS ' + table_name + ''' 
                                (ID SERIAL PRIMARY KEY     NOT NULL,
                                picture BYTEA[],
                                TEXT TEXT
                                )'''
        cursor.execute(sql_create_table)
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")
# create_table('Table1')


def insert_query(kol):
    try:
        # Подключение к существующей базе данных
        connection = psycopg2.connect(user="postgres",
                                      # пароль, который указали при установке PostgreSQL
                                      password="sql",
                                      host="127.0.0.1",
                                      port="5433",
                                      database = "test1")
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        # Курсор для выполнения операций с базой данных
        cursor = connection.cursor()
        for i in range(kol):
            data, text = get_captcha(5)
            send_data = data.getvalue()
            cursor.execute('''INSERT INTO Table1 (picture, text)VALUES (%s, %s)''', ([send_data], text))
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")

# insert_query(100)

def select_query(kol):
    try:
        # Подключение к существующей базе данных
        connection = psycopg2.connect(user="postgres",
                                      # пароль, который указали при установке PostgreSQL
                                      password="sql",
                                      host="127.0.0.1",
                                      port="5433",
                                      database = "test1")
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        # Курсор для выполнения операций с базой данных
        cursor = connection.cursor()
        cursor.execute('SELECT picture, text FROM Table1 WHERE id< ' + str(kol))
        result = cursor.fetchall()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")
    return result

data = select_query(50)
print(data[1][0])
root2 = tkinter.Tk()

for i in range(0,50):
    pos = (i // 10)
    lbl = Label(root2, text= data[i][1], font=("Arial Bold", 20))
    lbl.grid(row=i-(10 * pos), column=2 * pos + 1)
    canvas = tkinter.Canvas(root2, width=5*25, height=90)
    canvas.grid(row=i-(10 * pos), column=2 * pos)
    pic = io.BytesIO(data[i][0])
    pic1 = Image.open(pic)
    img = canvas.create_image(0, 0, anchor='nw',image=pic1)
root2.mainloop()