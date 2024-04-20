def tipo_acl_ipv4(numero_acl):
    if numero_acl >= 1 and numero_acl <= 99:
        return "ACL Layer 2 Estándar"
    elif numero_acl >= 100 and numero_acl <= 199:
        return "ACL Layer 3 Estándar"
    elif numero_acl >= 1300 and numero_acl <= 1999:
        return "ACL Layer 3 Extendida"
    elif numero_acl >= 2000 and numero_acl <= 2699:
        return "ACL Layer 2 Extendida"
    else:
        return "El número no corresponde a una lista de control de acceso."

def main():
    try:
        numero_acl = int(input("Ingrese el número de ACL IPv4: "))
        tipo = tipo_acl_ipv4(numero_acl)
        print("El tipo de ACL IPv4 para el número", numero_acl, "es:", tipo)
    except ValueError:
        print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()
