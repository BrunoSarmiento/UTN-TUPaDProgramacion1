import csv

"""1. Crear archivo inicial con productos: Crear un archivo de texto llamado
productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad"""
print("Escribiendo y pisando registros de archivo...")
with open("productos.txt", "w", newline="") as archivo_productos:
    archivo_productos.write("nombre,precio,cantidad\n")
    archivo_productos.write("Cartuchera,750.0,10\n")
    archivo_productos.write("Regla,100.0,25\n")
    archivo_productos.write("Portamina,300.0,15\n")

"""Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
formato:
Producto: Lapicera | Precio: $120.5 | Cantidad: 30"""
print("\nProductos en el archivo:")
with open("productos.txt", "r") as archivo:
    encabezado = archivo.readline().strip()
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

"""3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
cantidad) y lo agregue al archivo sin borrar el contenido existente."""
while True:
    nombre = input("\nIngrese el nombre del nuevo producto (ENTER para salir): ").strip()
    if nombre == "":
        break

    precio = input("Ingrese el precio del nuevo producto: ").strip()
    cantidad = input("Ingrese la cantidad del nuevo producto: ").strip()

    with open("productos.txt", "a", newline="") as archivo:
        archivo.write(f"{nombre},{precio},{cantidad}\n")

    print(f" Producto '{nombre}' agregado exitosamente.")

"""4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
una lista llamada productos, donde cada elemento sea un diccionario con claves:
nombre, precio, cantidad."""
productos = []

with open("productos.txt", "r", newline="") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        fila["precio"] = float(fila["precio"])
        fila["cantidad"] = int(fila["cantidad"])
        productos.append(fila)

print("\nLista de productos cargada:")
print(productos)

"""5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
no existe, mostrar un mensaje de error"""
nombre_producto = input("\nIngrese el nombre del producto que desea buscar: ").strip().lower()

encontrado = False
for producto in productos:
    if producto["nombre"].lower() == nombre_producto:
        print(f"\nProducto encontrado:")
        print(f"Nombre: {producto['nombre']}")
        print(f"Precio: ${producto['precio']}")
        print(f"Cantidad: {producto['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("El producto no se encuentra en la lista.")

"""6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
productos actualizados desde la lista."""
with open("productos.txt", "w", newline="") as archivo:
    campos = ["nombre", "precio", "cantidad"]
    escritor = csv.DictWriter(archivo, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(productos)

print("\nArchivo actualizado correctamente.")