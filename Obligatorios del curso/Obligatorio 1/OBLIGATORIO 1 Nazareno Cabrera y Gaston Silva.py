#Este es el obligatorio 1 de Nazareno Ivan Cabrera con Gastón Silva Larroca

#Funciones:
#Función para generar un menu:
def menu():
    """Menu para el tratamiento de secuencias de ADN"""
    print("1) Mostrar la secuencia")
    print("2) Calculadora de temperatura de fusion")
    print("3) Contador de ORFs (Open Reading Frames)")
    print("4) Intercalar las secuencias (Intercala la primer secuencia con el inverso de la segunda)")
    print("5) Verificador de la posibilidad de generar un primer")
    print("6) Replicador de secuencia (Replica cada base el numero de veces que se pida)")
    print("7) Muestra las parejas de la secuencia")
    print("0) Salir")
    opc=input("Ingrese opción: ")
    while not opc.isdigit():
        opc=input("Ingrese unicamente números: ")
    opc=int(opc)
    return opc
  

#Función para validar una secuencia según lo pedido:
def validar_secuencia(secuencia):
    """Validar una secuencia de ADN con las siguientes condiciones: 1) El largo es de al menos 1 carácter 2) La secuencia solo contiene “A”, “C”, “T” o “G”"""
    if len(secuencia)<1:
        return False
    for base in secuencia:
        if base not in "ATGC":
            return False
    return True

#Función para pedir una secuencia valida:
def pedir_secuencia_valida(mensaje="Ingrese una secuencia: "):
    """Pedir al usuario una secuencia y valida que se correcta"""

    sec=input(mensaje).upper()
    while not validar_secuencia(sec):
        print("Secuencia invalida")
        sec=input(mensaje).upper()
    
    return sec

#Función para generar una secuencia aleatoria:
def generar_secuencia_aleatoria(largo):
    """Retorna una secuencia aleatoria de largo determinado por el usuario"""
    import random
    secuencia_aleatoria=""
    for x in range(largo):
        num=random.randint(1,4)
        if num==1:
            secuencia_aleatoria += "A"
        elif num==2:
            secuencia_aleatoria += "T"
        elif num==3:
            secuencia_aleatoria += "G"
        elif num==4:
            secuencia_aleatoria += "C"
    return secuencia_aleatoria

#Función que pregunta si o no (Si: genera una secuencia aleatoria, No: pide una secuencia valida)
def pregunta_si_o_no():
    """Pregunta si se quiere generar una secuencia aleatoria. Si no se quiere pide una secuencia valida."""
    respuesta="no"
    while respuesta!="si":
        respuesta=input("¿Desea generar una secuencia aleatoria? (Si/No): ").lower()
        if respuesta=="si":
            largo=0
            while largo<1:
                largo=int(input("Ingrese el largo de la secuencia aleatoria: "))
                if largo<1:
                    print("El largo debe se de al menos 1")
                else:
                    secuencia=generar_secuencia_aleatoria(largo)
                    return secuencia
        elif respuesta=="no":
            secuencia=pedir_secuencia_valida()
            return secuencia
        else:
            print("Por favor, ingrese unicamente si o no")

#Función 1:
def mostrar(secuencia):
    """Retorna un string con la cantidad y el porcentaje de cada base"""
    #Cuenta cuanto hay de cada base
    CantA=secuencia.upper().count("A")
    CantT=secuencia.upper().count("T")
    CantG=secuencia.upper().count("G")
    CantC=secuencia.upper().count("C")
    #Hace el porcentaje de cada una
    Total=len(secuencia)
    PorcA=int((CantA/Total)*100)
    PorcT=int((CantT/Total)*100)
    PorcG=int((CantG/Total)*100)
    PorcC=int((CantC/Total)*100)
    #Retorna directamente el mensaje
    return f"A -> {"A"*CantA} {PorcA}% C -> {"C"*CantC} {PorcC}% T -> {"T"*CantT} {PorcT}% G -> {"G"*CantG} {PorcG}%"

