#Ensamblaje del Genoma como la Supercadena más Corta
import os
from collections import defaultdict

def find_max_overlap(reads, min_overlap=1):
    """Encuentra el par de lecturas con el mayor solapamiento válido"""
    reada, readb = None, None
    best_ovlp_len = 0
    
    for a in reads:
        for b in reads:
            if a == b:
                continue
                
            # Buscar el mayor solapamiento posible
            max_possible = min(len(a), len(b))
            for k in range(min(max_possible, len(a)-1), min_overlap-1, -1):
                if a.endswith(b[:k]):
                    if k > best_ovlp_len:
                        best_ovlp_len = k
                        reada, readb = a, b
                    break  # Tomamos el mayor posible para este par
    
    return reada, readb, best_ovlp_len

def merge_reads(a, b, overlap_len):
    """Fusiona dos lecturas dado su solapamiento"""
    return a + b[overlap_len:]

def assemble_genome(reads):
    """Ensambla el genoma a partir de lecturas con solapamientos >50%"""
    reads = reads.copy()
    
    while len(reads) > 1:
        a, b, ovlp_len = find_max_overlap(reads)
        
        # Condición del problema: solapamiento >50% de al menos una lectura
        min_len = min(len(a), len(b)) if a and b else 0
        if not a or ovlp_len < min_len/2:
            # Si no hay solapamientos válidos, intentamos con menos restricción
            a, b, ovlp_len = find_max_overlap(reads, min_overlap=10)
            if not a or ovlp_len < 10:
                break
        
        merged = merge_reads(a, b, ovlp_len)
        reads.remove(a)
        reads.remove(b)
        reads.append(merged)
    
    return reads[0] if reads else ""

def read_fasta(file_path):
    """Lee archivo FASTA, devuelve secuencias"""
    sequences = []
    with open(file_path, 'r') as f:
        current_seq = ""
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if current_seq:
                    sequences.append(current_seq)
                current_seq = ""
            else:
                current_seq += line
        if current_seq:
            sequences.append(current_seq)
    return sequences

def verify_coverage(assembly, reads):
    """Verifica que todas las lecturas estén incluidas en el ensamblaje"""
    missing = []
    for read in reads:
        if read not in assembly:
            missing.append(read)
    return missing

def main():
    # Configuración de rutas
    input_dir = r"C:\Users\gabri\Documents\SCRIPTS_ESTUDIO_PYTHON\archivos descargados python village"
    input_file = os.path.join(input_dir, "rosalind_long.txt")
    output_file = os.path.join(input_dir, "resultado_long.txt")
    
    # Leer datos
    reads = read_fasta(input_file)
    print(f"Lecturas cargadas: {len(reads)}")
    print(f"Longitud promedio: {sum(len(r) for r in reads)/len(reads):.1f} bp")
    
    # Ensamblar
    assembly = assemble_genome(reads)
    
    # Verificar resultados
    missing = verify_coverage(assembly, reads)
    if missing:
        print(f"Advertencia: {len(missing)} lecturas no se incluyeron en el ensamblaje")
    else:
        print("Todas las lecturas fueron incluidas en el ensamblaje")
    
    # Guardar resultados
    with open(output_file, 'w') as f:
        f.write(assembly)
    
    print(f"Longitud del ensamblaje: {len(assembly)} bp")
    print(f"Resultado guardado en: {output_file}")

if __name__ == "__main__":
    main()