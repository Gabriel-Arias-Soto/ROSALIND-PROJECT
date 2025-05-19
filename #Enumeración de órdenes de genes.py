#Enumeración de órdenes de genes

import os
from pathlib import Path
from itertools import permutations

def main():
    # Configuración de rutas (ajusta según tu sistema)
    os.chdir(r"C:\Users\gabri\Documents\SCRIPTS_ESTUDIO_PYTHON\archivos descargados python village")
    input_file = 'rosalind_perm.txt'
    output_file = 'resultado_perm.txt'
    
    # Leer datos de entrada
    try:
        with open(input_file, 'r') as f:
            n = int(f.read().strip())
    except FileNotFoundError:
        print(f"Error: No se encontró {input_file}. Creando archivo de ejemplo...")
        Path(input_file).write_text("3")  # Datos de muestra
        n = 3  # Valor por defecto
    
    # Validar entrada
    if n < 1 or n > 7:
        print("Error: n debe estar entre 1 y 7")
        return
    
    # Generar todas las permutaciones
    numbers = list(range(1, n+1))
    all_permutations = list(permutations(numbers))
    
    # Guardar resultados
    with open(output_file, 'w') as f:
        f.write(f"{len(all_permutations)}\n")  # Total de permutaciones
        for perm in all_permutations:
            f.write(" ".join(map(str, perm)) + "\n")
    
    # Mostrar resultados en consola
    print(f"Total de permutaciones: {len(all_permutations)}")
    print("Permutaciones:")
    for perm in all_permutations:
        print(" ".join(map(str, perm)))
    print(f"\nResultados guardados en: {os.path.abspath(output_file)}")

if __name__ == "__main__":
    main()