#Pruebas de la función 1
assert mostrar("ATCG") == "A -> A 25% C -> C 25% T -> T 25% G -> G 25%", f"No funciona el conteo o el porcentaje"
assert mostrar("ATGCATCG") == "A -> AA 25% C -> CC 25% T -> TT 25% G -> GG 25%", f"No funciona el conteo"

#Función 2:
def temp_de_fusion(secuencia):
    """Retorna la temperatura a la que se desnaturaliza el 50% de una molécula de ADN"""
    #Cuenta cuanto hay de cada base
    CantA=secuencia.upper().count("A")
    CantT=secuencia.upper().count("T")
    CantG=secuencia.upper().count("G")
    CantC=secuencia.upper().count("C")
    #Calculo de la temperatura de fusion
    Tm=int(2*(CantA+CantT) + 4*(CantG+CantC))
    return Tm

#Pruebas de la función 2:
assert temp_de_fusion("ATGC") == 12, f"Error en la secuencia ATGC, La temperatura esperada era 12"
assert temp_de_fusion("ATGCGCGCGC") == 36, f"Error en la secuencia ATGCGCGCGC, La temperatura esperada era 36"

#Función 3:
def contar_orfs(secuencia):
  orfs=0
  for x in range(len(secuencia)):
    if secuencia[x:x+3] == "ATG":
      for i in range(x+4,len(secuencia)):
        if secuencia[i:i+3] == "TAA" or secuencia[i:i+3] == "TAG" or secuencia[i:i+3] == "TGA":
          resta= i - x
          if resta % 3 ==0:
            orfs+=1
          break
  return orfs

#Función 4
def intercalar_inverso(secuencia1, secuencia2):
    # Invertir la secuencia2
    secuencia2_invertida = secuencia2[::-1]
    
    # Determinar la longitud de cada secuencia
    len_secuencia1 = len(secuencia1)
    len_secuencia2 = len(secuencia2_invertida)
    
    # Determinar la longitud máxima
    max_len = max(len_secuencia1, len_secuencia2)
    
    # Inicializar la nueva secuencia
    nueva_secuencia = ""
    
    # Intercalar las bases de las secuencias
    for x in range(max_len):
        if x < len_secuencia1:
            nueva_secuencia += secuencia1[x]
        if x < len_secuencia2:
            nueva_secuencia += secuencia2_invertida[x]
    
    return nueva_secuencia

#Pruebas de la función 4:
assert intercalar_inverso("ATTG", "CGTA") == "AATTTGGC"
assert intercalar_inverso("GGC", "TACTC") == "GCGTCCAT"

#Función 5: 
def se_puede_primer(secuencia,pos):
    """Retorna True si se puede generar un Primer desde esa posición inclusive (o posterior) en la secuencia o False en caso contrario."""
    numero_de_primers=0
    for x in range(pos,len(secuencia)):
        primer=secuencia[x:x+5]
        if len(primer)>=5:
            gcporcentaje=(primer.count("G")+primer.count("C"))*100/5
            if gcporcentaje>=50:
                numero_de_primers=+1  
    if numero_de_primers!=0:
        return True
    else:
        return False

#Pruebas de la función 5:
assert se_puede_primer("ACTGCATGCAT",2)==True, f"Se debería poder hacer un primer"
assert se_puede_primer("ACTGCATGCAT",5)==False, f"No se debería poder hacer un primer"
assert se_puede_primer("ATATATATATATGCGC",2)==True, f"Se debería poder hacer un primer"

#Función 6:

def replicar(secuencia, cant):
    secuencia_replicada = ""
    for base in secuencia:
        secuencia_replicada += base*cant
    return secuencia_replicada

# Prueba
assert replicar("ATAGTG", 3) == "AAATTTAAAGGGTTTGGG"

