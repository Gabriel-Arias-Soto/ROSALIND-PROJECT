#Transiciones y transversiones

import os
from Bio import SeqIO

def calculate_transition_transversion_ratio(s1, s2):
    """Calculate the transition/transversion ratio between two DNA sequences"""
    transitions = 0
    transversions = 0
    
    for base1, base2 in zip(s1, s2):
        if base1 != base2:
            # Check if it's a transition
            if (base1 in 'AG' and base2 in 'AG') or (base1 in 'CT' and base2 in 'CT'):
                transitions += 1
            else:
                transversions += 1
    
    return transitions / transversions if transversions != 0 else float('inf')

def main():
    # Configuración de rutas (ajusta según tu sistema)
    os.chdir(r"C:\Users\gabri\Documents\SCRIPTS_ESTUDIO_PYTHON\archivos descargados python village")
    input_file = 'rosalind_tran.txt'
    output_file = 'resultado_tran.txt'
    
    try:
        # Leer los datos en formato FASTA
        records = list(SeqIO.parse(input_file, "fasta"))
        s1 = str(records[0].seq.upper())
        s2 = str(records[1].seq.upper())
    except (FileNotFoundError, IndexError):
        print(f"Error: No se encontró {input_file} o no tiene el formato correcto")
        return
    
    # Verificar que las secuencias tengan la misma longitud
    if len(s1) != len(s2):
        print("Error: Las secuencias deben tener la misma longitud")
        return
    
    # Calcular la relación transición/transversión
    ratio = calculate_transition_transversion_ratio(s1, s2)
    
    # Guardar resultados
    with open(output_file, 'w') as f:
        f.write(f"{ratio}\n")
    
    print(f"Transiciones/Transversiones: {ratio}")
    print(f"Resultados guardados en: {os.path.abspath(output_file)}")

if __name__ == "__main__":
    main()