#Corrección de errores en lecturas

import os
from Bio import SeqIO
from collections import defaultdict

def reverse_complement(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join([complement[base] for base in dna[::-1]])

def hamming_distance(s1, s2):
    return sum(1 for a, b in zip(s1, s2) if a != b)

def correct_errors(reads):
    count = defaultdict(int)
    rc_count = defaultdict(int)
    
    # Count occurrences of each read and its reverse complement
    for read in reads:
        count[read] += 1
        rc_count[reverse_complement(read)] += 1
    
    corrections = []
    correct_reads = set()
    
    # Identify correct reads (appear at least twice including reverse complements)
    for read in reads:
        total = count[read] + rc_count[read]
        if total >= 2:
            correct_reads.add(read)
    
    # Find corrections for incorrect reads
    for read in reads:
        if read in correct_reads:
            continue
            
        found_correction = None
        # Check against all correct reads
        for correct in correct_reads:
            if hamming_distance(read, correct) == 1:
                if found_correction is None:
                    found_correction = correct
                else:
                    # More than one possible correction, skip
                    found_correction = None
                    break
        
        # Also check reverse complements of correct reads
        if found_correction is None:
            for correct in correct_reads:
                rc = reverse_complement(correct)
                if hamming_distance(read, rc) == 1:
                    if found_correction is None:
                        found_correction = rc
                    else:
                        found_correction = None
                        break
        
        if found_correction is not None:
            corrections.append(f"{read}->{found_correction}")
    
    return corrections

def main():
    # Configuración de rutas
    os.chdir(r"C:\Users\gabri\Documents\SCRIPTS_ESTUDIO_PYTHON\archivos descargados python village")
    input_file = 'rosalind_corr.txt'
    output_file = 'resultado_corr.txt'
    
    try:
        # Leer las secuencias del archivo FASTA
        records = list(SeqIO.parse(input_file, 'fasta'))
        reads = [str(record.seq) for record in records]
    except FileNotFoundError:
        print(f"Error: No se encontró {input_file}")
        return
    
    # Obtener correcciones
    corrections = correct_errors(reads)
    
    # Guardar resultados
    with open(output_file, 'w') as f:
        f.write('\n'.join(corrections) + '\n')
    
    print("Correcciones encontradas:")
    for correction in corrections:
        print(correction)
    print(f"Resultados guardados en: {os.path.abspath(output_file)}")

if __name__ == "__main__":
    main()