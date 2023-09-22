import random
import math
import os
import sys
def generarNumero():
    numero = random.randint(1000,9999)
    return numero
def separarDigitos(numero):
    digito1 = numero // 1000
    digito2 = (numero // 100) % 10
    digito3 = (numero // 10) % 10
    digito4 = numero % 10
    return digito1, digito2, digito3, digito4
def compararDigitos(numero, digito1, digito2, digito3, digito4):
    if numero == digito1:
        return 1
    elif numero == digito2:
        return 1
    elif numero == digito3:
        return 1
    elif numero == digito4:
        return 1
    else:
        return 0
def main():
    nombrejugador = input("Ingresa tu nombre: ")
    print("Hola", nombrejugador)
    numero = generarNumero()
    while True:
        digito1, digito2, digito3, digito4 = separarDigitos(numero)
        if digito1 == digito2:
            numero = generarNumero()
        elif digito1 == digito3:
            numero = generarNumero()
        elif digito1 == digito4:
            numero = generarNumero()
        elif digito2 == digito3:
            numero = generarNumero()
        elif digito2 == digito4:
            numero = generarNumero()
        elif digito3 == digito4:
            numero = generarNumero()
        else:
            break

    digito1, digito2, digito3, digito4 = separarDigitos(numero)
    print("Bienvenido al juego de los muertos y heridos.")
    print("Tienes 10 intentos para adivinar el número de 4 dígitos.")
    print("Los dígitos son del 0 al 9 y no se repiten.")
    print("Si adivinas un dígito en la posición correcta, tienes un herido.")
    print("Si adivinas un dígito en la posición incorrecta, tienes un muerto.")
    print("Si adivinas todos los dígitos en la posición correcta, ganas.")
    print("Si no adivinas todos los dígitos en la posición correcta, pierdes.")
    print("¡Buena suerte!")
    intentos = 0
    while intentos < 10:
        intentos = intentos + 1
        print("Intento", intentos)
        print("el número es", numero)
        adivinar = int(input("Ingresa el número de 4 dígitos: "))
        if adivinar == numero:
            
            print("¡Felicidades! Ganaste.")
            archivo = open("muertosyheridos.txt", "a")
            archivo.write("jugador: "+ nombrejugador +"\n")
            archivo.write("El número a adivinar era: " + str(numero) + "\n")
            archivo.write("El número de intentos fue: " + str(intentos) + "\n")
            archivo.close()   
            break
        else:
            digitoAdivinar1, digitoAdivinar2, digitoAdivinar3, digitoAdivinar4 = separarDigitos(adivinar)
            heridos = compararDigitos(digitoAdivinar1, digito1, digito2, digito3, digito4) + compararDigitos(digitoAdivinar2, digito1, digito2, digito3, digito4) + compararDigitos(digitoAdivinar3, digito1, digito2, digito3, digito4) + compararDigitos(digitoAdivinar4, digito1, digito2, digito3, digito4)
            muertos = 0
            if digitoAdivinar1 == digito1:
                muertos = muertos + 1
            elif digitoAdivinar1 == digito2:
                muertos = muertos + 1
            elif digitoAdivinar1 == digito3:
                muertos = muertos + 1
            elif digitoAdivinar1 == digito4:
                muertos = muertos + 1
            if digitoAdivinar2 == digito1:
                muertos = muertos + 1
            elif digitoAdivinar2 == digito2:
                muertos = muertos + 1
            elif digitoAdivinar2 == digito3:
                muertos = muertos + 1
            elif digitoAdivinar2 == digito4:
                muertos = muertos + 1
            if digitoAdivinar3 == digito1:
                muertos = muertos + 1
            elif digitoAdivinar3 == digito2:
                muertos = muertos + 1
            elif digitoAdivinar3 == digito3:
                muertos = muertos + 1
            elif digitoAdivinar3 == digito4:
                muertos = muertos + 1
            if digitoAdivinar4 == digito1:
                muertos = muertos + 1
            elif digitoAdivinar4 == digito2:
                muertos = muertos + 1
            elif digitoAdivinar4 == digito3:
                muertos = muertos + 1
            elif digitoAdivinar4 == digito4:
                muertos = muertos + 1
            print("Tienes", heridos, "heridos y", muertos, "muertos.")
    if intentos == 10:
        print("Lo siento, perdiste.")
main()


