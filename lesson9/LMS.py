# class Animal:
#     def breathe(self):
#         pass

#     def eat(self):
#         pass


# class Fish(Animal):
#     def swim(self):
#         pass

# class Bird(Animal):
#     def lay_eggs(self):
#         pass

# class FlyingBird(Bird):
#     def fly(self):
#         pass


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
#         return None


# class Entity(BaseObject):
#     def move(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z


# class Thing(BaseObject):
#     pass


class User:
    def __init__(self, name):
        self.name = name

    def send_message(self, user, message):
        print(f"Message to {user.name}: {message}")

    def post(self, message):
        print(f"{self.name} posted: {message}")

    def info(self):
        return ""

    def describe(self):
        print(f"This is a user named {self.name}. {self.info()}")


class Person(User):
    def __init__(self, name, age):
        info = f"Age: {age}"

    def subscribe(self, user: User):
        pass



class Community(User):
    def __init__(self,name, short_desc):
        pass

    def info(self):
        return "Описание..."
        

