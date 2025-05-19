#BIOINFORMATICS STRONGHOLD

import os

# Cambiar al directorio donde está el archivo
os.chdir(r"C:\Users\gabri\Documents\SCRIPTS_ESTUDIO_PYTHON\archivos descargados python village")

# Solution to DNA Nucleotide Count problem
with open('rosalind_dna.txt', 'r') as file:
    dna_string = file.read().strip()  # Read the DNA string

# Initialize counts
a_count = dna_string.count('A')
c_count = dna_string.count('C')
g_count = dna_string.count('G')
t_count = dna_string.count('T')

# Print results separated by spaces
print(f"{a_count} {c_count} {g_count} {t_count}")

#############################################################################################

# Solution to DNA to RNA Transcription problem
with open('rosalind_rna.txt', 'r') as file:
    dna_string = file.read().strip()  # Read the DNA string

# Transcribe DNA to RNA by replacing T with U
rna_string = dna_string.replace('T', 'U')

# Output the result
print(rna_string)

#############################################################################################

# Solution to Reverse Complement DNA problem
with open('rosalind_revc.txt', 'r') as file:
    dna_string = file.read().strip()  # Read the DNA string

# Create complement mapping
complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

# Generate reverse complement
reverse_complement = ''.join([complement[base] for base in reversed(dna_string)])

# Output the result
print(reverse_complement)

#############################################################################################

# Solution to Fibonacci-like Rabbit Population Problem
def rabbit_pairs(n, k):
    # Initialize the first two months
    if n == 1 or n == 2:
        return 1
    # Create a list to store population counts
    population=list()
    population = [0] * (n + 1)
    population[1] = 1
    population[2] = 1
    
    # Calculate population for each subsequent month
    for month in range(3, n + 1):
        population[month] = population[month - 1] + k * population[month - 2]
    
    return population[n]

# Read input (assuming input is two numbers separated by space)
with open('rosalind_fib.txt', 'r') as file:
    n, k = map(int, file.read().split())

# Calculate and print the result
print(rabbit_pairs(n, k))

#############################################################################################

# Solution to GC-content problem
def calculate_gc_content(dna):
    gc_count = dna.count('G') + dna.count('C')
    return (gc_count / len(dna)) * 100

