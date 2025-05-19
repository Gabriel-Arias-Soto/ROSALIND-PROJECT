#Enumerating k-mers Lexicographically

import os
from pathlib import Path
from itertools import product

def main():
    # Configuración de rutas
    os.chdir(r"C:\Users\gabri\Documents\SCRIPTS_ESTUDIO_PYTHON\archivos descargados python village")
    input_file = 'rosalind_lexf.txt'
    output_file = 'resultado_lexf.txt'

    # Leer datos de entrada
    try:
        with open(input_file, 'r') as f:
            lines = f.readlines()
            alphabet = lines[0].strip().split()
            n = int(lines[1].strip())
    except FileNotFoundError:
        print(f"Error: No se encontró {input_file}. Creando archivo de ejemplo...")
        example_data = "A C G T\n2"
        Path(input_file).write_text(example_data)
        alphabet = ['A', 'C', 'G', 'T']
        n = 2

    # Validar entrada
    if not alphabet or n < 1:
        print("Error: Datos de entrada no válidos")
        return

    # Generar todos los k-mers posibles
    kmers = [''.join(p) for p in product(alphabet, repeat=n)]
    
    # Ordenar lexicográficamente (según el orden del alfabeto dado)
    kmers_sorted = sorted(kmers, key=lambda x: [alphabet.index(c) for c in x])

    # Guardar resultados
    with open(output_file, 'w') as f:
        for kmer in kmers_sorted:
            f.write(f"{kmer}\n")

    # Mostrar resultados
    print(f"Alfabeto: {' '.join(alphabet)}")
    print(f"Longitud (n): {n}")
    print("\nK-mers generados:")
    for kmer in kmers_sorted:
        print(kmer)
    print(f"\nTotal de {len(kmers_sorted)} k-mers guardados en: {os.path.abspath(output_file)}")

if __name__ == "__main__":
    main()