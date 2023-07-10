
import cmpt120image
import random
pic = cmpt120image.getImage('images/child.png')
wi = cmpt120image.getWhiteImage(400, 300)

#---------------------------------------------------------
def recolorImage(img,colour):
  height = len(pic)
  width = len(img[0])
  r = random.choice(range(0,255))
  g = random.choice(range(0,255))
  b = random.choice(range(0,255))
  colour = (r,g,b)
  for h in range(height):
    for w in range(width):
      if img[h][w] != [255,255,255]:
        img[h][w] = colour
# recolorImage(pic,[25,255,39])
# cmpt120image.showImage(pic)
#---------------------------------------------------------
def average(p1,p2,p3,p4):
  r = (p1[0] + p2[0] + p3[0] + p4[0])/4
  g = (p1[1] + p2[1] + p3[1] + p4[1])/4
  b = (p1[2] + p2[2] + p3[2] + p4[2])/4
  avg = (r,g,b)
  return avg

def minify(img):
  h = len(pic)
  w = len(pic[0])
  blkimg = cmpt120image.getBlackImage(int(w/2),int(h/2))
  for r in range(0,h,2):
    for c in range(0,w,2):
      blkimg[int(r/2)][int(c/2)] = (average((pic[r][c]),(pic[r+1][c]),(pic[r][c+1]),(pic[r+1][c+1])))
  return blkimg
# pic = minify(pic)
# cmpt120image.showImage(pic)
#----------------------------------------------------------
def mirror(img):
  height = len(img)
  width = len(img[0])
  black = cmpt120image.getBlackImage(width,height)
  for h in range(height):
    l = []
    for w in range(width-1,-1,-1):
      l += [img[h][w]]
    black[h] = l   
  return black
# AH = mirror(pic)
# cmpt120image.showImage(AH)
#------------------------------------------------------------
def drawItem(img, pic, row, col):
  h = len(pic)
  w = len(pic[0])
  for r in range(h):
    for c in range(w):
      img[r + row][c + col] = pic[r][c]
  return img
# h = drawItem(wi,pic,100,100)
# cmpt120image.showImage(h)
#------------------------------------------------------------
def distributeItems(canvas,item,n):
  height_canvas = len(canvas) 
  width_canvas = len(canvas[0])
  height_item = len(item)
  width_item = len(item[0])
  for i in range(n):
    r = random.randint(0,height_canvas-height_item)
    c = random.randint(0,width_canvas-width_item)
    canvas = drawItem(canvas,item,r,c)
  return canvas
