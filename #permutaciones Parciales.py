#permutaciones Parciales

import os
from math import perm

def main():
    # Configuración de rutas (ajusta según tu sistema)
    os.chdir(r"C:\Users\gabri\Documents\SCRIPTS_ESTUDIO_PYTHON\archivos descargados python village")
    input_file = 'rosalind_pper.txt'
    output_file = 'resultado_pper.txt'
    
    # Leer datos de entrada
    try:
        with open(input_file, 'r') as f:
            n, k = map(int, f.read().strip().split())
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {input_file}")
        return
    except ValueError:
        print("Error: El archivo debe contener dos enteros positivos n y k")
        return
    
    # Validar los valores de entrada
    if not (0 < n <= 100) or not (0 < k <= 10) or k > n:
        print("Error: Los valores deben cumplir 100 ≥ n > 0 y 10 ≥ k > 0 y k ≤ n")
        return
    
    # Calcular P(n, k) = n! / (n-k)! mod 1,000,000
    # Podemos calcularlo como n × (n-1) × ... × (n-k+1) mod 1,000,000
    result = 1
    for i in range(n, n - k, -1):
        result = (result * i) % 1000000
    
    # Guardar resultado
    with open(output_file, 'w') as f:
        f.write(f"{result}\n")
    
    print(f"Resultado calculado: {result}")
    print(f"Resultado guardado en: {os.path.abspath(output_file)}")

if __name__ == "__main__":
    main()