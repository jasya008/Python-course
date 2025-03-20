# import random


# def make_bingo():
#     res = []
#     numbers = set()
#     for i in range(5):
#         a = []
#         for j in range(5):
#             if i != 2 or j != 2:
#                 while True:
#                     k = random.randint(1, 75)
#                     if k not in numbers:
#                         a.append(k)
#                         numbers.add(k)
#                         break
#             else:
#                 a.append(0)
#         res.append(tuple(a))
#     return tuple(res)


# import math
# a = float(input())
# a = int(a * 1000)

# if a % 10 >= 5:
#     print(math.ceil(a/10)/100)


# import string
# import random

# text = string.ascii_letters + string.digits
# dublicates = ["l", "I", "1", "0", "o", "O"]

# for t in text:
#     if t in dublicates:
#         text = text.replace(t, "")


# def generate_password(m):
#     return "".join(random.choices(text, k=m))

# # def main(n,m):
#     res = []
#     while True:
#         pasw = generate_password(m)
#         if pasw not in res:
#             res.append(pasw)
#             if len(res) == n:
#                 return n


# import math

# def radians_to_degrees(radians):
#     degrees = math.degrees(radians)
#     return degrees % 360

# radians = float(input())
# print(radians_to_degrees(radians))


# import string
# import random

# text = string.ascii_letters + string.digits
# dublicates = ["l", "I", "1", "0", "o", "O"]

# for t in dublicates:
#     text = text.replace(t, "")


# def generate_password(m):
#     while True:
#         password = "".join(random.sample(text, m))
#         if len(set(password)) == m and string.ascii_lowercase in password and string.ascii_uppercase in password and string.digits in password:
#             return password


# def main(n, m):
#     res = []
#     while len(res) < n:
#         pasw = generate_password(m)
#         if pasw not in res:
#             res.append(pasw)
#     return res


# from datetime import datetime
# from math import sin, pi

# day1, month1, year1 = map(int, input().split('.'))
# day2, month2, year2 = map(int, input().split('.'))

# birth = datetime(year1, month1, day1)
# biorithm = datetime(year2, month2, day2)
# T = (biorithm - birth).days

# phys = round(sin((2 * pi * T) / 23) * 100, 2)
# emotion = round(sin((2 * pi * T) / 28) * 100, 2)
# intellect = round(sin((2 * pi * T) / 33) * 100, 2)

# print(phys)
# print(emotion)
# print(intellect)


from datetime import datetime


def observation_day(*dates):
    today = datetime(2020, 1, 1)
    valid_dates = []

    for date_str in dates:
        year, month, day = map(int, date_str.split('-'))
        date = datetime(year, month, day)
        if date >= today and day % 3 != 0:
            valid_dates.append(date)

    nearest_date = min(valid_dates)
    days_until = (nearest_date - today).days
    weekday = int(nearest_date.strftime('%w'))
    if weekday == 0:
        weekday = 7

    print(days_until, weekday)
