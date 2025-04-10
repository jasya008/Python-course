# class Acellularia:
#     pass


# class Cellularia:
#     pass


# class Prokaryota(Cellularia):
#     pass


# class Eukaryota(Cellularia):
#     pass


# class Unicellularia(Eukaryota):
#     pass


# class Fungi(Eukaryota):
#     pass


# class Plantae(Eukaryota):
#     pass


# class Animalia(Eukaryota):
#     pass


# class User:
#     def solve(self, n):
#         pass


# class Student(User):
#     pass


# class Teacher(User):
#     def check_solution(self, user, n):
#         pass

#    class Admin(User):
#         def edit(self, n):
#             pass

#     class SuperAdmin(Admin):
#         def grant(self, user):
#             pass


# class BaseObject:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z

#     def get_coordinates(self):
#         return [self.x, self.y, self.z]


# class Block(BaseObject):
#     def shatter(self):
#         self.x = None
#         self.y = None
#         self.z = None
#         return [self.x, self.y, self.z]


# class Entity(BaseObject):
#     def move(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z


# class Thing(BaseObject):
#     pass


# import math


# class Square:
#     def __init__(self, a):
#         self.a = a

#     def area(self):
#         return self.a ** 2


# class Circle:
#     def __init__(self, r):
#         self.r = r

#     def area(self):
#         return math.pi * self.r ** 2
    
#     def to_square(self):
#         a = 2 * self.r / math.sqrt(2)
#         return Square(a)

# c = Circle(10)
# s = c.to_square()
# print(s.area())  