corredores = {}
def agregar_corredor():
    cant = int(input("Ingrese cuantos corredores desea ingresar: "))
    for i in range(cant):
        print(f"Corredor #{i + 1}")
        while True:
            dorsal = int(input("Ingrese el dorsal del corredor: "))
            if dorsal in corredores:
                print("Error, este dorsal ya fue asignado. Intente con otro número")
            elif dorsal < 0:
                print("Error, los dorsales deben de ser números positivos")
            else:
                break
        while True:
            nombre = input("Ingrese el nombre del corredor: ").upper()
            if not nombre:
                print("Error, campo requerido. Ingrese el nombre del corredor")
            else:
                break
        while True:
            edad = int(input("Ingrese la edad del corredor: "))
            if edad <= 0:
                print("Error, la edad no puede ser negativa ni 0")
            else:
                break
        while True:
            categoria = input("Ingrese la categoria del corredor(juvenil, adulto, máster): ")
            if not categoria:
                print("Error, campo requerido")
            else:
                break
        corredores[dorsal] = {
            "nombre": nombre,
            "edad": edad,
            "categoria": categoria
        }
def quicks_nombre(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    menores = [x for x in lista[1:] if x[1]['nombre'] < pivote[1]['nombre']]
    iguales = [x for x in lista if x[1]['nombre'] == pivote[1]['nombre']]
    mayores = [x for x in lista[1:] if x[1]['nombre'] > pivote[1]['nombre']]
    return quicks_nombre(menores) + iguales + quicks_nombre(mayores)
def quicks_edad_menores(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    menores = [x for x in lista[1:] if x[1]['edad'] < pivote[1]['edad']]
    iguales = [x for x in lista if x[1]['edad'] == pivote[1]['edad']]
    mayores = [x for x in lista[1:] if x[1]['edad'] > pivote[1]['edad']]
    return quicks_nombre(menores) + iguales + quicks_nombre(mayores)
def quicks_edad_mayores(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    menores = [x for x in lista[1:] if x[1]['edad'] < pivote[1]['edad']]
    iguales = [x for x in lista if x[1]['edad'] == pivote[1]['edad']]
    mayores = [x for x in lista[1:] if x[1]['edad'] > pivote[1]['edad']]
    return quicks_nombre(mayores) + iguales + quicks_nombre(menores)
def main():
    while True:
        print("======MENÚ======")
        print("1. Agregar corredores")
        print("2. Mostrar participantes ordenados por nombre.")
        print("3. Mostrar participantes ordenados por edad.")
        print("4. Salir.")
        opcion = input("Seleccione una opción: ")
        match opcion:
            case "1":
                agregar_corredor()
            case "2":
                hola = list(corredores.items())
                resultado = quicks_nombre(hola)
                for nombre, valor in resultado:
                    print(f"Dorsal: {nombre} | Datos: {valor}")
            case "3":
                adios = list(corredores.items())
                print("1. Menor a mayor")
                print("2. Mayor a menor")
                opciones = input("Seleccione el orden que desea ")
                if opciones == "1":
                    menores = quicks_edad_menores(adios)
                    for nombre, valor in menores:
                        print(f"Dorsal: {nombre} | Datos: {valor}")
                elif opciones == "2":
                    mayores = quicks_edad_mayores(adios)
                    for nombre, valor in mayores:
                        print(f"Dorsal: {nombre} | Datos: {valor}")
if __name__ == "__main__":
    main()