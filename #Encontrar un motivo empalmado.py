#Encontrar un motivo empalmado

import os
from Bio import SeqIO

def find_spliced_motif(s, t):
    """Find indices of t as a subsequence in s"""
    indices = []
    i = 0  # index for s
    j = 0  # index for t
    
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            indices.append(i + 1)  # Using 1-based indexing
            j += 1
        i += 1
    
    return indices if j == len(t) else None

def main():
    # Configuración de rutas (ajusta según tu sistema)
    os.chdir(r"C:\Users\gabri\Documents\SCRIPTS_ESTUDIO_PYTHON\archivos descargados python village")
    input_file = 'rosalind_sseq.txt'
    output_file = 'resultado_sseq.txt'
    
    try:
        # Leer los datos en formato FASTA
        records = list(SeqIO.parse(input_file, "fasta"))
        s = str(records[0].seq)
        t = str(records[1].seq)
    except (FileNotFoundError, IndexError):
        print(f"Error: No se encontró {input_file} o no tiene el formato correcto")
        return
    
    # Encontrar los índices del motivo
    indices = find_spliced_motif(s, t)
    
    if not indices:
        print("Error: t no es un subsequence de s")
        return
    
    # Guardar resultados
    with open(output_file, 'w') as f:
        f.write(' '.join(map(str, indices)) + '\n')
    
    print("Índices encontrados:", ' '.join(map(str, indices)))
    print(f"Resultados guardados en: {os.path.abspath(output_file)}")

if __name__ == "__main__":
    main()