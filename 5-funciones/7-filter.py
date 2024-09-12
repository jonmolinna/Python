amigos = [
    ("kendra", 29),
    ("Malina", 28),
    ("Noah", 25),
    ("Matias", 24),
    ("Sophia", 20),
]

age = lambda data: data[1] >= 25

res = list(filter(age, amigos))

for i in res:
    print(i)