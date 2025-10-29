"""1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300"""

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)

"""2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800"""

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print(precios_frutas)

"""3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
precios."""

lista_de_claves = list(precios_frutas.keys())
print(lista_de_claves)

"""4) Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe."""

dic_numeros_cel={}
for i in range(5):
    nuevaClave=input("Ingrese el nombre del contacto: ")
    nuevoValor=input(f"Ingrese el numero de celular de {nuevaClave}: ")
    dic_numeros_cel[nuevaClave]= nuevoValor
print(dic_numeros_cel)

nombre=input("Ingrese el nombre del que desea saber el numero")
if nombre in dic_numeros_cel.keys():
    print(f"El numero de {nombre} es: {dic_numeros_cel.get(nombre)}")
else:
    print("El nombre no esta agendado")

"""5) Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra"""

frase:str = input("Ingrese una frese")
frase = frase.lower()
lista_frase = frase.split()
set_frase = set(lista_frase)

dicc_frecuencias = {}

for palabra in lista_frase:
    dicc_frecuencias[palabra] = dicc_frecuencias.get(palabra, 0) + 1

print("\nPalabras únicas:")
print(set_frase)
print("\nFrecuencia de palabras:")
print(dicc_frecuencias)

"""6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno"""

def pedir_notas(nombre):
    notas = []
    for i in range(3):
        nota = float(input(f"Ingrese la nota {i+1} de {nombre}: "))
        notas.append(nota)
    return tuple(notas)

alumno1:str=input("Ingrese el nombre del alumno: ")
alumno2:str=input("Ingrese el nombre del alumno: ")
alumno3:str=input("Ingrese el nombre del alumno: ")

tupla_alumno1 = pedir_notas(alumno1)
tupla_alumno2 = pedir_notas(alumno2)
tupla_alumno3 = pedir_notas(alumno3)

promedio1 = sum(tupla_alumno1) / 3
promedio2 = sum(tupla_alumno2) / 3
promedio3 = sum(tupla_alumno3) / 3

print(f"\nPromedio de {alumno1}: {promedio1:.2f}")
print(f"Promedio de {alumno2}: {promedio2:.2f}")
print(f"Promedio de {alumno3}: {promedio3:.2f}")