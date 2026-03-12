cont=0
for x in range(5):
    adn=input(f"Ingrese la secuencia {x+1}: ")
    adn=adn.upper()
    num=len(adn)
    if num>3 and num<6 and (adn.startswith("A") or adn.startswith("T")):
        cont += 1
if cont>0:
    print(f"Hay {cont} secuencias que cumplen con lo pedido")
else:
    print("No hay secuencias que cumplan con lo pedido")