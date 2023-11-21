def main():
    opcion = 1
    print("Bienvenido al portal de veterinaria 'Tu mascota feliz'")
    while opcion != 5:
        print("1. Registrar paciente")
        print("2. Consultar registro")
        print("3. Modificar registro")
        print("4. Eliminar registro")
        print("5. Salir")
        opcion = int(input("Por favor, elija una de las siguientes opciones: "))
        match opcion:
            case 1:
                registro_paciente()
            case 2:
                consultar_registro()
            case 3:
                modificar_registro()
            case 4:
                eliminar_registro()
            case 5:
                pass


def registro_paciente():
    nombre = input("Nombre: ")
    sexo = input("Sexo(M/F): ")
    edad = input("Edad aproximada: ")
    especie = input("Especie (Canino/Felino): ")
    rasgos = input("Rasgos: ")
    enfermedad = input("Enfermedad: ")
    nombre_dueño = input("Nombre del dueño: ")
    numero_contacto = input("Número de contacto: ")
    pacientes.append(
        [nombre, sexo, edad, especie, rasgos, enfermedad, nombre_dueño, numero_contacto]
    )


def consultar_registro():
    INDEX = 0
    for paciente in pacientes:
        print(
            f"ID: {INDEX}. Nombre: {paciente[0]}. Sexo: {paciente[1]}. Edad: {paciente[2]}. Especie: {paciente[3]}. Rasgos: {paciente[4]}. Enfermedad: {paciente[5]}. Nombre del dueño: {paciente[6]}. Numero de contacto: {paciente[7]}"
        )
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

    pacientes.pop(ID - 1)

    print("¡Paciente eliminado!")

if __name__ == "__main__":
    pacientes = [["Felini", "Femenino", "8 meses", "Felino", "Negro con manchas blancas", "Gripe", "Erika", "11 2379-0359"], ["Julian", "Masculino", "4 meses", "Canino", "Blanco con manchas negras", "Resfriado", "Federico", "11 4022-0863"]]
    main()