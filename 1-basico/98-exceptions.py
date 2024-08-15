try:
    numerador = int(input('Ingrese un numero: '))
    denominador = int(input('Ingrese un numero: '))

    resultado = numerador / denominador
    print(resultado)

except ZeroDivisionError as err:
    print("No puedes dividir por cero!", err)
except ValueError as err:
    print("Ingrese solo numero", err)
except Exception as err:
    print('Algo salio mal', err)
finally:
    print("Esto se ejecuta siempre")