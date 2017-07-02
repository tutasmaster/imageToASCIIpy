
from PIL import Image

a = open("image.html","w")

im = Image.open("sample.png")
px = im.load()
width,height = im.size

print("<pre style=\"font: 10px/5px monospace; text-align: center;\">", file=a)

for y in range(0, height):
    for x in range(0, width):
        pxRGB = im.getpixel((x,y))
        R,G,B,A = pxRGB
        brt = sum([R,G,B])/3/255
        if brt>=0 and brt <0.2:
            print("#", end='', file=a)
        elif brt >=0.2 and brt < 0.4:
            print("O", end='', file=a)
        elif brt >=0.4 and brt < 0.6:
            print("|", end='', file=a)
        elif brt >=0.6 and brt < 0.8:
            print(",", end='', file=a)
        else:
            print(" ", end='', file=a)
    print("", file=a)
print("</pre>", file=a)
