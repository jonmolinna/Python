# Si un modulo contiene esto, es porque se ejecutara de manera independiente

if __name__ == '__main__':
    print('Estas ejecutando este archivo de manera directa')
else:
    print('Has importado este archivo, y se esta ejecutando de manera indirecta')