import sys


# Nerds

# overall = int(input())
# list2 = []

# for _ in range(overall):
#     N = int(input())
#     list1 = []
#     for n in range(N):
#         input_data = input().split()
#         if len(input_data) > 1 and int(input_data[1]) == 5:
#             list1.append(True)
#     list2.append(any(list1))

# print("YES" if all(list2) else "NOPE")


# import sys

# list_students = []

# for line in sys.stdin:
#     line = line.strip()
#     list_students.append(int(line))


# print(sum(list_students)/len(list_students) if list_students else -1)

# import sys

# overall = []

# for line in sys.stdin:
#     cucumber = []
#     tomato = []
#     line = line.strip()
#     numbers = line.split()

#     for number in numbers:
#         cucumber.append(number) if "0" in number else tomato.append(number)

#     overall.append(len(tomato) >= len(cucumber))

# print('EVERGREEN TOMATOS' if all(overall) else "ALUMNIUM CUCUMBERS")


# lines = sys.stdin.readlines()
# comment_lines = sum(1 for line in lines if line.strip().startswith('#'))
# print(comment_lines)


# import sys

# print(any('0' in line.split() for line in sys.stdin))



# import sys