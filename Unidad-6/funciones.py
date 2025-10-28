"""1. Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal."""
def imprimir_hola_mundo():
    print("Hola mundo!")

"""2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario"""
def saludar_usuario(nombre):
    print(f"Hola {nombre}") 

"""3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”.
Pedir los datos al usuario y llamar a esta función con los valores ingresados."""
def informacion_personal(nombre, apellido,edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

"""4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva
el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva
el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados"""
def calcular_area_circulo(radio):
    pi:float= 3.1416
    area:float=pi*(radio**2)
    return area

def calcular_perimetro_circulo(radio):
    pi:float= 3.1416
    perimetro=2*pi*radio
    return perimetro

"""5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función."""
def segundos_a_horas(segundos):
    return segundos/3600

"""6. Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función."""
def tabla_multiplicar(numero):
    for i in range(1,11):
        print(numero*i)