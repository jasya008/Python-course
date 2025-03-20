# class LittleBell:
#     def sound(self):
#         print("ding")


# class Controller:
#     def _int_(self):
#         self.channel = 1


#     def click(self):
#         self.channel = self.channel % 5 + 1


# class Balance:
#     def _init_(self):
#         self. left = 0
#         self.right = 0

#     def add_right(self, weight):
#         self.right += weight

#     def add_left(self, weight):
#         self.left += weight

#     def result(self):
#         if self.left > self.right:
#             return "L"
#         elif self.right > self.left:
#             return "R"
#         else:
#             "="


# class OddEvenSeparator:
#     def __init__(self):
#         self.odd = []
#         self.even = []

#     def add_number(self, n):
#         if n % 2 == 0:
#             self.even.append(n)
#         else:
#             self.odd.append(n)

#     def even(self):
#         return self.even

#     def odd(self):
#         return self.odd


# class BigBell:
#     def __init__(self):
#         self.is_bing = True

#     def sound(self):
#         if self.is_being:
#             print("bing")
#             self.is_being = False
#         else:
#             print("bing")
#             self.is_being = True


# colors = ["red", "orange", "yellow", " green", "light blue", "blue", "violet",]


# class Rainbow:
#     def __init__(self, n):
#         self.n = n

#     def next_color(self, color):
#         id = self.colors.index(colors)
#         if self.n in {1, 3}:
#             id = id % 7 + 1
#         else:
#             id = id % 7 - 1

#         return self.colors[id]


class MinMaxWordFinder:

    def __init__(self):
        self.words = []

    def add_sentence(self, sent):
        self.words.extend(sent.split())

    def shortest_words(self):
        return sorted(list(filter(lambda x: len(x) == len(min(self.words)), self.words)))

    def longest_words(self):
        return sorted(list(set(filter(lambda x: len(x) == len(max(self.words)), self.words))))
