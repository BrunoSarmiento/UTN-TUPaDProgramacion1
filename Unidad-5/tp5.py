#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
#range.

print("Ejercicio 1")

lista:list=[lista for lista in range(1, 101) if lista % 4 == 0]
print(lista)
print("----------")

#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
#penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
#indexing con números negativos!

print("Ejercico 2")

lista:list = ["Bruno","Santiago","Sarmiento","43117987","23/02/2000"]
print(lista[-2])

print("----------")

#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
#pantalla

print("Ejercico 3")

lista:list=[]
for i in range(3):
    lista.append(input("Agregue una palabra a la lista: "))
print(lista)

print("----------")

#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
#respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
#en los videos o bien investigar cómo funciona el indexing con números negativos!

print("Ejercicio 4")

animales = ["perro", "gato", "conejo", "pez"]
animales[1]="loro"
animales[-1]="oso"
print(animales)

print("----------")

#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

print("Ejercicio 5")

numeros=[8,15,3,22,7] #Crea una variable lista llamada numeros con 5 valores asignados
numeros.remove(max(numeros)) #Utiliza dos funciones, move y max, max() para encontrar el valor maximo y remove() para eliminar dicho valor
print(numeros)#Imprime la lista modificada

print("----------")

#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
#pantalla los dos primeros.

print("Ejercicio 6")

lista:list=list(range(10,31,5))
print(f"1°: {lista[0]}, 2°: {lista[1]}")

print("----------")

#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
#cualesquiera.

print("Ejercicio 7")

autos = ["sedan", "polo", "suran", "gol"]
autos[1]="audi"
autos[2]="toyota"

print("----------")

#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
#directamente. Imprimir la lista resultante por pantalla.

print("Ejercicio 8")

dobles:list=[]
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)

print("----------")

#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
#diferentes clientes:
#compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
#a) Agregar "jugo" a la lista del tercer cliente usando append.
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
#c) Eliminar "pan" de la lista del primer cliente.
#d) Imprimir la lista resultante por pantalla

print("Ejercicio 9")

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
compras[2].append("jugo")
compras[1][1]="tallarines"
compras[0].remove('pan')
print(compras)

print("----------")

#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
#● Posición lista_anidada[0]: 15
#● Posición lista_anidada[1]: True
#● Posición lista_anidada[2][0]: 25.5
#● Posición lista_anidada[2][1]: 57.9
#● Posición lista_anidada[2][2]: 30.6
#● Posición lista_anidada[3]: False
#Imprimir la lista resultante por pantalla.

print("Ejercicio 10")

lista_anidada=[[15],[True],[25.5,57.9,30.6],[False]]
print(lista_anidada)

print("----------")
