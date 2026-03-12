adn=input("ingrese una secuencia: ")
adn=adn.upper()
complementaria=""
base=""
for base in adn:
    if base not in "ATGCN":
    print("Solo se pueden ingresar secuencias completas de ADN")

        if base=="A":
        complementaria +="T"
        if base=="T":
        complementaria +="A"
        if base=="G":
        complementaria +="C"
        if base=="C":
        complementaria +="G"
        
print(adn)
print(complementaria[::-1])