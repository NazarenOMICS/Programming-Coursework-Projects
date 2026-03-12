# Obligatorio 2 – Gestión y traducción de secuencias genéticas

Este programa fue desarrollado como parte del segundo obligatorio del curso de programación. El objetivo del trabajo fue implementar un sistema en Python que permita gestionar científicos, almacenar secuencias de ADN asociadas a cada uno y realizar operaciones de análisis y traducción genética utilizando un código genético cargado desde archivo.

El programa utiliza programación orientada a objetos y estructuras de datos para organizar la información de los científicos y sus secuencias.

## Estructura del programa

El sistema se basa en la clase `Cientifico`, que representa a un investigador y almacena:

- Nombre del científico
- Grado académico (entre 1 y 5)
- Lista de secuencias de ADN asociadas

Cada científico puede tener múltiples secuencias y el programa permite acceder fácilmente a la última secuencia registrada.

## Carga del código genético

Al iniciar el programa se solicita una ruta a un archivo que contiene el código genético.  
Este archivo se procesa para generar un diccionario que relaciona **codones de ADN con aminoácidos**, permitiendo posteriormente traducir secuencias a proteínas.

## Validación de secuencias

Las secuencias ingresadas deben cumplir las siguientes condiciones:

- Contener únicamente bases **A, T, G o C**
- Tener una longitud **múltiplo de 3**
- Contener codones presentes en el archivo de código genético cargado

Esto asegura que las secuencias puedan ser traducidas correctamente.

## Funcionalidades del programa

El sistema funciona mediante un menú interactivo que permite realizar las siguientes operaciones:

### 1. Agregar científico
Permite registrar un nuevo científico ingresando su nombre y su grado académico.

### 2. Mostrar científicos
Muestra todos los científicos registrados ordenados alfabéticamente, junto con:
- su grado
- su última secuencia registrada
- la cantidad de secuencias asociadas

### 3. Agregar secuencia a un científico
Permite seleccionar un científico y agregar una nueva secuencia de ADN a su lista de secuencias.

### 4. Traducir secuencia a proteína
Toma la última secuencia registrada de un científico y la traduce a una cadena de aminoácidos utilizando el código genético cargado.

### 5. Científico con la secuencia más larga
Busca entre todos los científicos registrados cuál posee la secuencia de mayor longitud.

### 6. Exportar científicos
Permite exportar a un archivo los científicos que tengan al menos una cantidad mínima de secuencias especificada por el usuario.

El archivo exportado incluye:

- nombre del científico
- grado
- última secuencia registrada
- cantidad total de secuencias

### 7. Salir del programa
Finaliza la ejecución del sistema.

## Conceptos de programación utilizados

Este obligatorio incluye el uso de:

- Programación orientada a objetos
- Clases y métodos
- Listas y diccionarios
- Manejo de archivos
- Validación de datos
- Estructuras de control
- Menús interactivos

## Autores

Nazareno Iván Cabrera  
Gastón Silva Larroca