#Inferring mRNA from Protein

import os
from pathlib import Path
from collections import defaultdict

def main():
    # Configuración de rutas (ajusta según tu sistema)
    os.chdir(r"C:\Users\gabri\Documents\SCRIPTS_ESTUDIO_PYTHON\archivos descargados python village")
    input_file = 'rosalind_mrna.txt'
    output_file = 'resultado_mrna.txt'
    
    # Tabla de codones RNA -> aminoácido (incluyendo STOP)
    RNA_CODON_TABLE = {
        'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
        'UAU': 'Y', 'UAC': 'Y', 'UAA': 'STOP', 'UAG': 'STOP',
        'UGU': 'C', 'UGC': 'C', 'UGA': 'STOP', 'UGG': 'W',
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }

    # Leer datos de entrada
    try:
        with open(input_file, 'r') as f:
            protein = f.read().strip()
    except FileNotFoundError:
        print(f"Error: No se encontró {input_file}. Creando archivo de ejemplo...")
        Path(input_file).write_text("MA")  # Datos de muestra
        protein = "MA"  # Valor por defecto
    
    # Crear diccionario de conteo de codones por aminoácido
    aa_counts = defaultdict(int)
    for codon, aa in RNA_CODON_TABLE.items():
        aa_counts[aa] += 1
    
    # Calcular número de secuencias RNA posibles (módulo 1,000,000)
    result = aa_counts['STOP']  # Comenzamos con el codón STOP
    for aa in protein:
        result = (result * aa_counts[aa]) % 1000000
    
    # Guardar resultado
    with open(output_file, 'w') as f:
        f.write(f"{result}\n")
    
    print(f"Resultado calculado: {result}")
    print(f"Resultado guardado en: {os.path.abspath(output_file)}")

if __name__ == "__main__":
    main()