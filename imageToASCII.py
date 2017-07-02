import math
from PIL import Image


a = open("image.html","w")

symbols = ["#","O","A","T","I","i",";",",","."," "]
symbolSize = 1/len(symbols)

im = Image.open("sample.png").convert('RGBA')
px = im.load()
width,height = im.size

print("<pre style=\"font-size: 5px; display: inline-block; font-family: monospace;letter-spacing: 0.0em;line-height: 0.7em;\">", file=a)

for y in range(0, height):
    for x in range(0, width):
        pxRGB = im.getpixel((x,y))
        R,G,B,A = pxRGB
        brt = sum([R,G,B])/3/255
        if A > 0 and brt > 0.1:
            pos = round(brt/symbolSize)
        elif A > 0 and brt <= 0.1:
            pos = 1
        else:
            pos = len(symbols)
        print(symbols[pos - 1],end="",file=a)
    print("", file=a)
print("</pre>", file=a)
