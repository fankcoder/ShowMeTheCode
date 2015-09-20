#coding:utf-8
import string
import random
from PIL import Image
from PIL import ImageFont,ImageDraw

def ranStr():
    letters = string.letters
    ranstr = random.choice(letters)
    return ranstr

'''
im = Image.open('yzm0.jpg')
rx,ry = 290,80
im.resize((rx,ry)).save("rancaptcha.jpg")
'''

ranstr = ''+ranStr()+ranStr()+ranStr()+ranStr()
img = Image.open('rancaptcha.jpg')
myfont = ImageFont.truetype("FreeMono.ttf",60,0,'utf-8')
draw = ImageDraw.Draw(img)
draw.text((0,0),ranstr,font=myfont,fill=(20,220,20,0))
draw.line([(5,5),(10,100)],fill='red',width=2)
draw.line([(25,5),(150,20)],fill='red',width=2)
draw.line([(50,60),(120,20)],fill='red',width=2)
img.save('ranc1.jpg')
