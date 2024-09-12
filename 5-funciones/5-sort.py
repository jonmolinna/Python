# Ejemplo 1
students = ["Kendra", "Eung", "Matias", "Meryem"]

students.sort(reverse=True)

for i in students:
    print(i)

# Ejemplo 2
students = [
    ('Kendra', 'A', 26),
    ('Eung', 'B', 22),
    ('Matias', 'A', 27),
    ('Meryem', 'C', 20),
    ('Dallas', 'A', 28),
]

cali = lambda tupla: tupla[1]

students.sort(key=cali)

for i in students:
    print(i)