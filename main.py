# Lambda

# text = input().split()

# max_len = max(map(len, text))

# res = map(lambda el: el.rjust(max_len, "*"), text)

# print("\n".join(res))


# def find_farthest_orbit(list_of_orbits):
#     no = [orbit for orbit in list_of_orbits if orbit[0] != orbit[1]]

#     areas = []
#     for a, b in no:
#         areas.append(3.14 * a * b)

#     max_area = max(areas)
#     index = areas.index(max_area)

#     return no[index]


# a = str(a)

# list_a = []

# for i in range(len(a) - 1):
#     list_a.append((a[i], a[i + 1]))


# for num in list_a:
#     print(chr(int(num[0] + num[1])))


# a = 6511597110098101107


# a_str = str(a)

# translated = ''.join(chr(int(a_str[i:i+2])) for i in range(0, len(a_str), 2))

# print(translated)


# def express(*a):
#     def b(c, d):
#         e = len(c) >= 8
#         f = len(c) != len(set(c))
#         g = not any(h.isdigit() and int(h) % 2 == 0 for h in c)
#         i = (d + 1) % 7 != 0
#         return e and f and g and i

#     return [x[1] for x in filter(lambda x: b(x[1], x[0]), enumerate(a))]

# data = ['West Ham', 'Liverpool Central', 'Romford-3', 'Richmond', 'Tottenham Hale-1', 'Farringdon-2', 'Lewisham', 'Ilford', 'Cambridge']

# result = express(*data)

# print(*result, sep='\n')


# def typification(data):
#     result = {}
#     for item in data:
#         item_type = item.__class__.__name__
#         if item_type not in result:
#             result[item_type] = []
#         result[item_type].append(item)
#     return result


# def secret_sort(secret_avatars):
#     vowels = {"a", "e", "i", "o", "u"}

#     def count_vowels_on_odd_indices(name):
#         return sum(1 for i, char in enumerate(name.lower()) if i % 2 != 0 and char in vowels)

#     secret_avatars.sort(key=lambda name: (count_vowels_on_odd_indices(name), secret_avatars.index(name)))


def secret_sort(secret_avatars):
    d = {}

    for name in secret_avatars:
        count = sum(1 for i, char in enumerate(name) if i %
                    2 == 1 and char in 'aeiouyAEIOUY')
        d[name] = count

    secret_avatars.sort(key=lambda name: d[name])
