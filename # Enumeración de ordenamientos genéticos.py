# Enumeración de ordenamientos genéticos orientados

import os
from itertools import permutations, product

def main():
    # Configuración de rutas (ajusta según tu sistema)
    os.chdir(r"C:\Users\gabri\Documents\SCRIPTS_ESTUDIO_PYTHON\archivos descargados python village")
    input_file = 'rosalind_sign.txt'
    output_file = 'resultado_sign.txt'
    
    # Leer datos de entrada
    try:
        with open(input_file, 'r') as f:
            n = int(f.read().strip())
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {input_file}")
        return
    except ValueError:
        print("Error: El archivo debe contener un único entero positivo n ≤ 6")
        return
    
    # Validar entrada
    if not 1 <= n <= 6:
        print("Error: n debe ser un entero entre 1 y 6")
        return
    
    # Generar todas las permutaciones con signos
    numbers = range(1, n+1)
    signed_perms = []
    
    # Generar todas las permutaciones de los números
    for perm in permutations(numbers):
        # Generar todas las combinaciones de signos (+/-) para cada permutación
        for signs in product([-1, 1], repeat=n):
            signed_perm = [sign * num for sign, num in zip(signs, perm)]
            signed_perms.append(signed_perm)
    
    # Guardar resultados
    with open(output_file, 'w') as f:
        # Escribir el número total de permutaciones con signo
        f.write(f"{len(signed_perms)}\n")
        
        # Escribir cada permutación con signo
        for perm in signed_perms:
            f.write(' '.join(map(str, perm)) + '\n')
    
    print(f"Total de permutaciones con signo: {len(signed_perms)}")
    print(f"Resultados guardados en: {os.path.abspath(output_file)}")

if __name__ == "__main__":
    main()