from captcha.image import ImageCaptcha
import random, string
def get_captcha(strlen):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(strlen))
    print("Random string of length", strlen, "is:", rand_string)
    image = ImageCaptcha(width = strlen*25, height = 90)
    data = image.generate('rand_string')
    image.write(rand_string, 'demo.png')
    return data, rand_string

get_captcha(12)
