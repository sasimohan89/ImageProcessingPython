from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
print(img)
print(img.format)
print(img.size)
print(img.mode)

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save('BLUR.png', 'png')

filtered_img = img.filter(ImageFilter.SMOOTH)
filtered_img.save('SMOOTH.png', 'png')

filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img.save('SHARPEN.png', 'png')

filtered_img = img.convert('L')
flipped = filtered_img.rotate(90)
flipped.save('grey.png', 'png')
# flipped.show()

resized = filtered_img.resize((300, 300))
resized.save('small.png', 'png')
# resized.show()

cropped = filtered_img.resize((300, 300))
box = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.show()