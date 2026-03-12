#Funciones
def porcentaje_GC(adn):
    """Calcula el porcentaje GC"""
    cont=len(adn)
    contn=adn.count("N")
    gcporcentaje=(adn.count("G")+adn.count("C"))/(cont-contn)
    return gcporcentaje*100
"""
#Filtrado de listas
filtro=[]
lista=["ATGCC","AAAA","TTTT","CCCCC"]
for sec in lista:
    if porcentaje_GC(sec)>50:
        filtro.append(sec)
print(lista)
print(filtro)
"""
#Filtrado por función
def filtrar_secuencia(lista,condicion):
    filtro=[]
    for sec in lista:
        if condicion(sec):
            filtro.append(sec)
    return filtro

def largo_mayor_a_3(sec):
    return len(sec)>3

def porcentaje_GC_mayor_a_50(sec):
    return porcentaje_GC(sec)>50

lista=["ATGCGCGC","AA","TTTT","CCCCC"]
print(filtrar_secuencia(lista,largo_mayor_a_3))
print (filtrar_secuencia(lista,porcentaje_GC_mayor_a_50))

#Filtrado con funciones lambda
lista=["ATGCGCGC","AA","TTTT","CCCCC"]
print(list(filter(lambda s: porcentaje_GC(s)>50, lista)))