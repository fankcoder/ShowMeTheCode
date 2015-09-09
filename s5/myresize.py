from PIL import Image

<<<<<<< HEAD
num = 0
imgPath = '%s.jpg' %num
img = Image.open(imgPath)
x,y = img.size
print x,y
rx,ry = 800,400
img.resize((rx,ry)).save('test.jpg')
=======
num = 1
imgPath = '%s.png' %num
img = open(imgPath,'rb')
print img

>>>>>>> 8fe6dda643fa70c08d620d17e4bcef8c144e1bc3
