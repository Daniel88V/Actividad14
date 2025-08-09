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

