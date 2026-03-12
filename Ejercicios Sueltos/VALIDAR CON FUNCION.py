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

secuencia=pedir_secuencia_valida()
secuencia1=pedir_secuencia_valida("Ingrese secuencia 1:")