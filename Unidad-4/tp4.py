import random

#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(0,101):
    print(i)

print("---------------------------")

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

num = input("Ingrese un número entero: ")
bandera:bool = True
cant_digitos:int = 0

while bandera:
    if num.isalpha():
        num = input("Ingrese un número entero: ")
    elif num.isdigit():
        cant_digitos = 0
        for caracter in num:
            cant_digitos += 1
        print(f"La cantidad de dígitos que contiene el número es: {cant_digitos}")
        bandera = False
    elif num.startswith("-") and num[1:].isdigit():
        parte_numerica = num[1:]
        cant_digitos = 0
        for caracter in parte_numerica:
            cant_digitos += 1
        print(f"La cantidad de dígitos que contiene el número es: {cant_digitos}")
        bandera = False
    else:
        num = input("Ingrese un número entero: ")

print("---------------------------")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

num1:str
num2:str
aux:int = 0
contador:int = 0
bandera:bool = True

while bandera:

    num1 = input("Ingrese un numero entero: ")
    num2 = input("Ingrese otro numero entero: ")

    if num1.isalpha() or num2.isalpha():
        num1 = input("Ingrese un número entero: ")
        num2 = input("Ingrese otro numero entero: ")
    elif num1.isdigit() and num2.isdigit():
        num1 = int(num1)
        num2 = int(num2)
        for i in range(num1+1,num2):
                contador += i
        print(f"La suma de los numeros es: {contador}")
        bandera = False
    elif num1.startswith("-") and num1[1:].isdigit() and num2.startswith("-") and num2[1:].isdigit():
        num1 = int(num1)
        num2 = int(num2)
        for i in range(num1+1,num2):
                contador += i
        print(f"La suma de los numeros es: {contador}")
        bandera = False
    elif (num1.isdigit() and num2.startswith("-") and num2[1:].isdigit()) or (num2.isdigit() and num1.startswith("-") and num1[1:].isdigit()):
        num1 = int(num1)
        num2 = int(num2)
        for i in range(num1+1,num2):
                contador += i
        print(f"La suma de los numeros es: {contador}")
        bandera = False
    else:
        num1 = input("Ingrese un número entero: ")
        num2 = input("Ingrese otro numero entero: ")

print("---------------------------")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0

num:int
suma:int = 0
bandera:bool = True

while bandera:
    num=input("Ingrese un numero entero: ")

    if num.isalpha():
        num=input("Ingrese un numero entero: ")
    elif num.isdigit() or (num.startswith("-") and num[1:].isdigit()):
        num=int(num)
        if num != 0:
            suma = suma+num
        elif num == 0:
            print(f"La suma es: {suma}")
            bandera=False
    else:
        num=input("Ingrese un numero entero: ")

print("---------------------------")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

num:int = random.randint(0, 9)
num_user:int = input("Ingrese un numero entero: ")
contador:int = 1
bandera:bool = True

while bandera:
    if num_user.isalpha():
        num_user=input("Ingrese un numero entero: ")
        contador += 1
    elif num_user.isdigit():
        num_user=int(num_user)
        if num_user == num:
            print(f"Felicitaciones, acerto en {contador} intentos")
            bandera=False
        elif num_user != num:
            num_user=input("No ha aceertado. Ingrese otro numero: ")
            contador += 1
    else:
        num_user=input("Ingrese un numero entero: ")
        contador += 1

print("---------------------------")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

for i in range (100,0, -2):
    print (i)

print("---------------------------")

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

num:str = input("Ingrese un numero entero positivo: ")
suma:int = 0
bandera:bool = True

while bandera:
    if num.isalpha():
        num = input("Ingrese un número entero: ")
    elif num.isdigit():
        num = int(num)
        for i in range(0,num):
                suma = suma+i
        print(f"La suma de los numeros es: {contador}")
        bandera = False

print("---------------------------")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

num:str
cont_par:int=0
cont_impares:int=0
cont_negativos:int=0
cont_positivos:int=0

