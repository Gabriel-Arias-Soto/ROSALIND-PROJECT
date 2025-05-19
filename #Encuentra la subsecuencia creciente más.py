#Encuentra la subsecuencia creciente más larga usando programación dinámica

import os
from pathlib import Path

def longest_increasing_subsequence(sequence):
    """Encuentra la subsecuencia creciente más larga usando programación dinámica"""
    n = len(sequence)
    # DP[i] almacena la longitud de la LIS que termina en sequence[i]
    dp = [1] * n
    # Para reconstruir la subsecuencia
    prev = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if sequence[j] < sequence[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j

    # Encontrar el máximo y reconstruir la subsecuencia
    max_len = max(dp)
    max_index = dp.index(max_len)

    lis = []
    while max_index != -1:
        lis.append(sequence[max_index])
        max_index = prev[max_index]
    lis.reverse()

    return lis

def longest_decreasing_subsequence(sequence):
    """Encuentra la subsecuencia decreciente más larga (inverso de LIS)"""
    # Convertimos a un problema de secuencia creciente negando los valores
    inverted = [-x for x in sequence]
    lis = longest_increasing_subsequence(inverted)
    return [-x for x in lis]

def main():
    # Configuración de rutas
    os.chdir(r"C:\Users\gabri\Documents\SCRIPTS_ESTUDIO_PYTHON\archivos descargados python village")
    input_file = 'rosalind_lgis.txt'
    output_file = 'resultado_lgis.txt'

    # Leer datos de entrada
    try:
        with open(input_file, 'r') as f:
            lines = f.readlines()
            n = int(lines[0].strip())
            permutation = list(map(int, lines[1].strip().split()))
    except FileNotFoundError:
        print(f"Error: No se encontró {input_file}. Creando archivo de ejemplo...")
        example_data = "5\n5 1 4 2 3"
        Path(input_file).write_text(example_data)
        n = 5
        permutation = [5, 1, 4, 2, 3]

    # Validar entrada
    if len(permutation) != n:
        print("Error: La longitud de la permutación no coincide con n")
        return

    # Encontrar subsecuencias
    lis = longest_increasing_subsequence(permutation)
    lds = longest_decreasing_subsequence(permutation)

    # Guardar resultados
    with open(output_file, 'w') as f:
        f.write(' '.join(map(str, lis)) + '\n')
        f.write(' '.join(map(str, lds)) + '\n')

    # Mostrar resultados
    print("Subsecuencia creciente más larga:")
    print(' '.join(map(str, lis)))
    print("\nSubsecuencia decreciente más larga:")
    print(' '.join(map(str, lds)))
    print(f"\nResultados guardados en: {os.path.abspath(output_file)}")

if __name__ == "__main__":
    main()