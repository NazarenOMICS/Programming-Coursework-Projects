def gc_calc(adn):
    """ Calcula el porcentaje GC"""
    cont=len(adn)
    contn=adn.count("N")
    gcporcentaje=(adn.count("G")+adn.count("C"))/(cont-contn)
    return gcporcentaje*100

def validar_secuencia(adn):
    for base in adn:
        if base not in "ATGCN":
            return False
    return True

def reverso_complementario(adn):
    complementaria=""
    for base in adn:
        if base == "A":
            complementaria += "T"
        elif base == "T":
            complementaria += "A"
        elif base == "G":
            complementaria += "C"
        elif base == "C":
            complementaria += "G"
    return complementaria[::-1]

retornoV=False
while retornoV==False:
    adn=input("Ingrese una secuencia: ")
    adn=adn.upper()
    retornoV=validar_secuencia(adn)
    if retornoV==False:
        print("La secuencia es incorrecta")

rc=reverso_complementario(adn)

porcentaje=int(gc_calc(adn))

print("El porcentaje gc es: ", porcentaje,"%",)
print("El reverso complementario es: ", rc) 