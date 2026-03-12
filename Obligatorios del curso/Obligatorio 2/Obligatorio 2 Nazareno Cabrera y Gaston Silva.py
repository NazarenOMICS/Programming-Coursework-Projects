#Este es el obligatorio 2 de Nazareno Ivan Cabrera con Gastón Silva Larroca
#Imports
import os

#Clases
#Creación de la clase científico:
class Cientifico:

    def __init__(self, nombre, grado):
        self.nombre = nombre
        self.grado = grado
        self.lista_secuencias = []

    def __str__(self):
        if len(self.lista_secuencias) == 0:
            ultima_secuencia = "Sin secuencias"
            cantidad_secuencias = 0
        else:
            ultima_secuencia = self.lista_secuencias[-1]
            cantidad_secuencias = len(self.lista_secuencias)
        return f"{self.nombre} ({self.grado}) - {ultima_secuencia} - {cantidad_secuencias}"

    def agregar_secuencia(self, secuencia):
        self.lista_secuencias.append(secuencia)

    def mostrar_ultima_secuencia(self):
        if len(self.lista_secuencias) == 0:
            ultima_secuencia_m = ""
        else:
            ultima_secuencia_m = self.lista_secuencias[-1]
        return ultima_secuencia_m

    def mostrar_lista_secuencias(self):
        return self.lista_secuencias

#Funciones:
#Función para validar una secuencia según lo pedido:
def validar_secuencia(secuencia):
    """Validar una secuencia de ADN con las siguientes condiciones: 1) El largo es de al menos 1 carácter 2) La secuencia solo contiene “A”, “C”, “T” o “G”"""
    if len(secuencia) % 3 == 0: #Verifica que la secuencia sea múltiplo de 3
        if len(secuencia) < 1:
            return False
        for base in secuencia:
            if base not in "ATGC": #Verifica las bases
                return False
        return True
    else:
        return False

#Función para pedir una secuencia valida:
def pedir_secuencia_valida(mensaje="Ingrese una secuencia: "):
    """Pedir al usuario una secuencia y valida que se correcta"""
    sec = input(mensaje).upper()
    while not validar_secuencia(sec):
        print("Secuencia invalida, verifique que las bases son correctas y el largo de la secuencia es múltiplo de 3")
        sec = input(mensaje).upper()
    return sec

#Función mostrar científicos:
def mostrar_cientificos(lista_cientificos):
    """Muestra todos los científicos en la lista"""
    if len(lista_cientificos) == 0:
        print("no hay cientificos registrados")
    else:
        lista_cientificos.sort(key=lambda c: c.nombre) #Ordena los cientificos en orden alfabético
        for cientifico in lista_cientificos:
            print(cientifico)
    return

#Función para cargar códigos genéticos desde archivos:
def cargar_codigos(ruta):
    """Carga los códigos genéticos de un archivo en un diccionario llamado codigos_geneticos"""
    with open(ruta, "r") as archivo:
        for linea in archivo:
            codigo = linea.replace("\n", "").split(" ") #Separa por espacio
            for elemento in codigo:
                codigo_y_proteina = elemento.split("#") #Genera una lista con el codon y la base
                codigos_geneticos[codigo_y_proteina[0]] = codigo_y_proteina[1] #Genera un diccionario con la el con y la base para cada codon en el archivo
    return codigos_geneticos

#Funcion para cargar los codones:
def codones_validos(secuencia):
    """Verifica que los codones estén en el codigo genético"""
    dic = cargar_codigos(ruta) #Carga los codones
    for base in range(0, len(secuencia), 3):
        codon = secuencia[base:base + 3]
        if codon not in dic: #Verifica que los codones estan en el diccionario
            return False
    return True

