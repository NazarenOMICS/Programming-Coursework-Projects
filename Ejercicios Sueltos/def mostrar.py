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
    return f"A -> {"A"*CantA} {PorcA}% C -> {"C"*CantC} {PorcC}% G -> {"G"*CantG} {PorcG}% T -> {"T"*CantT} {PorcT}%"

sec="TAAACAACCT"
print(mostrar(sec))
