# Obligatorio 1 – Procesamiento de secuencias de ADN

Este programa fue desarrollado como parte del primer obligatorio del curso de programación. El objetivo del trabajo fue implementar distintas funciones para el análisis y manipulación básica de secuencias de ADN utilizando Python.

El programa funciona a través de un menú interactivo que permite al usuario ingresar una secuencia de ADN válida o generar una secuencia aleatoria y luego aplicar distintas operaciones sobre ella.

## Funcionalidades implementadas

El programa incluye las siguientes herramientas para el análisis de secuencias:

1. **Mostrar composición de la secuencia**  
   Calcula la cantidad y el porcentaje de cada base (A, T, C y G) presente en la secuencia.

2. **Calculadora de temperatura de fusión (Tm)**  
   Calcula la temperatura de fusión del ADN utilizando la fórmula simplificada:
   
   Tm = 2 × (A + T) + 4 × (G + C)

3. **Conteo de ORFs (Open Reading Frames)**  
   Identifica posibles marcos de lectura abiertos detectando codones de inicio (ATG) y codones de stop (TAA, TAG, TGA) que mantengan el marco de lectura.

4. **Intercalado de secuencias**  
   Intercala una secuencia con el **inverso de otra secuencia**, generando una nueva secuencia combinada.

5. **Verificación de posibilidad de generar un primer**  
   Evalúa si es posible generar un primer de longitud 5 nucleótidos con al menos **50% de contenido GC** a partir de una posición determinada.

6. **Replicación de secuencia**  
   Permite replicar cada base de la secuencia un número determinado de veces.

7. **Análisis de parejas de bases consecutivas**  
   Genera una matriz que contabiliza las combinaciones de pares de bases consecutivas en la secuencia.

## Validación de secuencias

El programa incluye funciones para validar que las secuencias ingresadas:

- Contengan únicamente bases válidas: **A, T, G o C**
- Tengan al menos un carácter

También permite generar **secuencias aleatorias de ADN** de un largo definido por el usuario.

## Estructura del programa

El código está organizado en funciones independientes que permiten reutilizar y probar cada operación de forma modular. Algunas funciones incluyen pruebas utilizando `assert` para verificar su correcto funcionamiento.

## Autores

Nazareno Iván Cabrera  
Gastón Silva Larroca