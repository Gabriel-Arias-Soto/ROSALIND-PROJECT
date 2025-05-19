#RNA SPLICING

import os
from pathlib import Path
from Bio import SeqIO
from Bio.Seq import Seq

def main():
    # Configuración de rutas
    os.chdir(r"C:\Users\gabri\Documents\SCRIPTS_ESTUDIO_PYTHON\archivos descargados python village")
    input_file = 'rosalind_splc.txt'
    output_file = 'resultado_splc.txt'

    # Leer datos de entrada
    try:
        records = list(SeqIO.parse(input_file, 'fasta'))
        if len(records) < 2:
            raise ValueError("El archivo debe contener al menos 2 secuencias")
    except FileNotFoundError:
        print(f"Error: No se encontró {input_file}. Creando archivo de ejemplo...")
        example_data = """>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT"""
        Path(input_file).write_text(example_data)
        records = list(SeqIO.parse(example_data.splitlines(), 'fasta'))

    # Procesar secuencias
    dna = str(records[0].seq)
    introns = [str(record.seq) for record in records[1:]]

    # Eliminar intrones
    for intron in introns:
        dna = dna.replace(intron, '')

    # Transcribir y traducir
    mrna = Seq(dna).transcribe()
    protein = mrna.translate(to_stop=True)

    # Guardar resultado
    with open(output_file, 'w') as f:
        f.write(f"{protein}\n")

    # Mostrar resultados
    print(f"Secuencia original: {records[0].seq}")
    print(f"Intrones removidos: {introns}")
    print(f"\nProteína resultante: {protein}")
    print(f"Resultado guardado en: {os.path.abspath(output_file)}")

if __name__ == "__main__":
    main()