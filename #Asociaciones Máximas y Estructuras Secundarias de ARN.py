#Asociaciones Máximas y Estructuras Secundarias de ARN

import os
from collections import defaultdict
from math import factorial
from Bio import SeqIO
from pathlib import Path

def count_max_matchings(rna):
    """Count all possible maximum matchings in RNA secondary structure"""
    counts = defaultdict(int)
    for base in rna:
        counts[base] += 1
    
    # Pairs we can form
    au_pairs = min(counts['A'], counts['U'])
    cg_pairs = min(counts['C'], counts['G'])
    
    # Calculate possible matchings
    au_fact = factorial(max(counts['A'], counts['U'])) // factorial(abs(counts['A'] - counts['U']))
    cg_fact = factorial(max(counts['C'], counts['G'])) // factorial(abs(counts['C'] - counts['G']))
    
    return au_fact * cg_fact

def main():
    # Configure directories (as in your previous scripts)
    directorio = Path(r"C:\Users\gabri\Documents\SCRIPTS_ESTUDIO_PYTHON\archivos descargados python village")
    archivo_entrada = directorio / "rosalind_mmch.txt"
    archivo_salida = directorio / "resultado_mmch.txt"
    
    # Create directory if needed
    directorio.mkdir(parents=True, exist_ok=True)
    
    try:
        # Read RNA sequence from FASTA
        record = next(SeqIO.parse(archivo_entrada, "fasta"))
        rna = str(record.seq).upper()
        
        # Validate RNA sequence
        if any(base not in 'ACGU' for base in rna):
            raise ValueError("Invalid RNA sequence")
        if len(rna) > 100:
            raise ValueError("RNA sequence too long (max 100 bases)")
        
        # Calculate maximum matchings
        result = count_max_matchings(rna)
        
        # Save results
        with open(archivo_salida, 'w') as f:
            f.write(f"{result}\n")
        
        print(f"\n✅ Resultado guardado en: {archivo_salida}")
        print(f"Total de emparejamientos máximos: {result}")
    
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        return

if __name__ == "__main__":
    main()