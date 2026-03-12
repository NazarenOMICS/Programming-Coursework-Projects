adn = input("Ingrese una secuencia: ")
adn = adn.upper()
complementaria = ""

if all(base in "ATCG" for base in adn):
    for base in adn:
        if base == "A":
            complementaria += "T"
        elif base == "T":
            complementaria += "A"
        elif base == "G":
            complementaria += "C"
        elif base == "C":
            complementaria += "G"
    print(adn)
    print(complementaria)
else:
    print("Solo se pueden ingresar secuencias de ADN")