#Calcular el arreglo de fallos

import os
from Bio import SeqIO
from pathlib import Path

def calcular_arreglo_fallos(secuencia):
    """Calcula el arreglo de fallos (función prefijo) para una secuencia de ADN"""
    n = len(secuencia)
    fallos = [0] * n  # Inicializamos todo con 0
    j = 0  # Longitud del prefijo más largo que también es sufijo
    
    for i in range(1, n):
        # Mientras no coincidan, retrocedemos usando los fallos anteriores
        while j > 0 and secuencia[i] != secuencia[j]:
            j = fallos[j-1]
        
        # Si hay coincidencia, avanzamos
        if secuencia[i] == secuencia[j]:
            j += 1
            fallos[i] = j
        else:
            fallos[i] = 0
    
    return fallos

def main():
    # Configuración de rutas (ajusta según tu sistema)
    directorio = Path(r"C:\Users\gabri\Documents\SCRIPTS_ESTUDIO_PYTHON\archivos descargados python village")
    archivo_entrada = directorio / "rosalind_kmp.txt"
    archivo_salida = directorio / "resultado_kmp.txt"
    
    # Crear directorio si no existe
    directorio.mkdir(parents=True, exist_ok=True)
    
    try:
        # Leer archivo FASTA
        if not archivo_entrada.exists():
            raise FileNotFoundError(f"Archivo no encontrado: {archivo_entrada}")
        
        registro = next(SeqIO.parse(archivo_entrada, "fasta"))
        secuencia = str(registro.seq).upper()
        
        # Validar que sea ADN
        if any(c not in 'ACGT' for c in secuencia):
            raise ValueError("La secuencia contiene caracteres no válidos (solo A,C,G,T permitidos)")
        
        # Calcular arreglo de fallos
        arreglo_fallos = calcular_arreglo_fallos(secuencia)
        
        # Guardar resultados
        with open(archivo_salida, 'w') as f:
            f.write(' '.join(map(str, arreglo_fallos)) + '\n')
        
        print("\n✅ Análisis completado con éxito")
        print(f"🔹 Secuencia analizada: {len(secuencia)} bases")
        print(f"🔹 Resultados guardados en: {archivo_salida}\n")
    
    except Exception as e:
        print(f"\n❌ Error: {str(e)}\n")
        return

if __name__ == "__main__":
    main()