# SHOW IMAGE WITH LIBARRY PILLOW
# from PIL import Image
# im = Image.open("c:/Users/Jasmina/Desktop/Yandex lessons Python/lesson4/cat.jpg")

# print(im.format, im.size, im.mode)

# im.show()


# CHANGE IMAGE SIZE AND SAVE + ADD BACKGROUND COLOR

# from PIL import Image, ImageOps
# size = (100, 150)
# with Image.open("c:/Users/Jasmina/Desktop/Yandex lessons Python/lesson4/cat.jpg") as im:
#     ImageOps.contain(im, size).save("imageops_contain.webp")
#     ImageOps.cover(im, size).save("imageops_cover.webp")
#     ImageOps.fit(im, size).save("imageops_fit.webp")
#     ImageOps.pad(im, size, color="#fff").save("imageops_pad.webp")

#     im.thumbnail(size)
#     im.save("image_thumbnail.webp")



# DRAW ON IMAGE (Make a new image with a draw on it)

# from PIL import Image, ImageDraw

# im = Image.new("RGB", (500, 500), (200, 200, 100))

# drawn = ImageDraw.Draw(im)

# im.save("drawn.jpg")



