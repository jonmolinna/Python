import functools

letters = ["H", "O", "L", "A"]

letter = functools.reduce(lambda x, y: x + y, letters)
print(letter)