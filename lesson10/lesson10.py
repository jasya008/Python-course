# def func(a, b: list):
#     b.append(a)
#     return b


# a1 = 23

# b1 = [2, 4, 5, 6]

# res = func(a1, b1) func touch the list and change it

# print(res)
# print(a1)
# print(b1) change the list


# On this way the list stay unchanged
# def func(a, b: list):
#     a = a - 1
#     b_res = b[:] [:] or method copy help to make another new list with changes
#     b_res.append(a)

#     return b_res


# a1 = 23
# b1 = [21, 34, 6]

# res = func(a1, b1)
# print(res)
# print(a1)
# print(b1)


class Knight:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def can_move(self, row1, col1):
        if not (0 <= row1 < 8 and 0 <= col1 < 8):
            return False
        row_diff = abs(self.row - row1)
        col_diff = abs(self.col - col1)
        return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)

    def set_position(self, row1, col1):
        if 0 <= row1 < 8 and 0 <= col1 < 8:
            self.row = row1
            self.col = col1

    def get_color(self):
        return self.color

    def char(self):
        return "N"
