# class FoodInfo:
#     def __init__(self, protein, fats, carbohydrates):
#         self.protein = protein
#         self.fats = fats
#         self.carbohydrates = carbohydrates

#     def get_proteins(self):
#         return self.protein

#     def get_fats(self):
#         return self.fats

#     def get_carbohydrates(self):
#         return self.carbohydrates

#     def get_kcalories(self):
#         return (4 * self.protein + 9 * self.fats + 4 * self.carbohydrates)

#     def __add__(self, other):
#         protein = self.protein + other.protein
#         fats = self.fats + other.fats
#         carbohydrates = self.carbohydrates + other.carbohydrates
#         return FoodInfo(protein, fats, carbohydrates)


# class ChairLeg:
#     def __init__(self, length):
#         self.length = length

#     def __mul__(self, other):
#         self.length *= other
#         return self

#     def __rmul__(self, other):
#         return self.__mul__(other)

#     def __truediv__(self, other):
#         self.length /= other
#         return self

#     def __mod__(self, other):
#         return self. length % other


# class Potato:
#     def __init__(self, n):
#         self.n = n

#     def __itruediv__(self, n):
#         self.n /= n
#         return self

#     def __itruediv__(self, n):
#         new_n = self.n / n
#         return Potato(new_n)

#     def __str__(self):
#         return f"Potato({self.n})"


class Scrabble:
    def __init__(self, word):
        self.word = word
        self.book = {
            1: ('A', 'E', 'I', ' L', ' N', 'O', ' R', 'S', ' T', 'U'),
            2: ('D', 'G'),
            3: ('B', 'C', 'M', 'P'),
            4: ('F', 'H', 'V', 'W', 'Y'),
            5: ('K'),
            8: ('J', 'X'),
            10: ('Q', 'Z')
        }

    def __call__(self, word):
        points = 0

        if all(map(lambda x: x in self.word, word)):        
            for w in word:
                for key, letters in self.book.items():
                    if w in letters:
                        points += key
            return points


