mayor3=False
for x in range(5):
    adn=input(f"Ingrese la secuencia {x+1}: ")
    num=len(adn)
    if num>3:
        mayor3=True
if mayor3==True:
    print("Hay una secuencia mas larga que 3")
else:
    print("No hay una secuencia mas larga que 3")