def generar_secuencia_aleatoria():
    import random
    secuencia_aleatoria=""
    for x in range(10):
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


print(generar_secuencia_aleatoria())