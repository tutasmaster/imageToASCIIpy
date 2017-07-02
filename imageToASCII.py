from PIL import Image

a = open("image.html","w")

symbols = [chr(219),"#","O","A","T","I","i",";",",","."," "]
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
        if A > 0:
            pos = round(brt/symbolSize)
        else:
            pos = len(symbols)
        print(symbols[pos - 1],end="",file=a)
    print("", file=a)
print("</pre>", file=a)
