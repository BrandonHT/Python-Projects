from PIL import Image, ImageFilter

img = Image.open("./Pokedex/pikachu.jpg")
filtered_image = img.filter(ImageFilter.BLUR)
filtered_image.save("pikachu_blured.png", "png")
gray_image = img.convert('L')
gray_image.save("pikachu_gray.png", "png")

filtered_image.show()
gray_image.show()

resized_image = img.resize((200, 300))
resized_image.show()