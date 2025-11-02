import funciones

#Ejercico 1

funciones.imprimir_hola_mundo()

#Ejercicio 2

nombre:str=input("Ingrese su nombre: ")
funciones.saludar_usuario(nombre)

#Ejercicio 3

nombre:str=input("Ingrese su nombre: ")
apellido:str=input("Ingrese su apellido: ")
edad:int=input("Ingrese su edad(en numeros):")
residencia:str=input("Ingrese su lugar de residenca: ")
funciones.informacion_personal(nombre,apellido,edad,residencia)

#Ejercicio 4

radio:float=float(input("Ingrese el radio del circulo(en numeros): "))
area=funciones.calcular_area_circulo(radio)
perimetro=funciones.calcular_perimetro_circulo(radio)
print(f"El area del cirulo con radio: {radio} es: {area}")
print(f"El perimetro del cirulo con radio: {radio} es: {perimetro}")

#Ejercicio 5

segundos:float=float(input("Ingrese la cantidad de segundos que desea convertir en horas "))
horas:float=funciones.segundos_a_horas(segundos)
print(f"{segundos} segundos equivalen a {horas} horas")

#Ejercicio 6

numero:int=int(input("Ingese el numero(entero) del que desea saber la tabla de multiplicar: "))
funciones.tabla_multiplicar(numero)

#Ejercicio 7

a = float(input("Ingrese el primer numero: "))
b = float(input("Ingrese el segundo numero: "))
resultado=funciones.operaciones_basicas(a, b)

print(f"{a}+{b} = {resultado[0]}\n"
      f"{a}-{b} = {resultado[1]}\n" \
      f"{a}*{b} = {resultado[2]}\n" \
      f"{a}/{b} = {resultado[3]}")

#Ejercicio 8

peso = float(input("Ingrese el peso: "))
altura = float(input("Ingrese la altura (en metros): "))

imc = funciones.calcular_imc(peso,altura)
print(f"SU imc es: {imc:.2f}")

#Ejercicio 9

celsius = float(input("Ingrese los grados celsius: "))
fahrenheit = funciones.celsius_a_fahrenheit(celsius)
print(f"{celsius}°C equivalen a {fahrenheit}°F")

#Ejercicio 10

a=float(input("Ingrese la primer nota: "))
b=float(input("Ingrese la segunda nota: "))
c=float(input("Ingrese la tercer nota: "))

promedio = funciones.calcular_promedio(a, b, c)

print(f"EL promedio de las notas {a}, {b}, {c} es {promedio}")