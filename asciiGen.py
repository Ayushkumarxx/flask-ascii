from PIL import Image , ImageDraw, ImageFont

import math




repeatedChar = 'JAISHREERAM'
repeatedCharLength = len(repeatedChar)
repeatedCharIndex = 0

def getRepeatedChar():
    global repeatedCharIndex  # Declare repeatedCharIndex as global
    
    char = repeatedChar[repeatedCharIndex]
    repeatedCharIndex = (repeatedCharIndex + 1) % repeatedCharLength
    
    return char


scaleFactor = 0.3
oneCharWidth = 10
oneCharHeight = 16


im = Image.open('rishab.jpg')
fnt = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)

width, height = im.size

im = im.resize((int(scaleFactor*width), int(scaleFactor*height*(oneCharWidth/oneCharHeight))), Image.Resampling.NEAREST)

width, height = im.size

pix = im.load()


outputImg2 = Image.new("RGB", (oneCharWidth * width, oneCharHeight * height) , color=(0,0,0))

d2 = ImageDraw.Draw(outputImg2)

for i in range(height):
    for j in range(width):
        r, g, b = pix[j, i]
        h = int(r/3 + g/3 + b/3)
        pix[j, i] = (h, h, h)
     
       
        d2.text((j*oneCharWidth, i*oneCharHeight), getRepeatedChar(), font=fnt, fill=(r,g,b))





outputImg2.save("ascii2.png")

