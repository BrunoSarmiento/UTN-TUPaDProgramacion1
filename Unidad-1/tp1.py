#Trabajo Practico n°1 - Bruno Sarmiento - Comision 2 - Enferrel

#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”

print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.

nombre:str = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla

nombre:str = input("Ingrese su nombre: ")
apellido:str = input("Ingrese su apellido: ")
edad:int = int(input("Ingrese su edad: "))
pais:str = input("Ingrese su lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {pais}")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.

radio:float = float(input("Ingrese el radio: "))

area:float = 3.14159 * (radio**2)
perimetro:float = 2*radio*3.14159

print(f"El área del circulo es: {area} y su perimetro es: {perimetro}")


# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

segundos:float = float(input("Ingrese una cantidad de segundos: "))
horas:float = segundos/3600

print(f"{segundos} segundos equivalen a {horas} horas")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.

num:int = int(input("Ingrese un numero para ver su tabla de multiplicar: "))
print(f"{num}*1 = {num*1}")
print(f"{num}*2 = {num*2}")
print(f"{num}*3 = {num*3}")
print(f"{num}*4 = {num*4}")
print(f"{num}*5 = {num*5}")
print(f"{num}*6 = {num*6}")
print(f"{num}*7 = {num*7}")
print(f"{num}*8 = {num*8}")
print(f"{num}*9 = {num*9}")
print(f"{num}*10 = {num*10}")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

num1:int = int(input("Ingrese el primer numero entero distinto de 0: "))
num2:int = int(input("Ingrese el segundo numero entero distinto de 0: "))
print(f"{num1}+{num2}={num1+num2}")
print(f"{num1}-{num2}={num1-num2}")
print(f"{num1}*{num2}={num1*num2}")
print(f"{num1}/{num2}={num1/num2}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
# modo: 𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔/(𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚**2)

peso:float = float(input("Ingrse su peso en kg: "))
altura:float = float(input("Ingrese su altura en metros: "))
imc:float = peso/(altura**2)
(print(f"Su imc es: {imc}"))

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
# TF = (9/5)*TC+32

temp_celsius:float = float(input("Ingrese temperatura en grados celsius: "))
temp_fahrenheit:float = (9/5)*temp_celsius+32
print(f"{temp_celsius}°C equivalen a {temp_fahrenheit}°F")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.

num1:float = float(input("Ingrese el primer numero: "))
num2:float = float(input("Ingrese el segundo numero: "))
num3:float = float(input("Ingrese el tercer numero: "))
promedio:float = (num1+num2+num3)/3
print(f"El promedio entre {num1}, {num2}, {num3} es: {promedio}")