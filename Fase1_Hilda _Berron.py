import os
from datetime import datetime

# Diccionario para almacenar clientes
clientes = {}

# Función para cargar datos de clientes desde archivos
def cargar_clientes():
    for archivo in os.listdir():
        if archivo.endswith(".txt"):
            with open(archivo, "r") as file:
                nombre = archivo.replace(".txt", "")
                direccion = file.readline().split(": ")[1].strip()
                telefono = file.readline().split(": ")[1].strip()
                correo = file.readline().split(": ")[1].strip()
                fecha_creacion = file.readline().split(": ")[1].strip()
                file.readline()  # Leer la línea "Descripciones:"
                descripciones = [linea.strip().replace("- ", "") for linea in file]
                clientes[nombre] = {
                    'direccion': direccion,
                    'telefono': telefono,
                    'correo': correo,
                    'fecha_creacion': fecha_creacion,
                    'descripciones': descripciones
                }

# Función para agregar un cliente nuevo
def agregar_cliente(nombre, descripcion, direccion, telefono, correo):
    if nombre in clientes:
        print("El cliente ya existe. Actualizando descripción...")
        clientes[nombre]['descripciones'].append(descripcion)
    else:
        print("Creando un nuevo cliente...")
        clientes[nombre] = {
            'descripciones': [descripcion],
            'direccion': direccion,
            'telefono': telefono,
            'correo': correo,
            'fecha_creacion': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    guardar_cliente(nombre)

# Función para guardar cliente en un archivo
def guardar_cliente(nombre):
    with open(f"{nombre}.txt", "w") as file:
        file.write(f"Nombre: {nombre}\n")
        file.write(f"Dirección: {clientes[nombre]['direccion']}\n")
        file.write(f"Teléfono: {clientes[nombre]['telefono']}\n")
        file.write(f"Correo: {clientes[nombre]['correo']}\n")
        file.write(f"Fecha de Creación: {clientes[nombre]['fecha_creacion']}\n")
        file.write("Descripciones:\n")
        for descripcion in clientes[nombre]['descripciones']:
            file.write(f"- {descripcion}\n")
    print(f"Información guardada en {nombre}.txt")

# Función para leer la información de un cliente
def leer_cliente(nombre):
    if nombre in clientes:
        print(f"Información del cliente {nombre}:")
        print(f"Dirección: {clientes[nombre]['direccion']}")
        print(f"Teléfono: {clientes[nombre]['telefono']}")
        print(f"Correo: {clientes[nombre]['correo']}")
        print(f"Fecha de Creación: {clientes[nombre]['fecha_creacion']}")
        print("Descripciones:")
        for descripcion in clientes[nombre]['descripciones']:
            print(f"- {descripcion}")
    else:
        print("Cliente no encontrado.")

# Función para eliminar un cliente
def eliminar_cliente(nombre):
    if nombre in clientes:
        os.remove(f"{nombre}.txt")
        del clientes[nombre]
        print(f"Cliente {nombre} eliminado.")
    else:
        print("Cliente no encontrado.")

# Función para ver la lista de clientes
def ver_lista_clientes():
    if clientes:
        print("Lista de clientes:")
        for cliente in clientes:
            print(f"- {cliente}")
    else:
        print("No hay clientes registrados.")

# Menú principal
def menu():
    cargar_clientes()
    while True:
        print("\nMenú:")
        print("1. Ver lista de clientes")
        print("2. Ver cliente")
        print("3. Crear cliente nuevo")
        print("4. Agregar servicio a cliente existente")
        print("5. Eliminar cliente")
        print("6. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ver_lista_clientes()
        elif opcion == "2":
            nombre = input("Introduce el nombre del cliente: ")
            leer_cliente(nombre)
        elif opcion == "3":
            nombre = input("Introduce el nombre del cliente nuevo: ")
            direccion = input("Introduce la dirección del cliente: ")
            telefono = input("Introduce el teléfono del cliente: ")
            correo = input("Introduce el correo electrónico del cliente: ")
            descripcion = input("Introduce la descripción del servicio: ")
            agregar_cliente(nombre, descripcion, direccion, telefono, correo)
        elif opcion == "4":
            nombre = input("Introduce el nombre del cliente existente: ")
            descripcion = input("Introduce la descripción del nuevo servicio: ")
            if nombre in clientes:
                clientes[nombre]['descripciones'].append(descripcion)
                guardar_cliente(nombre)
            else:
                print("Cliente no encontrado.")
        elif opcion == "5":
            nombre = input("Introduce el nombre del cliente a eliminar: ")
            eliminar_cliente(nombre)
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Ejecución del programa
menu()