# Read FASTA file
fasta_data = {}
current_id = ""
with open('rosalind_gc.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if line.startswith('>'):
            current_id = line[1:]  # Remove '>' from ID
            fasta_data[current_id] = ""
        else:
            fasta_data[current_id] += line

# Calculate GC-content for each sequence
gc_contents = {}
for seq_id, dna in fasta_data.items():
    gc_contents[seq_id] = calculate_gc_content(dna)

# Find sequence with highest GC-content
max_id = max(gc_contents, key=gc_contents.get)
max_gc = gc_contents[max_id]

# Output result with 6 decimal places
print(f"{max_id}\n{max_gc:.6f}")

#############################################################################################

# Solution to Hamming Distance problem
def hamming_distance(s, t):
    if len(s) != len(t):
        raise ValueError("DNA strings must be of equal length")
    return sum(1 for a, b in zip(s, t) if a != b)

# Read input file
with open('rosalind_hamm.txt', 'r') as file:
    lines = file.readlines()
    s = lines[0].strip()
    t = lines[1].strip()

# Calculate and print Hamming distance
print(hamming_distance(s, t))

#############################################################################################

# Primera Ley de Mendel

with open("rosalind_iprb.txt", "r") as file:
    k, m, n = map(int, file.readline().split())  # Leemos los valores del archivo

def mendels_first_law(k, m, n):
    """Calcula la probabilidad de obtener un descendiente con un alelo dominante."""
    
    total = k + m + n  # Población total
    total_combinations = total * (total - 1)  # Todas las combinaciones posibles

    # Probabilidad de elegir cada pareja y que tenga un fenotipo dominante
    dominant_prob = (
        k * (k - 1) +  # kk → 100% dominante
        2 * k * m +    # km y mk → 100% dominante
        2 * k * n +    # kn y nk → 100% dominante
        m * (m - 1) * 0.75 +  # mm → 75% dominante
        2 * m * n * 0.5  # mn y nm → 50% dominante
    ) / total_combinations

    return round(dominant_prob, 5)  # Redondeamos a 5 decimales como en el ejemplo

# Ejecutamos la función y mostramos el resultado
resultado = mendels_first_law(k, m, n)
print(resultado)

#############################################################################################

#Translating RNA into Protein

# Diccionario que representa la tabla de codones de ARN
codon_table = {
    "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "UAU": "Y", "UAC": "Y", "UAA": "Stop", "UAG": "Stop",
    "UGU": "C", "UGC": "C", "UGA": "Stop", "UGG": "W",
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}

# Función para traducir un ARN en una proteína
def translate_rna_to_protein(rna_sequence):
    protein = ""
    for i in range(0, len(rna_sequence) - 2, 3):  # Leer de 3 en 3
        codon = rna_sequence[i:i+3]
        amino_acid = codon_table.get(codon, "")
        if amino_acid == "Stop":
            break  # Detener la traducción si se encuentra un codón de parada
        protein += amino_acid
    return protein

# Leer la secuencia de ARN desde un archivo
with open("rosalind_prot.txt", "r") as file:
    rna_sequence = file.readline().strip()

# Obtener la secuencia de proteínas
protein_string = translate_rna_to_protein(rna_sequence)

# Imprimir el resultado
print(protein_string)

#############################################################################################

#Finding a Motif in DNA

def find_motif_locations(s, t):
    positions = [i + 1 for i in range(len(s) - len(t) + 1) if s[i:i+len(t)] == t]
    return positions

# Leer el archivo de entrada
input_filename = "rosalind_subs.txt"
output_filename = input_filename.replace(".txt", "_results.txt")

with open(input_filename, "r") as file:
    s = file.readline().strip()
    t = file.readline().strip()

# Encontrar las posiciones de la subcadena
positions = find_motif_locations(s, t)

# Mostrar los resultados
print(" ".join(map(str, positions)))

# Preguntar si se quiere generar el archivo de salida
generate_output = input("¿Generar txt con resultados? (s/n): ").strip().lower()
if generate_output == "s":
    with open(output_filename, "w") as out_file:
        out_file.write(" ".join(map(str, positions)))
    print(f"Resultados guardados en {output_filename}")

#############################################################################################

from collections import Counter

def parse_fasta(filename):
    sequences = []
    with open(filename, "r") as file:
        sequence = ""
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if sequence:
                    sequences.append(sequence)
                sequence = ""
            else:
                sequence += line
        sequences.append(sequence)
    return sequences

def build_profile_matrix(sequences):
    n = len(sequences[0])
    profile = {"A": [0] * n, "C": [0] * n, "G": [0] * n, "T": [0] * n}
    
    for seq in sequences:
        for i, nucleotide in enumerate(seq):
            profile[nucleotide][i] += 1
    
    consensus = "".join(max(profile, key=lambda x: profile[x][i]) for i in range(n))
    
    return consensus, profile

def save_results(filename, consensus, profile):
    output_file = filename.replace(".txt", "_output.txt")
    with open(output_file, "w") as f:
        f.write(consensus + "\n")
        for nucleotide in "ACGT":
            f.write(f"{nucleotide}: {' '.join(map(str, profile[nucleotide]))}\n")
    print(f"Resultados guardados en {output_file}")

def main():
    input_file = "rosalind_cons.txt"  # Ajusta el nombre según corresponda
    sequences = parse_fasta(input_file)
    consensus, profile = build_profile_matrix(sequences)
    print(consensus)
    for nucleotide in "ACGT":
        print(f"{nucleotide}: {' '.join(map(str, profile[nucleotide]))}")
    
    save_option = input("¿Generar archivo de texto con resultados? (s/n): ")
    if save_option.lower() == "s":
        save_results(input_file, consensus, profile)

if __name__ == "__main__":
    main()

#############################################################################################

def mortal_rabbits(n, m):
    # Inicializar lista para contar conejos por edad (1 a m meses)
    population = [0] * (m + 1)    # Índice 0 no se usa, edad comienza en 1
    population[1] = 1  # 1 pareja de recién nacidos en mes 1

    for month in range(2, n + 1):
        # Recién nacidos = suma de conejos maduros (edad >= 2)
        newborns = sum(population[2:])
        
        # Envejecer conejos (empezando desde los mayores)
        for age in range(m, 0, -1):
            if age == m:
                # Conejos mueren al llegar a edad m
                population[age] = 0
            else:
                # Mover al siguiente grupo de edad
                population[age + 1] = population[age]
        
        # Actualizar recién nacidos (edad 1)
        population[1] = newborns

    return sum(population[1:])  # Sumar todos los conejos vivos

# Leer archivo de entrada
with open('rosalind_fibd.txt', 'r') as file:
    n, m = map(int, file.read().split())

# Calcular y mostrar resultado
print(mortal_rabbits(n, m))