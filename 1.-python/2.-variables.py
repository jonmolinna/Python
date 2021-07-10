# Crea un variable con el precio de un juguete que es 15
# muestra en pantalla su valor
# el precio baja a 12. Asigna el nuevo valor a la variable que has creado.
# Muestra el nuevo valor por pantalla
precio = 15
precio = 12
precio = precio + 10
print(precio)


# Crea una variable "caramelo" con valor 5.
# Crea una variable "precio" con valor 2.
# crea otra variable que calcule el coste de comprar los caramelos
# muestra el valor del coste por pantalla
# 
# cambia el numero de caramelos a 8
# cambia el precio a 3
# calcula el nuevo coste
# muestra en pantall 

caramelo = 8
precio = 3
coste = caramelo * precio
print(coste)

# Tenemos 15 euros de ahorros 
# Nuestro abuelo nos da 10 euros nos gastamos 2 euros en un helado
# Nuestra tia nos da 5 euros
# Nos gastamos 7 euros en un juego.
# ¿Cuanto dinero tendremos?

ahorro = 15 + 10 - 2 + 5 - 7
print(ahorro)

# El numero de plazas totales de un autobus es de 46
# El numero de plazas ocupdas es de 32 y el numero de plazas reservadas es de 14
# Crea una variable, plazas vacias, cuyo valor sea el resultado de restar
# El numero de plazas totales menos el numero de plazas ocupadas mas plazas reservadas
# crea una variable, autobus lleno, cuyo valor sea el resultado de comparar
# el numero de plazas totales con el numero de plazas ocupadas + plazas reservadas

totales = 46
ocupadas = 32
reservadas = 14
plaza_vacia = totales - (ocupadas + reservadas)
bus_lleno = totales == ocupadas + reservadas
print(plaza_vacia)

# En un juego hay que conseguir 100 puntos entre 2 niveles de que consta:
# en el nivel 1 tenemos: 48 puntos, en el nivel 2 tenemos: 62 puntos
# calcula los puntos totales conseguidos en el juego
# Crea una variable cuyo valor sea el resultado de comparar si los puntos totales conseguidos son
# mayor o igual que los puntos a conseguir
# Muestra el valor de la variable por pantalla

nivel1 = 48
nivel2 = 62
puntos = nivel1 + nivel2
puntos_totales = nivel1 + nivel2 >= 100
print(puntos_totales)

# nos dan un dato 5 kilometros
# converitr este dato a metros y luego a centimetros

metros = 5 * 1000
centimetros = metros * 100
print({"metros": metros, "centimetros": centimetros})

# Nos dan un dato: 3 dias 
# Convertir este dato a horas y luego a minutos

horas = 3 * 24
minutos = horas * 60
print({"Horas" : horas, "Minutos" : minutos})