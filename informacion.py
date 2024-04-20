def validar_seccion(codigo_seccion):
    seccion_correcta = "DRY7122-003V"
    return codigo_seccion == seccion_correcta

def obtener_informacion():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    codigo_seccion = input("Ingrese su código de sección: ")
    sede = input("Ingrese su sede: ")
    return nombre, apellido, codigo_seccion, sede

def main():
    nombre, apellido, codigo_seccion, sede = obtener_informacion()
    
    if validar_seccion(codigo_seccion):
        print("\nInformación del alumno:")
        print("Nombre:", nombre)
        print("Apellido:", apellido)
        print("Código de sección:", codigo_seccion)
        print("Sede:", sede)
    else:
        print("Lo siento, no perteneces a la sección especificada (DRY7122-003V).")

if __name__ == "__main__":
    main()
