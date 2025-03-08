# Lambda anonimus functions repeat

# words = ["tiger", "Fox", "Wolf", "cat"] 
# print(sorted(words, key=lambda el: -el[0].isupper())) Fox,Wolf,tiger... sort from uppercase



# words = ["tiger", "fox", "wolf", "cat"]

# print(sorted(words, key=lambda el: [len(el), el])) ['cat', 'fox', 'wolf', 'tiger']  sort from lengt








# ANY // ALL

# print(all([2,3,4,5,0])) find False
# print(any([2,3,4,0,4])) find True


# def any (iterable):
#     for el in iterable:
#         if bool(el) == True:
#             return True
#         return False
    


# def all (iterable):
#     for el in iterable:
#         if bool(el) == False:
#             return True
#         return False



# words = "Enjoy every moment".split()

# print(any(len(i) > 5 for i in words)) True
# print(any(map (lambda x: len(x)> 5, words))) True







# SYS - library System-specific parameters and functions

# import sys


# for line in sys.stdin: infinity input
#     print(line)

# print(list(map(str.strip, sys.stdin)))
# print(sys.stdin.read())

