def complemento_base(base):
    """ Complemento de cada nucleótido"""
    if base == "A":
        return "T"
    elif base == "T":
        return "A"
    elif base == "G":
        return "C"
    elif base == "C":
        return "G"
    else:
        return "N"

#Creando pruebas
assert complemento_base("A")=="T",f"La base complemento debería se T para A"
assert complemento_base("Z")=="N"

def complemento_secuencia(adn:str):
    """ Recibe una secuencia y devuelve su complemento"""
    complementaria=""
    for sec in adn:
        complementaria += complemento_base(sec)
    return complementaria
print(complemento_secuencia("ATGCZ"))

#Otra forma:

def complementario(adn):
    """Hace el complementario de una secuencia de ADN"""
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
    return complementaria

#Creando pruebas
assert complementario("A")=="T", f"la base complemento de A debería ser T"
assert complementario("Z")=="N", f"El complemento"