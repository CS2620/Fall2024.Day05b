from PIL import Image

image = Image.open("car.jpg")
data = image.load()
for y in range(image.height):
    for x in range(image.width):
        #pixel = data[x,y]
        r,g,b,*_ = data[x,y]

        mask = 0b111110000

        r = r & mask
        g = g & mask
        b = b & mask

        data[x,y] = (r,g,b)

image.save("binary-car.png")
