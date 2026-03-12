Cant=int(input("Ingrese cuantos números va a comparar: "))
MayNum=int(input("Ingrese el número 1: "))
for x in range (2,Cant+1):
    num=int(input(f"ingrese el número {x}: "))
    if num>MayNum:
        MayNum=num

print("el mayor número es: ",MayNum)