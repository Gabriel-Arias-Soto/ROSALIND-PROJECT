# OPEN READING FRAMES

import os
from pathlib import Path
from Bio.Seq import Seq
from Bio import SeqIO

def main():
    # Configuración de rutas (ajusta según tu sistema)
    os.chdir(r"C:\Users\gabri\Documents\SCRIPTS_ESTUDIO_PYTHON\archivos descargados python village")
    input_file = 'rosalind_orf.txt'
    output_file = 'resultado_orf.txt'
    
    # Diccionario de traducción de codones DNA a aminoácidos
    CODON_TABLE = {
        'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
        'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
        'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
        'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
        'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
        'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*',
        'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W',
        'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }

    # Leer datos de entrada
    try:
        with open(input_file, 'r') as f:
            record = next(SeqIO.parse(f, 'fasta'))
            dna_seq = str(record.seq)
    except FileNotFoundError:
        print(f"Error: No se encontró {input_file}. Creando archivo de ejemplo...")
        example_data = """>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"""
        Path(input_file).write_text(example_data)
        record = next(SeqIO.parse(example_data.splitlines(), 'fasta'))
        dna_seq = str(record.seq)

    # Función para traducir ORFs
    def translate_sequence(sequence):
        proteins = set()
        for i in range(len(sequence) - 2):
            codon = sequence[i:i+3]
            if codon == 'ATG':  # Start codon
                protein = []
                for j in range(i, len(sequence) - 2, 3):
                    current_codon = sequence[j:j+3]
                    amino_acid = CODON_TABLE.get(current_codon, '')
                    if amino_acid == '*':  # Stop codon
                        proteins.add(''.join(protein))
                        break
                    protein.append(amino_acid)
        return proteins

    # Obtener todas las posibles proteínas
    all_proteins = set()
    
    # Cadena directa y sus marcos de lectura
    for i in range(3):
        all_proteins.update(translate_sequence(dna_seq[i:]))
    
    # Cadena complementaria inversa y sus marcos de lectura
    reverse_complement = str(Seq(dna_seq).reverse_complement())
    for i in range(3):
        all_proteins.update(translate_sequence(reverse_complement[i:]))

    # Guardar resultados
    with open(output_file, 'w') as f:
        for protein in all_proteins:
            f.write(f"{protein}\n")

    print("\nProteínas encontradas:")
    for protein in all_proteins:
        print(protein)
    print(f"\nResultados guardados en: {os.path.abspath(output_file)}")

if __name__ == "__main__":
    main()