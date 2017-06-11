from PIL import Image

test_image = "assets/tom.jpg"
original = Image.open(test_image)
original.show()

width, height = original.size   # Get dimensions
left = width/4
top = height/4
right = 3 * width/4
bottom = 3 * height/4

# cropped_Image = original.crop((left, top, right, bottom))

cropped_Image = original.crop((0, 0, 960, 960))


cropped_Image.show()
cropped_Image.save('assets/croped_tom.PNG')