#Función 7:
def parejas(secuencia):
    # Inicializar la matriz de parejas
    matriz_parejas = [[0]*4 for _ in range(4)]
    bases = "ACTG"

    # Recorrer la secuencia y contar las parejas
    for x in range(len(secuencia) - 1):
        base1 = secuencia[x]
        base2 = secuencia[x + 1]

        # Obtener los índices de las bases en la matriz
        index1 = bases.index(base1)
        index2 = bases.index(base2)

        # Incrementar el conteo de parejas en la matriz
        matriz_parejas[index1][index2] += 1

    return matriz_parejas

#A partir de aca comienza el programa:
#Pedido inicial de secuencia aleatoria
respuesta="si"
while respuesta!="no":
    respuesta=input("¿Desea generar una secuencia aleatoria? (Si/No): ").lower()
    if respuesta=="si":
        largo=0
        while largo==0:
            largo=input("Ingrese el largo de la secuencia aleatoria: ")
            if largo.isdigit():
                largo=int(largo)
                if largo>1:
                    secuencia=generar_secuencia_aleatoria(largo)
                    print("Esta es la secuencia aleatoria generada:",secuencia)
                else:
                    print("El largo debe se de al menos 1")
            else:
                print("Ingrese unicamente un número entero para el largo")
                largo=0
        break
    elif respuesta!="no":
        print("Ingrese unicamente si o no")

opcion=menu()
while opcion!=0:
    if opcion==1:
        if respuesta=="no":
            secuencia=pedir_secuencia_valida()
        
        print(mostrar(secuencia))
    elif opcion==2:
        if respuesta=="no":
            secuencia=pedir_secuencia_valida()
        
        print(temp_de_fusion(secuencia))
    elif opcion==3:
        if respuesta=="no":
            secuencia=pedir_secuencia_valida()
        
        print(contar_orfs(secuencia))
    elif opcion==4:
        if respuesta=="no":
            secuencia1=pedir_secuencia_valida("Ingrese la secuencia 1: ")
            secuencia2=pedir_secuencia_valida("Ingrese la secuencia 2: ")
        else:
            secuencia1=secuencia
            respuesta_f4="si"
            while respuesta_f4!="no":
                respuesta_f4=input("¿Desea generar otra secuencia aleatoria para intercalar? (Si/No): ").lower()
                if respuesta_f4=="si":
                    largo=0
                    while largo==0:
                        largo=input("Ingrese el largo de la secuencia aleatoria: ")
                        if largo.isdigit():
                            largo=int(largo)
                            if largo>1:
                                secuencia2=generar_secuencia_aleatoria(largo)
                                print("Esta es la secuencia generada para intercalar:",secuencia2)
                            else:
                                print("El largo debe se de al menos 1")
                        else:
                            print("Ingrese unicamente un número entero para el largo")
                            largo=0
                    break
                elif respuesta_f4=="no":
                    secuencia2=pedir_secuencia_valida()

                elif respuesta_f4!="no":
                    print("Ingrese unicamente si o no")

        print("Resultado:",intercalar_inverso(secuencia1,secuencia2))

    elif opcion==5:
        if respuesta=="no":
            secuencia=pedir_secuencia_valida()

        pos=input("ingrese la posición para buscar un primer: ")
        while not pos.isdigit():
            pos=input("Ingrese unicamente números: ")
        pos=int(pos)
        print(se_puede_primer(secuencia,pos))

    elif opcion==6:
        if respuesta=="no":
            secuencia=pedir_secuencia_valida()

        cant=input("ingrese la cantidad de veces a replicar: ")
        while not cant.isdigit():
            cant=input("Ingrese unicamente números: ")
        cant=int(cant)
        print(replicar(secuencia,cant))


    elif opcion==7:
        if respuesta=="no":
            secuencia=pedir_secuencia_valida()

        #Formato matriz
        bases="ACGT"
        print("     ", end="")
        for base in bases:
            print(f"{base:4}", end="")
        print()

        # Imprimir filas con nombres de bases y valores
        for x, fila in enumerate(parejas(secuencia)):
            print(f"{bases[x]} ", end="")
            for valor in fila:
                print(f"{valor:4}", end="")
            print()

    elif opcion==0:
        print("Salir")

    else:
        print("No existe la opción", opcion)
    opcion=menu()

