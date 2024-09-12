names = ["Kendra", "Malina", "Noah"]
password = ("123", "abc", "contra")

# users = zip(names, password)
users = list(zip(names, password))

for i in users:
    print(i)