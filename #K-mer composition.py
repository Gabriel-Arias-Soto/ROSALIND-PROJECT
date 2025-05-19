#K-mer composition

import os
from collections import defaultdict
from itertools import product
from Bio import SeqIO
from pathlib import Path

class KmerAnalyzer:
    def __init__(self, k=4):
        self.k = k
        self.kmers = self._generate_kmers()
        self.kmer_index = {kmer: idx for idx, kmer in enumerate(self.kmers)}
    
    def _generate_kmers(self):
        """Genera todos los k-mers posibles en orden lexicográfico"""
        bases = ['A', 'C', 'G', 'T']
        return [''.join(p) for p in product(bases, repeat=self.k)]
    
    def analyze_sequence(self, sequence):
        """Calcula la frecuencia de todos los k-mers en la secuencia"""
        counts = defaultdict(int)
        for i in range(len(sequence) - self.k + 1):
            kmer = sequence[i:i+self.k]
            counts[kmer] += 1
        return [counts[kmer] for kmer in self.kmers]

def main():
    # Configuración de rutas (más robusta con pathlib)
    base_dir = Path(r"C:\Users\gabri\Documents\SCRIPTS_ESTUDIO_PYTHON\archivos descargados python village")
    input_file = base_dir / "rosalind_kmer.txt"
    output_file = base_dir / "resultado_kmer.txt"
    
    # Verificar y crear directorio si no existe
    base_dir.mkdir(parents=True, exist_ok=True)
    
    # Manejo de errores mejorado
    try:
        # Leer secuencia FASTA con validación
        if not input_file.exists():
            raise FileNotFoundError(f"Archivo de entrada no encontrado: {input_file}")
        
        records = list(SeqIO.parse(input_file, "fasta"))
        if not records:
            raise ValueError("El archivo FASTA no contiene secuencias")
        
        sequence = str(records[0].seq).upper()
        
        # Validar caracteres de la secuencia
        invalid_chars = set(sequence) - {'A', 'C', 'G', 'T'}
        if invalid_chars:
            raise ValueError(f"Secuencia contiene caracteres inválidos: {invalid_chars}")
        
        # Análisis de k-mers
        analyzer = KmerAnalyzer(k=4)
        composition = analyzer.analyze_sequence(sequence)
        
        # Guardar resultados con formato
        with output_file.open('w') as f:
            f.write(' '.join(map(str, composition)) + '\n')
        
        # Reporte de ejecución
        print("\n" + "═"*50)
        print(f"🔹 Archivo procesado: {input_file}")
        print(f"🔹 Longitud de secuencia: {len(sequence)} bp")
        print(f"🔹 Total de 4-mers analizados: {len(composition)}")
        print(f"🔹 Archivo de resultados: {output_file}")
        print("═"*50 + "\n")
        
    except Exception as e:
        print(f"\n❌ Error: {e}\n")
        return

if __name__ == "__main__":
    main()