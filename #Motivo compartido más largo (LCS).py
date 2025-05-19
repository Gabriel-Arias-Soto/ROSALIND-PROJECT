#Motivo compartido más largo (LCS)

import os
from pathlib import Path

def parse_fasta(filename):
    """Lee archivos FASTA y devuelve un diccionario {id: secuencia}."""
    with open(filename, 'r') as file:
        data = file.read().split('>')[1:]  # Ignorar el primer elemento vacío
    sequences = {}
    for entry in data:
        lines = entry.split('\n')
        seq_id = lines[0].strip()
        seq = ''.join(lines[1:]).strip()
        sequences[seq_id] = seq
    return sequences

def find_shared_motif(sequences):
    """Encuentra el substring común más largo entre todas las secuencias."""
    if not sequences:
        return ""
    
    # Tomar la secuencia más corta como referencia
    shortest_seq = min(sequences.values(), key=len)
    max_len = len(shortest_seq)
    motif = ""
    
    # Probar todos los posibles substrings de mayor a menor longitud
    for length in range(max_len, 0, -1):
        for start in range(0, max_len - length + 1):
            candidate = shortest_seq[start:start + length]
            
            # Verificar si el candidato está en todas las secuencias
            if all(candidate in seq for seq in sequences.values()):
                if len(candidate) > len(motif):
                    motif = candidate
                    # Retornar al encontrar el primer máximo (puede haber varios)
                    return motif
    return motif

def main():
    # Configuración de rutas (ajusta según tu sistema)
    os.chdir(r"C:\Users\gabri\Documents\SCRIPTS_ESTUDIO_PYTHON\archivos descargados python village")
    input_file = 'rosalind_lcsm.txt'
    output_file = 'resultado_lcsm.txt'
    
    # Leer datos
    try:
        sequences = parse_fasta(input_file)
    except FileNotFoundError:
        print(f"Error: No se encontró {input_file}. Creando archivo de ejemplo...")
        example_data = """>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA"""
        Path(input_file).write_text(example_data)
        sequences = parse_fasta(input_file)
    
    # Calcular motivo compartido
    lcsm = find_shared_motif(sequences)
    
    # Guardar y mostrar resultados
    with open(output_file, 'w') as f:
        f.write(lcsm + '\n')
    
    print(f"\nMotivo compartido más largo: {lcsm}")
    print(f"Resultado guardado en: {os.path.abspath(output_file)}")

if __name__ == "__main__":
    main()