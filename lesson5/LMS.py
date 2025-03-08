# from PIL import Image


# def transparency(input_file1, input_file2):
#     image_1 = Image.open(input_file1)
#     image_2 = Image.open(input_file2)

#     pixels_1 = image_1.load()
#     pixels_2 = image_2.load()

#     x, y = image_1.size
#     for i in range(x):
#         for j in range(y):
#             r1, g1, b1 = pixels_1[i, j]
#             r2, g2, b2 = pixels_2[i, j]

#             r = int(0.5 * r1 + 0.5 * r2)
#             g = int(0.5 * g1 + 0.5 * g2)
#             b = int(0.5 * b1 + 0.5 * b2)

#             pixels_1[i, j] = r, g, b

#     image_1.save("res.jpg")


# from PIL import Image

# replacer = input()

# im = Image.open("fruits.png")
# x, y = im.size

# cordinates = [
#     (0, 0), (x//2, 0),
#     (0, y//2), (x//2, y//2)
# ]

# v = im.crop((0, 0, x//2, y//2))
# m = im.crop((x//2, 0, x, y//2))
# k = im.crop((0, y//2, x//2, y))
# s = im.crop((x//2, y//2, x, y))

# parts = {
#     "1": v,
#     "2": m,
#     "3": k,
#     "4": s
# }

# for i in range(4):
#     im.paste(parts[replacer[i]], cordinates[i])


# im.save("cycle.png")


# from PIL import Image, ImageFilter

# def motion_blur(n):
#     im = Image.open("c:/Users/Jasmina/Desktop/Yandex lessons Python/lesson4/owl.jpg")
#     im = im.transpose(method=Image.Transpose.ROTATE_270)
#     im2 = im.filter(ImageFilter.GaussianBlur(n))
#     im2.save("res.jpg")


# motion_blur(7)


# from PIL import Image
# image_1 = Image.open()
# image_2 = Image.open()

# x,y = input().split()
# x = int(x)
# y = int(y)

# reflect = input()

# if reflect == "reflect":
#     image_2 = image_2.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT)

# image_1.paste(image_2, (x, y), image_2)
# image_2.save("happy_camel.png")


# from PIL import Image, ImageFilter

# image = Image.open('c:/Users/Jasmina/Desktop/Yandex lessons Python/lesson4/owl.jpg')
# x,y = image.size

# number = int(input())


# ref = image.transpose(method=Image.Transpose.FLIP_TOP_BOTTOM)
# image_2 = ref.filter(ImageFilter.GaussianBlur(number))
# res = image.resize((x,y ** 2))

# res.paste(image,(0,0))
# res.paste(ref,(0,y))
# res.save('res.jpg')


# from PIL import Image


# def twist_image(input_file_name, output_file_name):
#     image = Image.open(input_file_name)

#     x, y = image.size

#     left_half = image.crop((0, 0, x // 2, y))
#     right_half = image.crop((x // 2, 0, x, y))

#     res = Image.new('RGB', (x, y))
#     res.paste(right_half, (0, 0))
#     res.paste(left_half, (x // 2, 0))

#     res.save(output_file_name)


# from PIL import Image

# def make_preview(size, n_colors):
#     with Image.open("image.jpg") as image:
#         image.thumbnail(size)
#         res = image.quantize(colors=n_colors)
#         res.save("res.bmp")
