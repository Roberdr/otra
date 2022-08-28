def main():
    lista = [
        'Hola.',
        'Estoy escribiendo en un archivo de texto.',
        'Adios.',
        ''
    ]

    lista2 = [
        'Hola, otra vez.',
        'Vuelvo a escribir por segunda vez.',
        'Adiós.'
    ]

    f=open('fichero.txt', 'w')
    for linea in lista:
        f.write(linea + '\n')

    f.close()

    f=open('fichero.txt', 'a')
    for linea in lista2:
        f.write(linea + '\n')

    f.close()

if __name__ == '__main__':
    main()