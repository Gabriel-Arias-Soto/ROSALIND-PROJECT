#Independent Alleles

import os
from math import comb
from pathlib import Path

def calculate_probability(k, N):
    """
    Calcula la probabilidad de que al menos N organismos en la generación k
    tengan genotipo Aa Bb, asumiendo apareamiento con Aa Bb en cada generación.
    
    Args:
        k (int): Número de generaciones
        N (int): Número mínimo deseado de organismos Aa Bb
    
    Returns:
        float: Probabilidad solicitada
    """
    total_organisms = 2 ** k
    prob_aa_bb = 0.25  # Probabilidad de Aa Bb en cada descendiente
    
    # Usamos probabilidad binomial acumulativa: P(X >= N) = 1 - P(X < N)
    probability = 0.0
    for i in range(N, total_organisms + 1):
        probability += comb(total_organisms, i) * (prob_aa_bb ** i) * ((1 - prob_aa_bb) ** (total_organisms - i))
    
    return probability

def main():
    # Configuración de rutas (ajusta según tu sistema)
    os.chdir(r"C:\Users\gabri\Documents\SCRIPTS_ESTUDIO_PYTHON\archivos descargados python village")
    input_file = 'rosalind_lia.txt'
    output_file = 'resultado_lia.txt'
    
    # Leer datos de entrada
    try:
        with open(input_file, 'r') as f:
            data = f.read().strip().split()
            k = int(data[0])
            N = int(data[1])
    except FileNotFoundError:
        print(f"Error: No se encontró {input_file}. Creando archivo de ejemplo...")
        Path(input_file).write_text("2 1")  # Datos de muestra
        k, N = 2, 1  # Valores por defecto
    
    # Calcular probabilidad
    probability = calculate_probability(k, N)
    
    # Guardar resultado (redondeado a 3 decimales como en el ejemplo)
    with open(output_file, 'w') as f:
        f.write(f"{probability:.3f}\n")
    
    # Mostrar resultados
    print("\n" + "="*50)
    print(f"Generaciones (k): {k}")
    print(f"Mínimo requerido (N): {N}")
    print(f"Probabilidad calculada: {probability:.6f}")
    print(f"Resultado guardado en: {os.path.abspath(output_file)}")
    print("="*50 + "\n")

if __name__ == "__main__":
    main()