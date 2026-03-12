def porcentaje_GC(adn):
    """Calcula el porcentaje GC"""
    cont=len(adn)
    contn=adn.count("N")
    gcporcentaje=(adn.count("G")+adn.count("C"))/(cont-contn)
    return gcporcentaje*100

def validar_secuencia(adn):
    """Valida una secuencia de ADN"""
    for base in adn:
        if base not in "ATGCN":
            return False
    return True

def pedir_secuencia_valida(mensaje="Ingrese una secuencia: "):
    """Pedir al usuario una secuencia y valida que se correcta"""

    sec=input(mensaje).upper()
    while not validar_secuencia(sec):
        print("Secuencia invalida")
        sec=input(mensaje).upper()
    
    return sec

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
assert complemento_base("A")=="T",f"La base complemento debería ser T para A"
assert complemento_base("T")=="A",f"La base complemento debería ser A para T"
assert complemento_base("G")=="C",f"La base complemento debería ser C para G"
assert complemento_base("C")=="G",f"La base complemento debería ser G para C"
assert complemento_base("Z")=="N",f"La base complemento de cualquier letra que no sea ATGC es N"

def complemento_secuencia(adn:str):
    """ Recibe una secuencia y devuelve su complemento"""
    complementaria=""
    for sec in adn:
        complementaria += complemento_base(sec)
    return complementaria

def inverso(adn):
    """Hace el inverso de una secuencia de ADN"""
    inv=adn[::-1]
    return inv

def porcentaje_similitud(adn1,adn2):
    """Compara 2 secuencias de ADN y devuelve el porcentaje de similitud"""
    len1=len(adn1)
    len2=len(adn2)
    #Uso el más corto para la recorrida y más largo para el divisor
    if len1>len2:
        corto=len2
        largo=len1
    else:
        corto=len1
        largo=len2
    contador=0
    for pos in range(corto):
        if adn1[pos]==adn2[pos]:
            contador+=1
    porc=int((contador/largo)*100)
    return porc

#Creando pruebas
assert porcentaje_similitud("ATGCATGC","ATGC")==50, f"No funcionan las coincidencias"

def menu():
    """Menu básico para el tratamiento de secuencias de ADN"""
    print("1) Porcentaje GC")
    print("2) Complemento")
    print("3) Inverso")
    print("4) Porcentaje de coincidencias")
    print("0) Salir")
    opc=int(input("Ingrese opción: "))
    return opc

#Aca comienza nuestro programa
opcion=menu()
while opcion!=0:
    if opcion==1:
        sec=pedir_secuencia_valida()
        por=int(porcentaje_GC(sec))
        print("El porcentaje GC es",por,"%")
    elif opcion==2:
        sec=pedir_secuencia_valida()
        com=complemento_secuencia(sec)
        print("El complemento de la secuencia es",com)
    elif opcion==3:
        sec=pedir_secuencia_valida()
        inv=inverso(sec)
        print("El inverso de la secuencia es",inv)
    elif opcion==4:
        sec1=pedir_secuencia_valida()
        sec2=pedir_secuencia_valida()
        porsim=porcentaje_similitud(sec1,sec2)
        print ("El porcentaje de similitud es",porsim)
    elif opcion==0:
        print("Salir")
    else:
        print("No existe la opción", opcion)
    opcion=menu()