#Función del menu:
def menu():
    """Función del menu"""
    lista_opc = ["Agregar un científico", "Mostrar científicos", "Agregar secuencia a científico", "Traducir secuencia", "Científico con secuencia más larga", "Exportar científicos", "Salir"]
    lista_letra = ["a", "b", "c", "d", "e", "f", "g"]
    #Mostrar las opciones
    for pos in range(len(lista_opc)):
        print(f"{lista_letra[pos]}-{lista_opc[pos]}")
    pedir = True
    while pedir:
        try:
            opcion_letra = input("Ingrese una opción: ").lower()
            opcion = lista_letra.index(opcion_letra) #Transforma la letra en numero
            if opcion < 0 or opcion >= len(lista_opc): #Valida que la letra este en las opciones
                print("Opción incorrecta")
            else:
                pedir = False
        except:
            print("La opcion ingresada es incorrecta")

    return opcion


#Aca empieza el programa
#lector de archivos
codigos_geneticos = {}
ruta = input("Ingrese una ruta valida: ")
pedir = True
while pedir:
    try:
        cargar_codigos(ruta)
        print("El codigo genético se ha cargado exitosamente")
        pedir = False
    except:
        print("El nombre del archivo es incorrecto o el mismo no existe") #Salta si hay un error al elegir la ruta
        ruta = input("Ingrese una ruta valida: ")

