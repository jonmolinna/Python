import time

# Ver tiempo actual
print(time.ctime(time.time()))

# Ver tiempo actual
tiempo_actual = time.localtime()
tiempo = time.strftime("%B %d %y %H:%M:%S", tiempo_actual)

print(tiempo)