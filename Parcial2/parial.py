#importamos librerias

import csv
import os

#definimos una constante para el nombre de archivo
NOMBRE_ARCHIVO = "productos.csv"


def obtenerProductos():
    productos=[]
    if not os.path.exists(NOMBRE_ARCHIVO):
        with open(NOMBRE_ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["nombre", "precio"])
            escritor.writeheader()
            return productos
        
    
    with open(NOMBRE_ARCHIVO, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            productos.append({"nombre": fila["nombre"], "precio":float(fila["precio"])})
    return productos

def agregar_producto(producto):
    with open(NOMBRE_ARCHIVO,"a",newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["nombre", "precio"])
        escritor.writerow(producto)


def existeProducto(nombre):
    productos = obtenerProductos()
    for producto in productos:
        if producto["nombre"].lower() == nombre.strip().lower():
            return True
    return False

def validarNumero(precio):
    if precio.count(".") > 1:
        return False
    if not precio.replace(".","").isdigit():
        return False
    return True

def mostrarProductos():
    print("--- Listado de productos ---")
    productos=obtenerProductos()
    print("Nombre          Precio")
    for producto in productos:
        print(f"{producto["nombre"]} - ${producto["precio"]}")



def agregarProducto():
    print("Agregar nuevo producto")

    nombre=input("Ingrese nombre del producto: ").strip()
    if existeProducto(nombre):
        print("El producto ya existe")
        return
    
    precio=input("Ingrese el precio: ").strip()
    if not validarNumero(precio):
        print("El precio no es valido")
        return
    precio =float(precio)
    agregar_producto({"nombre": nombre, "precio": precio})
    print("Producto agregado con exito!")

def guardarProductos(productos):
    with open(NOMBRE_ARCHIVO,"w",newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["nombre", "precio"])
        escritor.writeheader()
        escritor.writerows(productos)

def editarProducto():
    
    nombre = input("Ingrese nombre del producto que desa editar: ").strip()
    if not nombre:
        print("El nombre no puede estar vacio")
        return

    productos=obtenerProductos()

    for producto in productos:
        if producto["nombre"].lower() == nombre.lower():
            precio = input("Ingrese nuevo precio: ").strip()
            if not validarNumero(precio):
                print("El precio no es valido")
                return
        producto["precio"] = float(precio)
        guardarProductos(productos)
        print("EL producto fue modificado")
        break
    else:
        print("No se encuentra el archivo en el producto")

def eliminarProducto():
    nombre = input("Ingrese el nombre del producto que desea eliminar: ").strip()
    if not nombre:
        print("El nombre no puede estar vacio")
        return
    productos=obtenerProductos()
    productosFiltrados=[]
    for producto in productos:
        if producto["nombre"].lower() != nombre.lower():
            productosFiltrados.append(producto)
    if len(productosFiltrados) == len(productos):
        print("El producto no se encuentra en el archivo")
        return
    guardarProductos(productosFiltrados)
    print("El producto fue eliminado con exito")
def menu():
    """Funcion para mostrar el menu"""
    while True:

        print("====== MENÚ DE PRODUCTOS ======\n"
        "1. Mostrar productos\n"
        "2. Agregar producto\n"
        "3. Editar precio de producto\n"
        "4. Eliminar producto\n"
        "5. Salir\n"
        "===============================")
        opcion=input("Ingrese una opcion: ").strip()
        match opcion:
            case "1":
                mostrarProductos()
            case "2":
                agregarProducto()
            case "3":
                print("Editar precio de producto")
                editarProducto()
            case "4":
                print("Eliminar producto")
                eliminarProducto()
            case "5":
                print("Gracias por usar el programa :)")
                break
            case _:
                print("La opcion seleccionada no es valida")
#--------#
menu()