"""1. Crear archivo inicial con productos: Crear un archivo de texto llamado
productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad"""

print("Escribiendo y pisando registros de archivo")
archivo_productos = open("productos.txt", "w")
archivo_productos.write("nombre,precio,cantidad\n")
archivo_productos.write("Cartuchera,750.0,10\n")
archivo_productos.write("Regla,100.0,25\n")
archivo_productos.write("Portamina,300.0,15\n")
archivo_productos.close()

"""2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
formato:
Producto: Lapicera | Precio: $120.5 | Cantidad: 30"""

print("Leyendo archivo")
with open("productos.txt", "r") as archivo:
    encabezado = archivo.readline().strip()
    print("Encabezado:", encabezado)

    linea1 = archivo.readline().strip().split(",")
    print("Primera línea:")
    print(f"Producto: {linea1[0]} | Precio: {linea1[1]} | Cantidad: {linea1[2]}")

    linea2 = archivo.readline().strip().split(",")
    print("Segunda línea:")
    print(f"Producto: {linea2[0]} | Precio: {linea2[1]} | Cantidad: {linea2[2]}")
    
    linea3 = archivo.readline().strip().split(",")
    print("Segunda línea:")
    print(f"Producto: {linea3[0]} | Precio: {linea3[1]} | Cantidad: {linea3[2]}")

"""3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
cantidad) y lo agregue al archivo sin borrar el contenido existente"""
nombre = input("Ingrese el nombre del nuevo producto: ")
precio = input("Ingrese el precio del nuevo producto: ")
cantidad = input("Ingrese la cantidad del nuevo producto: ")

producto_completo = f"{nombre}, {precio}, {cantidad}"
with open("productos.txt", "a") as archivo:
    archivo.write(f"{producto_completo}\n")

print(f"El producto '{nombre}' ha sido agregado exitosamente.")
