#Números Catalanes y Estructuras Secundarias de ARN

import os
from collections import defaultdict
from Bio import SeqIO

def count_noncrossing_matchings(rna):
    """Count noncrossing perfect matchings using dynamic programming"""
    n = len(rna)
    pair = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}
    
    # Initialize DP table
    dp = [[0] * n for _ in range(n)]
    
    # Base case: empty subsequences have 1 matching
    for i in range(n):
        dp[i][i-1] = 1  # Handles empty strings when i > j
    
    for length in range(2, n+1, 2):  # Only even lengths matter
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = 0
            for k in range(i+1, j+1, 2):  # Check possible pairings
                if rna[k] == pair[rna[i]]:
                    # Ensure indices are within bounds
                    left = dp[i+1][k-1] if (i+1 <= k-1) else 1
                    right = dp[k+1][j] if (k+1 <= j) else 1
                    dp[i][j] += left * right
                    dp[i][j] %= 1000000
    
    return dp[0][n-1]

def main():
    # Configuración de rutas
    os.chdir(r"C:\Users\gabri\Documents\SCRIPTS_ESTUDIO_PYTHON\archivos descargados python village")
    input_file = 'rosalind_cat.txt'
    output_file = 'resultado_cat.txt'
    
    try:
        with open(input_file) as f:
            record = next(SeqIO.parse(f, 'fasta'))
            rna = str(record.seq).upper()
    except FileNotFoundError:
        print(f"Error: No se encontró {input_file}")
        return
    
    # Verificar pares balanceados
    counts = {'A': rna.count('A'), 'U': rna.count('U'),
              'C': rna.count('C'), 'G': rna.count('G')}
    if counts['A'] != counts['U'] or counts['C'] != counts['G']:
        print("Error: La secuencia no tiene pares A-U y C-G balanceados")
        return
    
    result = count_noncrossing_matchings(rna)
    
    with open(output_file, 'w') as f:
        f.write(f"{result}\n")
    
    print(f"Resultado: {result}")
    print(f"Guardado en: {os.path.abspath(output_file)}")

if __name__ == "__main__":
    main()