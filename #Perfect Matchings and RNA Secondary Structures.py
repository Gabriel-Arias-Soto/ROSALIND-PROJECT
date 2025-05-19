#Perfect Matchings and RNA Secondary Structures

import os
from pathlib import Path
from math import factorial
from collections import defaultdict

def main():
    # Configuración de rutas (ajusta según tu sistema)
    os.chdir(r"C:\Users\gabri\Documents\SCRIPTS_ESTUDIO_PYTHON\archivos descargados python village")
    input_file = 'rosalind_pmch.txt'
    output_file = 'resultado_pmch.txt'
    
    # Leer datos de entrada
    try:
        with open(input_file, 'r') as f:
            # Saltar la línea del encabezado si existe
            lines = f.readlines()
            rna = ''.join(line.strip() for line in lines[1:] if not line.startswith('>'))
    except FileNotFoundError:
        print(f"Error: No se encontró {input_file}. Creando archivo de ejemplo...")
        example_data = """>Rosalind_23
AGCUAGUCAU"""
        Path(input_file).write_text(example_data)
        rna = "AGCUAGUCAU"  # Datos de muestra
    
    # Contar las ocurrencias de cada base
    counts = defaultdict(int)
    for base in rna:
        counts[base] += 1
    
    # Verificar que las cuentas sean válidas (A=U y C=G)
    if counts['A'] != counts['U'] or counts['C'] != counts['G']:
        print("Error: La cadena RNA no tiene igual número de A-U y C-G")
        return
    
    # Calcular el número de emparejamientos perfectos
    # Para A-U: factorial del número de A (o U)
    # Para C-G: factorial del número de C (o G)
    a_pairs = factorial(counts['A'])
    c_pairs = factorial(counts['C'])
    total = a_pairs * c_pairs
    
    # Guardar resultado
    with open(output_file, 'w') as f:
        f.write(f"{total}\n")
    
    print(f"Resultado calculado: {total}")
    print(f"Resultado guardado en: {os.path.abspath(output_file)}")

if __name__ == "__main__":
    main()