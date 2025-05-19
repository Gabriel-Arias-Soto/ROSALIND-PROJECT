#Locating Restriction Sites

import os
from pathlib import Path
from Bio import SeqIO
from Bio.Seq import Seq

def main():
    # Configuración de rutas
    os.chdir(r"C:\Users\gabri\Documents\SCRIPTS_ESTUDIO_PYTHON\archivos descargados python village")
    input_file = 'rosalind_revp.txt'
    output_file = 'resultado_revp.txt'

    # Leer datos de entrada
    try:
        with open(input_file, 'r') as f:
            record = next(SeqIO.parse(f, 'fasta'))
            dna = str(record.seq)
    except FileNotFoundError:
        print(f"Error: No se encontró {input_file}. Creando archivo de ejemplo...")
        example_data = """>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT"""
        Path(input_file).write_text(example_data)
        record = next(SeqIO.parse(example_data.splitlines(), 'fasta'))
        dna = str(record.seq)

    # Encontrar todos los palíndromos inversos
    results = []
    min_len = 4
    max_len = 12
    
    for length in range(min_len, max_len + 1):
        for i in range(len(dna) - length + 1):
            substring = dna[i:i+length]
            rev_complement = str(Seq(substring).reverse_complement())
            
            if substring == rev_complement:
                results.append((i+1, length))  # +1 para convertir a posición 1-based

    # Guardar resultados
    with open(output_file, 'w') as f:
        for pos, length in sorted(results):
            f.write(f"{pos} {length}\n")

    # Mostrar resultados
    print("Palíndromos inversos encontrados:")
    for pos, length in sorted(results):
        print(f"{pos} {length}")
    print(f"\nResultados guardados en: {os.path.abspath(output_file)}")

if __name__ == "__main__":
    main()