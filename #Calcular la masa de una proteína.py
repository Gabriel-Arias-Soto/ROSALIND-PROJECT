#Calcular la masa de una proteína

import os
from pathlib import Path

def main():
    # Configuración de rutas
    os.chdir(r"C:\Users\gabri\Documents\SCRIPTS_ESTUDIO_PYTHON\archivos descargados python village")
    input_file = 'rosalind_prtm.txt'
    output_file = 'resultado_prtm.txt'
    
    # Tabla de masas monoisotópicas (valores exactos)
    MONOISOTOPIC_MASS_TABLE = {
        'A': 71.03711, 'C': 103.00919, 'D': 115.02694, 'E': 129.04259,
        'F': 147.06841, 'G': 57.02146, 'H': 137.05891, 'I': 113.08406,
        'K': 128.09496, 'L': 113.08406, 'M': 131.04049, 'N': 114.04293,
        'P': 97.05276, 'Q': 128.05858, 'R': 156.10111, 'S': 87.03203,
        'T': 101.04768, 'V': 99.06841, 'W': 186.07931, 'Y': 163.06333
    }

    # Leer datos de entrada
    try:
        with open(input_file, 'r') as f:
            protein = f.read().strip().upper()
            if not protein:
                raise ValueError("El archivo está vacío")
            if not all(aa in MONOISOTOPIC_MASS_TABLE for aa in protein):
                raise ValueError("Contiene aminoácidos no válidos")
    except FileNotFoundError:
        print(f"Error: Archivo {input_file} no encontrado. Creando ejemplo...")
        Path(input_file).write_text("SKADYEK")
        protein = "SKADYEK"

    # Calcular masa (SIN agregar agua)
    total_mass = sum(MONOISOTOPIC_MASS_TABLE[aa] for aa in protein)
    
    # Formatear resultado (3 decimales como en el Sample Output)
    formatted_mass = f"{total_mass:.3f}".rstrip('0').rstrip('.') if '.' in f"{total_mass:.3f}" else f"{total_mass:.3f}"
    
    # Guardar resultado
    with open(output_file, 'w') as f:
        f.write(f"{formatted_mass}\n")
    
    print(f"Masa calculada: {formatted_mass}")
    print(f"Resultado guardado en: {os.path.abspath(output_file)}")

if __name__ == "__main__":
    main()