#Código del menu y sus opciones:
#Creación de la lista de cientificos:
lista_cientificos = []
#Menu
salir = False
while not salir:
    opc = menu()

    if opc == 0:  #Agregar científicos
        pedir = True
        while pedir:
            nombre = input("Ingrese nombre: ").upper()
            if any(cientifico.nombre == nombre for cientifico in lista_cientificos): #Verifica si el nombre del científico ya esta registrado
                print("El nombre del científico ya existe.")
            else:
                pedir = False
        pedir = True
        while pedir:
            try:
                grado = int(input("Ingrese grado (1-5): ")) 
                if grado < 1 or grado > 5: #Verifica que el grado ingresado sea entre 1 y 5
                    print("Grado inválido, debe ser un número entre 1 y 5.")
                else:
                    pedir = False
            except ValueError: #Verifica que el grado ingresado sea un numero
                print("Grado inválido, debe ser un número entre 1 y 5.")

        cientifico = Cientifico(nombre, grado)
        lista_cientificos.append(cientifico)
        print("Científico agregado exitosamente 👍👌") #Printea en emojis para aumentar la felicidad del usuario

    if opc == 1: #Mostrar cientificos
        if lista_cientificos == []:
            print("No hay cientificos cargados")
        else:
            mostrar_cientificos(lista_cientificos) #llama a la función mostrar cientificos

    if opc == 2:  #Agregar secuencia a científico
        if lista_cientificos == []:
            print("No hay cientificos cargados")
        else:
            #Mostrar cientifico
            print("Elija el científico al que agregar la secuencia:")
            for pos in range(len(lista_cientificos)):
                print(f"{pos} - {lista_cientificos[pos]}")
            #Pedir y validar
            pedir = True
            while pedir:
                try:
                    posicion_cientifico = int(input("Ingrese la posición del cientifico: "))
                    if posicion_cientifico < 0 or posicion_cientifico >= len(lista_cientificos): #Verifica que la posicion ingresada este dentro del rango
                        print("Posición incorrecta")
                    else:
                        pedir = False
                except ValueError: #Verifica que la posicion ingresada sea un numero
                    print("Ingrese unicamente números")
            #Mostrar
            print(f"Cientifico seleccionado: {lista_cientificos[posicion_cientifico]}")
            #Pedir la secuencia y verifica que los codones sean validos
            secuencia = pedir_secuencia_valida()
            while not codones_validos(secuencia):
                print("Ingrese unicamente codones presentes en el archivo cargado")
                secuencia = pedir_secuencia_valida()
            #Agrega la secuencia a la lista de secuencias del cientifico elegido
            lista_cientificos[posicion_cientifico].lista_secuencias.append(secuencia)
            print(lista_cientificos[posicion_cientifico])
            print("Secuencia agregada correctamente 👍🙂")

    if opc == 3:  #Traducir secuencia
        #Genera lista filtrada en la que solo están los cientificos con al menos 1 secuencia
        lista_filtrada = []
        for pos in range(len(lista_cientificos)):
            if lista_cientificos[pos].mostrar_ultima_secuencia() != "":
                lista_filtrada.append(lista_cientificos[pos])
        #Verifica que hay al menos 1 cientifico con al menos 1 secuencia
        if lista_filtrada == []:
            print("No hay cientificos con al menos 1 secuencia cargados")
        else:
            #Mostrar cientifico
            print("Elija el científico al que traducir a proteína su ultima secuencia:")
            for pos in range(len(lista_filtrada)):
                print(f"{pos} - {lista_filtrada[pos]}")
            #Pedir y validar
            pedir = True
            while pedir:
                try:
                    posicion_cientifico = int(input("Ingrese la posición del cientifico: "))
                    if posicion_cientifico < 0 or posicion_cientifico >= len(lista_filtrada):
                        print("Posición incorrecta")
                    else:
                        pedir = False
                except ValueError:
                    print("Ingrese unicamente números")
            #Mostrar
            print(f"Cientifico seleccionado: {lista_filtrada[posicion_cientifico]}")
            #Traducir secuencia
            ultima_secuencia = lista_filtrada[posicion_cientifico].mostrar_ultima_secuencia()
            proteina = ""
            aminoacido = ""
            for base in range(0, len(ultima_secuencia), 3):
                codon = ultima_secuencia[base:base + 3]
                aminoacido = codigos_geneticos.get(codon, "X")
                proteina += aminoacido
            print(f"La proteina generada con la ultima secuencia es: {proteina}")

    if opc == 4:  #Científico con secuencia más larga
        if lista_cientificos == []:
            print("No hay cientificos cargados")
        else:
            #Recorre y verifica cual es la secuencia mas larga
            cientificos_sec_mas_larga = {}
            sec_max = ""
            for cientifico in lista_cientificos:
                for sec in cientifico.lista_secuencias:
                    for x in range(len(sec)):
                        if len(sec) >= len(sec_max):
                            sec_max = sec
            #Elige la mas larga sabiendo cual es el máximo
            for cientifico in lista_cientificos:
                for sec in cientifico.lista_secuencias:
                    for x in range(len(sec)):
                        if len(sec) >= len(sec_max):
                            cientificos_sec_mas_larga[cientifico.nombre] = sec
            #Muestra los cientificos con la secuencia mas larga, teniendo en cuenta que pueden ser mas de 1
            print("Estos son el/los cientificos con la secuencia mas larga")
            for c in cientificos_sec_mas_larga:
                print(f"Cientifico: {c}, Secuencia: {cientificos_sec_mas_larga[c]}") #Muestra al cientifico con la secuencia mas larga

    if opc == 5:  #Exportar científicos
        if lista_cientificos == []:
            print("No hay cientificos cargados")
        else:
            #Pide al usuario la cantidad minima de secuencias
            cantidad_minima = 0
            pedir = True
            while pedir:
                try:
                    cantidad_minima = int(input("Ingrese la cantidad mínima de secuencias estudiadas: "))
                    if cantidad_minima>=0:
                        pedir = False
                    else:
                        print("Ingrese un número entero positivo")
                        
                except ValueError:      #Verifica que el valor ingresado sea un numero entero
                    print("Ingrese un número entero")
            #Pide al usuario la ruta y el nombre del archivo
            ruta_archivo = input("Ingrese la ruta y nombre del archivo de destino: ")
            with open(ruta_archivo, 'w') as archivo:    
                for cientifico in lista_cientificos:
                    if len(cientifico.lista_secuencias) >= cantidad_minima:
                        #Pone sin secuencias si no hay secuencias
                        if cientifico.lista_secuencias != []:
                            ultima_secuencia = cientifico.lista_secuencias[-1]
                        else:
                            ultima_secuencia = "Sin secuencias"
                        #Escribe la información del cientifico en el archivo en el orden adecuado
                        archivo.write(f"{cientifico.nombre} ({cientifico.grado}) - {ultima_secuencia} - {len(cientifico.lista_secuencias)} \n") 

            print(f"Científicos exportados a {ruta_archivo}.")

    if opc == 6:  #Salir
        print("Programa terminado")
        salir = True
