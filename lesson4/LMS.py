# r,g,b = input().split()
# r = int(r)
# g = int(g)
# b = int(b)

# print (255-r, 255-g, 255-b)


# from PIL import Image

# image = Image.open('image.jpg')

# w, h = image.size

# pixel = []

# for x in range(w):
#     for y in range(h):
#         r, g, b = image.getpixel((x, y))
#         pixel.append([r, g, b])

# avr = [sum(x)//len(x) for x in zip(*pixel)]

# print(' '.join(str(x) for x in avr))


# from PIL import Image


# def mirror():
#     with Image.open('c:/Users/Jasmina/Desktop/Yandex lessons Python/lesson4/owl.jpg') as im:
#         im = im.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT)
#         im = im.transpose(method=Image.Transpose.ROTATE_270)
#         im.save('res.jpg')


# mirror()


# from PIL import Image

# with Image.open('yoda.png') as im:
#     pixels = im.load()
#     x, y = im.size
#     n = int(input())

#     for i in range(x):
#         for j in range(y):
#             r, g, b = pixels[i, j]
#             diference = min(r, g, b) - max(r, g, b)
#             r = r + diference * n
#             g = g + diference * n
#             b = b + diference * n
#             pixels[i, j] = (r, g, b)

# im.save('sense.png')
# im.show()
