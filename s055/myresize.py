from PIL import Image

num = 0
imgPath = '%s.jpg' %num
img = Image.open(imgPath)
x,y = img.size
print x,y
rx,ry = 800,400
img.resize((rx,ry)).save('test.jpg')
