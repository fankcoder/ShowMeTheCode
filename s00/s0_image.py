import Image
from PIL import ImageFont,ImageDraw
import os

def drawNum(filer,num,color):
    img = Image.open(filer)
    print img.format,img.size,img.mode
    x,y = img.size
    myfont = ImageFont.truetype("FreeMono.ttf",40,0,'utf-8')
    draw = ImageDraw.Draw(img)
    draw.text((x*0.7,0),str(num),font=myfont,fill=str(color))
    filer_name = 'num_'+ filer
    img.save(filer_name)

if __name__ == '__main__':
    drawNum('1.jpg',3,'black')
