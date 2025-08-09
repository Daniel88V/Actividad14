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
            nombre = input("Ingrese el nombre del corredor: ")
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