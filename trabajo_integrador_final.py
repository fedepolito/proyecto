def main():
    """
    Interfaz principal del programa.
    """
    try:
        print("Bienvenido al portal de veterinaria 'Tu mascota feliz'")
        print()
        while True:
            print("1. Registrar paciente")
            print("2. Consultar registro")
            print("3. Modificar registro")
            print("4. Eliminar registro")
            print("5. Salir")
            print()
            opcion = int(input("Por favor, elija una de las siguientes opciones: "))
            match opcion:
                case 1:
                    agregar_registro()
                case 2:
                    mostrar_registro()
                case 3:
                    modificar_registro()
                case 4:
                    eliminar_registro()
                case 5:
                    break
                case _:
                    print()
                    print("Elija una opción válida(Entre el 1 y el 5)")
    except ValueError:
        print()
        print("Por favor ingrese un número")
        main()


def agregar_registro():
    try:
        nombre = input("Nombre: ")
        while True:
            sexos = "M", "F", "Masculino", "Femenino"
            sexo = input("Sexo (M/F/Masculino/Femenino): ").capitalize()
            if sexo in sexos: break
            else: print("Elija una opción entre M, F, Masculino o Femenino")
            
        edad = int(input("Edad aproximada en años(Ej: 6, 12, etc): "))
        while True:
            especies = "Canino", "Felino"
            especie = input("Especie (Canino/Felino): ").capitalize()
            if especie in especies: break
            else: print ("Elija entre Canino o Felino")
        rasgos = input("Rasgos: ")
        enfermedad = input("Enfermedad: ")
        nombre_dueño = input("Nombre del dueño: ")
        numero_contacto = input("Número de contacto: ")
        pacientes.append([nombre, sexo, edad, especie, rasgos, enfermedad, nombre_dueño, numero_contacto])
        archivo = open("registrados.txt", "a")
        archivo.write(f"{nombre}|{sexo}|{edad}|{especie}|{rasgos}|{enfermedad}|{nombre_dueño}|{numero_contacto}\n")

    except ValueError as err:
       print("Escriba un número.", err)
       agregar_registro()

def mostrar_registro():
    INDEX = 0
    for paciente in pacientes:
        print("ID           : {0:<15} Nombre    : {1:<15} Sexo      : {2:<15}".format(INDEX + 1, paciente[0], paciente[1]))  
        print("Edad         : {0:<15} Especie   : {1:<15} Rasgos    : {2:<15}".format(paciente[2], paciente[3], paciente[4])) 
        print("Enfermedad   : {0:<15} Dueño     : {1:<15} Teléfono  : {2:<15}".format(paciente[5], paciente[6], paciente[7]))
        print()
        INDEX += 1

def modificar_registro():
    contador = 1
    for paciente in pacientes:
        print(contador, paciente[0])
        contador += 1
    INDEX = int(input("Ingrese el ID del paciente: "))
    INDEX -= 1
    print(f"ID: {pacientes[INDEX]}")
    print(f"1. Nombre: {pacientes[INDEX][0]}")
    print(f"2. Sexo: {pacientes[INDEX][1]}")
    print(f"3. Edad: {pacientes[INDEX][2]}")
    print(f"4. Especie: {pacientes[INDEX][3]}")
    print(f"5. Rasgos: {pacientes[INDEX][4]}")
    print(f"6. Enfermedad: {pacientes[INDEX][5]}")
    print(f"7. Nombre del dueño: {pacientes[INDEX][6]}")
    print(f"8. Número de contacto: {pacientes[INDEX][7]}")
    ID = int(input("Ingrese el dato que desea modificar: "))
    ID -= 1
    pacientes[INDEX][ID] = input("Ingrese nuevo valor: ")
    print(f"Su nuevo valor es {pacientes[INDEX][ID]}.")

def eliminar_registro():
    for i in range(len(pacientes)):
        print(f"{i + 1}. {pacientes[i][0].capitalize()}")
    ID = int(input("Elije el ID del paciente: "))
    # archivo = open("eliminados.txt", "a")
    # archivo.write()
    pacientes.pop(ID - 1)
    print("¡Paciente eliminado!")

def pacientes_registrados():
    try: 
        archivo = open('registrados.txt', 'r')
        registrados = archivo.readlines()
        if registrados:
            print("Pacientes registrados:")
            for registrado in registrados:
                print(registrado.strip())
        else:
            print("La lista de nombres está vacía.")        
    except FileNotFoundError:
        archivo = open('registrados.txt', 'x')
        print("Archivo no encontrado, se ha creado uno nuevo.")

def pacientes_eliminados():
    try: 
        archivo = open('eliminados.txt', 'r')
        eliminados = archivo.readlines()
        if eliminados:
            print("Pacientes eliminados:")
            for registrado in eliminados:
                print(registrado.strip())
        else:
            print("La lista de nombres está vacía.")        
    except FileNotFoundError:
        archivo = open('eliminados.txt', 'x')
        print("Archivo no encontrado, se ha creado uno nuevo.")

def cargar_pacientes():
    archivo = open("registrados.txt", "r")
    

if __name__ == "__main__":
    pacientes = [["Felini", "Femenino", "8 meses", "Felino", "Negro con manchas blancas", "Gripe", "Erika", "11 2379-0359"], ["Julian", "Masculino", "4 meses", "Canino", "Blanco con manchas negras", "Resfriado", "Federico", "11 4022-0863"]]
    registrados = 0
    eliminados = 0
    main()
    pacientes_registrados()
