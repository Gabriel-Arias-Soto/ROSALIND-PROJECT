#Rosalind ejercios Python village

a = 957
b = 926
c = a - b

print(f"a - b is {c}")

print ("a - b is " + str(c))

############################################

#Solución problema 1 

import os

# Cambiar al directorio donde está el archivo
os.chdir(r"C:\Users\gabri\Documents\SCRIPTS_ESTUDIO_PYTHON\archivos descargados python village")
with open("rosalind_ini2.txt", "r") as file:
    data = file.read().split()  # Divide el contenido en una lista

a = int(data[0])  # Primer número
b = int(data[1])  # Segundo número

c_squared = a**2 + b**2  # Calcula el cuadrado de la hipotenusa
print(c_squared)  # Devuelve el resultado

a = b = c = d = None 

###############################################

#Solución problema 2

# Abrimos el archivo y leemos su contenido
with open("rosalind_ini3.txt", "r") as file:
    lines = file.readlines()

# Extraemos la cadena y los índices
s = lines[0].strip()  # Primera línea es la cadena de texto
a, b, c, d = map(int, lines[1].split())  # Segunda línea contiene los índices

# Obtenemos los segmentos requeridos de la cadena
substring1 = s[a:b+1]  # Incluye el índice b
substring2 = s[c:d+1]  # Incluye el índice d

# Imprimimos la respuesta en el formato solicitado
print(substring1, substring2)

###############################################

#Solución problema 3

# Paso 1: Leer el archivo de entrada
with open("rosalind_ini4.txt", "r") as file:
    line = file.readline()  # Leer la línea (ej: "100 200")
    a, b = map(int, line.split())  # Convertir a enteros

# Paso 2: Generar todos los números en el rango [a, b]
numeros = range(a, b + 1)

# Paso 3: Filtrar solo los impares y sumarlos
suma_impares = 0
for num in numeros:
    if num % 2 != 0:  # ¿Es impar?
        suma_impares += num

# Paso 4: Mostrar el resultado
print(suma_impares)

#################################################

#Solución problema 4

# Abrir el archivo y leer líneas
with open('rosalind_ini5.txt', 'r') as file:
    lines = file.readlines()

# Filtrar líneas pares (1-based) -> índices 1, 3, 5... (0-based: 1, 3, 5...)
even_lines = [line for idx, line in enumerate(lines) if idx % 2 == 1]

# Mostrar las líneas pares (sin crear archivo de salida)
print("=== Líneas pares del archivo ===")
for line in even_lines:
    print(line.strip())  # .strip() para quitar saltos de línea adicionales

##################################################

#Solución problema 5

with open('rosalind_ini6.txt', 'r') as file:
    # Leer el contenido y dividir en palabras (ignorando múltiples espacios)
    words = file.read().strip().split()

# Diccionario para contar palabras (case-sensitive)
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# Escribir resultados en output_ini6.txt
with open('output_ini6.txt', 'w') as out_file:
    for word, count in word_count.items():
        out_file.write(f"{word} {count}\n")

print("Proceso completado. Resultados guardados en 'output_ini6.txt'")

#####################################################
