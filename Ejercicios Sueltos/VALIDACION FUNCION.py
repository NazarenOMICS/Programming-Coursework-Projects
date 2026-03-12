def validar_secuencia(adn):
    for base in adn:
        if base not in "ATGCN":
            return False
    return True

retorno=False
while retorno==False:
    sec=input("Ingrese secuencia 1: ")
    sec=sec.upper()
    retorno=validar_secuencia(sec)

retorno=False
while retorno==False:
    sec2=input("Ingrese secuencia 2: ")
    sec2=sec2.upper()
    retorno=validar_secuencia(sec2)

print("Las secuencias son", sec,"y", sec2)