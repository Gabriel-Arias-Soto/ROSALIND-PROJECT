#Introducción a las cadenas aleatorias

import os
import math

def main():
    # Configuración de rutas (ajusta según tu sistema)
    os.chdir(r"C:\Users\gabri\Documents\SCRIPTS_ESTUDIO_PYTHON\archivos descargados python village")
    input_file = 'rosalind_prob.txt'
    output_file = 'resultado_prob.txt'
    
    # Leer datos de entrada
    try:
        with open(input_file, 'r') as f:
            lines = f.readlines()
            s = lines[0].strip()
            A = list(map(float, lines[1].strip().split()))
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {input_file}")
        return
    except (IndexError, ValueError):
        print("Error: El formato del archivo debe ser:\n<DNA_string>\n<valores GC-content>")
        return
    
    # Precalcular conteos de bases
    count_gc = s.count('G') + s.count('C')
    count_at = len(s) - count_gc
    
    # Calcular probabilidades logarítmicas para cada GC-content
    B = []
    for gc_content in A:
        # Calcular probabilidades de cada base
        prob_gc = gc_content / 2
        prob_at = (1 - gc_content) / 2
        
        # Calcular probabilidad total (en escala logarítmica)
        if prob_gc == 0 or prob_at == 0:
            log_prob = float('-inf')  # Caso de probabilidad cero
        else:
            prob = (prob_gc ** count_gc) * (prob_at ** count_at)
            log_prob = math.log10(prob) if prob > 0 else float('-inf')
        
        B.append(log_prob)
    
    # Guardar resultado
    with open(output_file, 'w') as f:
        f.write(' '.join(f"{x:.3f}" for x in B) + '\n')
    
    print("Resultado calculado:")
    print(' '.join(f"{x:.3f}" for x in B))
    print(f"Resultado guardado en: {os.path.abspath(output_file)}")

if __name__ == "__main__":
    main()