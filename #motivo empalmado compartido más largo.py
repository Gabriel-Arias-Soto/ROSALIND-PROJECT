#motivo empalmado compartido más largo

import os
from Bio import SeqIO
from pathlib import Path

def encontrar_lcs(s, t):
    """Encuentra la subsecuencia común más larga usando programación dinámica"""
    m, n = len(s), len(t)
    # Crear tabla DP (m+1 x n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Llenar la tabla DP
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Reconstruir la secuencia LCS
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if s[i-1] == t[j-1]:
            lcs.append(s[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    return ''.join(reversed(lcs))

def main():
    # Configuración de directorios (ajusta a tu sistema)
    directorio = Path(r"C:\Users\gabri\Documents\SCRIPTS_ESTUDIO_PYTHON\archivos descargados python village")
    archivo_entrada = directorio / "rosalind_lcsq.txt"
    archivo_salida = directorio / "resultado_lcsq.txt"
    
    # Crear directorio si no existe
    directorio.mkdir(parents=True, exist_ok=True)
    
    try:
        # Leer secuencias FASTA
        registros = list(SeqIO.parse(archivo_entrada, "fasta"))
        if len(registros) < 2:
            raise ValueError("El archivo debe contener al menos 2 secuencias")
        
        s = str(registros[0].seq).upper()
        t = str(registros[1].seq).upper()
        
        # Validar secuencias
        if not all(c in 'ACGT' for c in s + t):
            raise ValueError("Las secuencias solo pueden contener A, C, G, T")
        
        # Encontrar LCS
        resultado = encontrar_lcs(s, t)
        
        # Guardar resultados
        with open(archivo_salida, 'w') as f:
            f.write(resultado + '\n')
        
        print("\n✅ Análisis completado:")
        print(f"Secuencia 1: {len(s)} bases")
        print(f"Secuencia 2: {len(t)} bases")
        print(f"LCS encontrado ({len(resultado)} bases): {resultado}")
        print(f"Resultado guardado en: {archivo_salida}")
    
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        return

if __name__ == "__main__":
    main()