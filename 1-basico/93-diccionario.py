students = [
    {
        'id': 1,
        'name': 'Kendra Contreras',
        'age': 28,
        'skill': 'Ui',
        'university': True,
    },
    {
        'id': 2,
        'name': 'Malina Tanase',
        'age': 27,
        'skill': 'React',
        'university': False,
    },
    {
        'id': 3,
        'name': 'Noah Saez',
        'age': 29,
        'skill': 'Kotlin',
        'university': True
    }
]

for student in students:
    # print(student.get('name'))
    for key, value in student.items():
        print(key, value)

    print("-----------------")