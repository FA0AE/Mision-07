#Francisco Ariel Arenas Enciso
#A01369122
#Realización de la tarea 7 (ciclo while)


'''La función 'dividir' recibe de main los valores del dividendo y del divisor. Estos mediante un ciclo while
son restados con el fin de lograr obtener el resultado esperado utilizando solamente restas'''
def dividir(dividendo, divisor):
    residuo = dividendo
    cociente = 0
    while divisor <= residuo:
        residuo = residuo - divisor
        cociente += 1
    print(dividendo, "/", divisor, "=", cociente, ", sobran:", residuo)


'''La función 'encontrarMayor' no recibe nigún parametro pues es dentro de ella que se le pregunta al usuario los 
números que desea usar. Mediante un ciclo whule, y varios if's, se establece la relación y/o condición necesaria 
para obtener el resultado '''
def encontrarMayor():
    serieDeNumeros = 0
    valorNumeroMayor = 0
    while serieDeNumeros != -1:
        serieDeNumeros = int(input('''Por favor, escribe cualquier serie de números [Teclea -1 para salir]: '''))
        if serieDeNumeros < -1:
            print('No hay valor mayor')
        elif serieDeNumeros > valorNumeroMayor:
            valorNumeroMayor = serieDeNumeros
    if valorNumeroMayor == 0:
        print('No hay valor mayor')
    else:
        print(valorNumeroMayor, 'es el valor mayor')


'''La función main será la encargada de tener el menú para el usuario y es en donde se obtendrán los parametros
necesarios para la función 'dividir' '''
def main():
    opcion = -1
    while (opcion != 0):
        opcion = int(input('''
        -------------------------------------------
        Misión 07
        Autor: Francisco Ariel Arenas Enciso
        Matrícula: A01369122

        De las siguientes opciones, seleccione una:
        1. Calcular divisiones
        2. Encontrar el mayor
        3. Salir
        -------------------------------------------
        ¿Qué opción desea hacer? 
        '''))
        if opcion == 1:
            print('''
        -------------------------------------------
        Has elegido la opción 1: 'Calcular divisiones' 
            ''')
            dividendo = int(input('Por favor, escribe el valor del dividendo: '))
            divisor = int(input('Por favor, ahora escribe el valor del divisor:  '))
            dividir(dividendo, divisor)

        elif opcion == 2:
            print('''
        -------------------------------------------
        Has elegido la opción 2: 'Encontrar el mayor' 
            ''')
            encontrarMayor()

        elif opcion == 3:
            print('''
        -------------------------------------------
        Gracias por ejecutar el programa''')
            break

        elif opcion <= 0 or opcion > 3:
            print('''
        ERROR, teclea 1, 2 o 3''')


main()