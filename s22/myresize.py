from PIL import Image

def resize(rx=800,ry=400):
    num = 0
    imgPath = '%s.jpg' %num
    img = Image.open(imgPath)
    x,y = img.size
    img.resize((rx,ry)).save('test.jpg')

if __name__ == '__main__':
    resize(1334,750)
