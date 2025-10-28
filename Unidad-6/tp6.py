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