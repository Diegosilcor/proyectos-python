#PROYECTO 1

# Concatenar cadenas de caracteres
# Supongamos que queremos crear una cadena que diga:
# Aprende a programar con ___________.

# organizacion = "Diego Silva Cordoba"

# print ("Aprende a programar con " + organizacion)
# print ("Aprende a programar con {}". format(organizacion))
# print (f"Aprende a programar con {organizacion}") #f-string La mejor opcion


# Mad Libs (Historias)

# adj = input("Adjetivo: ")
# verbo1 = input("Verbo: ")
# verbo2 = input("Verbo: ")
# sustantivo_plural = input ("Sustantivo (plural): ")

# madlib = f"Programar es tan {adj} Siempre me emociona por que me gusta {verbo2}. Aprende a {verbo2} con Diego Silva Cordoba y alcanza tus {sustantivo_plural} en la programacion"

# print(madlib)



#PROYECTO 2
# Adivinar un numero generado por la computadora, sera interactivo. El usuario adivinar un numero en un rango especifico y le vamos a decir si ese numoer en mayor, menor o igual al numero aleatorio generado por la computadora.

import random

def adivina_el_numero(x):
    
    
    print("=========================")
    print("¡Bienvenido(a) al juego! ")
    print("=========================")
    print ("Tu meta es adivinar el numero generado por la computadora.")
    
    numero_aleatorio = random.randint(1, x) # Numero aleatorio entre 1 y x.
    prediccion = 0
    while prediccion != numero_aleatorio:
        # El usuario ingresa un numero
        prediccion = int(input(f"Adivina un numero entre 1 y {x}: ")) # f-string
        
    if prediccion < numero_aleatorio:
        print("Intenta  otra vez. Este numero es muy pequeño. ")
    elif prediccion > numero_aleatorio:
        print("Intenta otra vez. Este numero es muy grande. ")


    print(f"¡Felicitaciones! Adivinaste el numero {numero_aleatorio} correctamente. ")


adivina_el_numero(10)
