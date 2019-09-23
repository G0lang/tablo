from PIL import Image, ImageOps, ImageDraw


img = Image.open("/tmp/1.jpg")
img = ImageOps.grayscale(img)
img = ImageOps.equalize(img)
dicedImg = Image.new('RGBA', (img.width, img.height), color='white')
dicew = 30
dicesize = int(img.width * 1.0/dicew)
diceh = int(img.height * 1.0/img.width * dicew)
nim = Image.new("L", (img.width, img.height), 'white')
nimd = ImageDraw.Draw(nim)
print ('you need %s dices for this' % (dicew * diceh))
for y in range(0, img.height-dicesize, dicesize):
    for x in range(0, img.width-dicesize, dicesize):
        thisSectorColor = 0
        for dicex in range(0, dicesize):
            for dicey in range(0, dicesize):
                thisColor = img.getpixel((x+dicex, y+dicey))
                thisSectorColor += thisColor
        thisSectorColor /= (dicesize ** 2)
        nimd.rectangle([(x, y), (x+dicesize, y+dicesize)], thisSectorColor)
        diceNumber = (255-thisSectorColor) * 6 / 255 + 1
        print diceNumber,
    print
nim.show()
