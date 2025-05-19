#Creando una matriz de distancia

import os
from Bio import SeqIO
from pathlib import Path

def calculate_p_distance(s1, s2):
    """Calculate the p-distance between two sequences of equal length"""
    differences = sum(1 for a, b in zip(s1, s2) if a != b)
    return differences / len(s1)

def main():
    # Configure directories (as in your previous scripts)
    directorio = Path(r"C:\Users\gabri\Documents\SCRIPTS_ESTUDIO_PYTHON\archivos descargados python village")
    archivo_entrada = directorio / "rosalind_pdst.txt"
    archivo_salida = directorio / "resultado_pdst.txt"
    
    # Create directory if needed
    directorio.mkdir(parents=True, exist_ok=True)
    
    try:
        # Read sequences from FASTA
        records = list(SeqIO.parse(archivo_entrada, "fasta"))
        sequences = [str(record.seq) for record in records]
        
        # Validate sequences
        if len(sequences) > 10:
            raise ValueError("Maximum 10 sequences allowed")
        if any(len(seq) > 1000 for seq in sequences):
            raise ValueError("Maximum sequence length is 1000 bp")
        if len({len(seq) for seq in sequences}) != 1:
            raise ValueError("All sequences must be of equal length")
        
        # Calculate distance matrix
        n = len(sequences)
        matrix = [[0.0] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(i, n):
                distance = calculate_p_distance(sequences[i], sequences[j])
                matrix[i][j] = distance
                matrix[j][i] = distance
        
        # Save results with proper formatting
        with open(archivo_salida, 'w') as f:
            for row in matrix:
                formatted_row = " ".join(f"{val:.5f}" for val in row)
                f.write(formatted_row + "\n")
        
        print(f"\n✅ Matriz de distancias guardada en: {archivo_salida}")
    
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        return

if __name__ == "__main__":
    main()