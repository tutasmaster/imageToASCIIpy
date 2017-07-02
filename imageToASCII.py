from PIL import Image

a = open("image.html","w")

symbols = [chr(219),"#","O","I","i",";","."," "]
symbolSize = 1/len(symbols)

im = Image.open("sample.png").convert('RGB')
px = im.load()
width,height = im.size

print("<pre style=\"font: 10px/5px monospace; text-align: center;\">", file=a)

for y in range(0, height):
    for x in range(0, width):
        pxRGB = im.getpixel((x,y))
        R,G,B = pxRGB
        brt = sum([R,G,B])/3/255
        pos = round(brt/symbolSize)
        print(symbols[pos - 1],end="",file=a)
    print("", file=a)
print("</pre>", file=a)
