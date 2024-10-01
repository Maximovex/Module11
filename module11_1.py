from PIL import Image
import requests

r=requests.get('https://vtf.ru/contacts/')
print(r.text)
print(r.headers['content-type'])


try:
    with Image.open('image.jpg') as im:
        print(im.size)
        r, g, b = im.split()
        im = Image.merge("RGB", (b, g, r))
        im.save('image_mixed.png')
except OSError:
    pass
