from PIL import Image, ImageOps, ImageDraw
import requests
from io import BytesIO
from os import getenv


# Load the image url from ENV
url = getenv('IMG_URL')

# fetch the image
response = requests.get(url)

# Load Image 
img = Image.open(BytesIO(response.content))

# Convert the image to grayscale.
img = ImageOps.grayscale(img)

# Equalize the image histogram
img = ImageOps.equalize(img)

# Creates a new image with the given mode and size.
dicedImg = Image.new('RGBA', (img.width, img.height), color='white')

# Calculate the dice dimension
dicew = 30 # dices are squre we just need the width
dicesize = int(img.width * 1.0/dicew)
diceh = int(img.height * 1.0/img.width * dicew)

# Create the normalize image
nim = Image.new("L", (img.width, img.height), 'white')

# Draw the normalize 
nimd = ImageDraw.Draw(nim)

# print the totla number of the dices you need to create the picture 
print ('you need %s dices for this' % (dicew * diceh))

# Go thru the matrix(image) match each pixel with one dices
for y in range(0, img.height-dicesize, dicesize):
    for x in range(0, img.width-dicesize, dicesize):
        thisSectorColor = 0 # Closure for each sector 
        for dicex in range(0, dicesize):
            for dicey in range(0, dicesize):
                thisColor = img.getpixel((x+dicex, y+dicey))
                thisSectorColor += thisColor
        thisSectorColor /= (dicesize ** 2)
        nimd.rectangle([(x, y), (x+dicesize, y+dicesize)], thisSectorColor)
        # match color range (0-255) with dice number
        diceNumber = (255-thisSectorColor) * 6 / 255 + 1
        print diceNumber,
    print
