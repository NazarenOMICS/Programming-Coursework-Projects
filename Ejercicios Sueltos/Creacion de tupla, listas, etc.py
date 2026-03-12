"""
#Creacion de tupla
tupla=(1,2,"AT",5,1,True)

#Recorrida por posicion
for pos in range (len(tupla)):
    print(tupla[pos])

print(type(tupla))

#funcion para primer y ultima
def primer_y_ultima(sec):
    posfinal=len(sec)-1
    tupla=(sec[0],sec[posfinal])
    return tupla

#Otra forma
def primer_y_ultima(sec):
    tupla=(sec[0],sec[-1])
    return tupla

assert primer_y_ultima("ATGC")==("A","C"), f"No responde correctamente"
assert primer_y_ultima("ATGCA")==("A","A"), f"No responde correctamente 2"

sec=input("Ingrese una secuencia: ").upper()
print(primer_y_ultima(sec))

"""

#Creacion de Listas
lista=[1,2,3]
print(lista)
lista.append("A")
print(lista)
del lista[1]
print(lista)
lista[1]=True
print(lista)
lista.insert(1,"posicion 1")
print(lista)

#Programa que pida un numero N, luego N secuencias y al final mueste todas las secuencias ingresadas.

def validar_secuencia(adn):
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

num=int(input("Ingrese el número de secuencias: "))
lista=[]
for x in range(1,num+1):
    sec=pedir_secuencia_valida(f"Ingrese la secuencia {x}: ").upper()
    lista.append(sec)

for adn in lista:
    print(adn)