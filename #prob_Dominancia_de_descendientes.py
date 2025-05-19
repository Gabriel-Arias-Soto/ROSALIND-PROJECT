import os
from pathlib import Path

def expected_dominant_offspring(couples):
    """
    Calcula el número esperado de descendientes con fenotipo dominante.
    Cada pareja produce exactamente 2 hijos.
    
    Argumentos:
        couples -- Lista de 6 enteros representando el número de parejas para cada genotipo:
                   [AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, aa-aa]
    
    Probabilidades de fenotipo dominante por tipo de pareja:
    AA-AA: 100%   (1.0)
    AA-Aa: 100%   (1.0)
    AA-aa: 100%   (1.0)
    Aa-Aa: 75%    (0.75)
    Aa-aa: 50%    (0.5)
    aa-aa: 0%     (0.0)
    """
    dominance_prob = [1.0, 1.0, 1.0, 0.75, 0.5, 0.0]
    return sum(2 * couple * prob for couple, prob in zip(couples, dominance_prob))

# Configuración inicial para tu PC
def main():
    # 1. Establecer directorio de trabajo (cambia la ruta según tu necesidad)
    working_dir = r"C:\Users\gabri\Documents\SCRIPTS_ESTUDIO_PYTHON\archivos descargados python village"
    os.chdir(working_dir)
    
    # 2. Leer archivo de entrada (crea 'rosalind_iev.txt' con los datos de entrada)
    input_file = 'rosalind_iev.txt'
    
    try:
        with open(input_file, 'r') as f:
            data = f.read().strip()
            couples = list(map(int, data.split()))
            
            if len(couples) != 6:
                raise ValueError("El archivo debe contener exactamente 6 números")
                
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {input_file}")
        print("Creando archivo de ejemplo con los datos del sample...")
        Path(input_file).write_text("1 0 0 1 0 1")  # Datos de muestra
        couples = [1, 0, 0, 1, 0, 1]  # Usar datos de muestra

    # 3. Calcular resultado
    result = expected_dominant_offspring(couples)
    
    # 4. Guardar y mostrar resultados
    output_file = 'resultado_iev.txt'
    with open(output_file, 'w') as f:
        f.write(f"{result}\n")
    
    print("\n" + "="*50)
    print(f"Resultado calculado: {result}")
    print(f"Guardado en: {os.path.abspath(output_file)}")
    print("="*50 + "\n")

if __name__ == "__main__":
    main()