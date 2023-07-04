'''1 - Pedir numeros al usuario y cada valor se debe agregar a una lista, se termina de guardar
los numeros cuando se ingrese 0, el cero no se guarda, una vez que se haya dejado de pedir
mostrar la lista ordenada de menor a mayor, sumar todos los numeros, mostrar la suma total
y el promedio.'''
# 1) Pedir números al usuario y agregarlos a una lista
numeros = []
while True:
    numero = int(input("Ingrese un número (ingrese 0 para terminar): "))
    if numero == 0:
        break  # Se termina el ciclo si se ingresa 0
    numeros.append(numero)

# Ordenar la lista de menor a mayor
numeros.sort()

# Mostrar la lista ordenada
print("Lista ordenada de menor a mayor:", numeros)

# Calcular la suma de todos los números
suma_total = sum(numeros)

# Calcular el promedio
promedio = suma_total / len(numeros)

# Mostrar la suma total y el promedio
print("Suma total de los números:", suma_total)
print("Promedio de los números:", promedio)
'''2 - Hacer un menu donde se puedan agregar nombres de personas, se pueda eliminar un
nombre, modificar un nombre, eliminar la lista completa o mostrar todos los nombres, en
caso de que no haya nombres en la lista mostrar un mensaje que diga " No hay nombres en
la lista"'''
# Creamos una lista vacía para almacenar los nombres
nombres = []

# Función para validar si la lista de nombres está vacía
def lista_vacia():
    if len(nombres) == 0:
        print("No hay nombres en la lista.")

# Función para agregar un nombre a la lista
def agregar_nombre():
    nombre = input("Ingrese un nombre: ")
    nombres.append(nombre)
    print("Nombre agregado con éxito.")

# Función para eliminar un nombre de la lista
def eliminar_nombre():
    lista_vacia()
    if nombres:
        nombre = input("Ingrese el nombre a eliminar: ")
        if nombre in nombres:
            nombres.remove(nombre)
            print("Nombre eliminado con éxito.")
        else:
            print("El nombre no existe en la lista.")

# Función para modificar un nombre de la lista
def modificar_nombre():
    lista_vacia()
    if nombres:
        nombre_actual = input("Ingrese el nombre a modificar: ")
        if nombre_actual in nombres:
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            indice = nombres.index(nombre_actual)
            nombres[indice] = nuevo_nombre
            print("Nombre modificado con éxito.")
        else:
            print("El nombre no existe en la lista.")

# Función para eliminar la lista completa de nombres
def eliminar_lista():
    nombres.clear()
    print("Lista de nombres eliminada.")

# Función para mostrar todos los nombres en la lista
def mostrar_nombres():
    lista_vacia()
    if nombres:
        print("Nombres en la lista:")
        for nombre in nombres:
            print(nombre)

# Ejecutamos el programa principal
while True:
    # Mostramos el menú
    print("---- Menú ----")
    print("1. Agregar nombre")
    print("2. Eliminar nombre")
    print("3. Modificar nombre")
    print("4. Eliminar lista completa")
    print("5. Mostrar todos los nombres")
    print("6. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        agregar_nombre()
    elif opcion == "2":
        eliminar_nombre()
    elif opcion == "3":
        modificar_nombre()
    elif opcion == "4":
        eliminar_lista()
    elif opcion == "5":
        mostrar_nombres()
    elif opcion == "6":
        print("Hasta luego.")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")
