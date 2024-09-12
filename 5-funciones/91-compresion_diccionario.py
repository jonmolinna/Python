# diccionario = {key: expresion for (key, value) in iterable}

# Example 1
city_f = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}

city_c = {key: round((value-32) * (5/9)) for (key, value) in city_f.items()}

print(city_c)

# Example 2
clima = {'New York': 'Nieve', 'Boston': 'Soleado', 'Los Angeles': 'Soleado', 'Chicago': 'Nublado'}

clima_sunny = {key: value for (key, value) in clima.items() if value == 'Soleado'}

print(clima_sunny)

# Example 3
city_f_2 = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}

clima_res = {key: ("CALOR" if value >= 40 else "FRIO") for (key, value) in city_f_2.items()}

print(clima_res)

# Example 4
def check_temp(value):
    if value >= 70:
        return 'CALOR'
    elif 60 >= value >= 40:
        return 'NORMAL'
    else:
        return 'FRIO'

cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}

temperatura = {key: check_temp(value) for (key, value) in cities.items()}

print(temperatura)