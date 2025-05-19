#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solución definitiva para Finding a Protein Motif (Rosalind)
Versión: 3.0 (Julio 2024)
Características:
- Detección precisa de motivos con solapamientos
- Manejo robusto de errores y rate limiting
- Validación de secuencias
- Output compatible al 100% con Rosalind
"""

import re
import requests
import time
from pathlib import Path
from typing import Dict, List, Optional, Set
from concurrent.futures import ThreadPoolExecutor, as_completed

# Configuración global
UNIPROT_API = "https://rest.uniprot.org/uniprotkb"
MAX_RETRIES = 3
REQUEST_TIMEOUT = 20
DELAY_BETWEEN_REQUESTS = 0.6  # Cumple políticas de UniProt
MAX_WORKERS = 5
VALID_AMINOACIDS = set('ACDEFGHIKLMNPQRSTVWY')

class ProteinMotifFinder:
    def __init__(self):
        self.motif_cache: Dict[str, List[int]] = {}
    
    @staticmethod
    def normalize_uniprot_id(uniprot_id: str) -> str:
        """Normaliza IDs de UniProt, manejando casos especiales."""
        base_id = uniprot_id.split('_')[0]
        
        # Manejo de IDs obsoletos (ejemplo)
        id_mapping = {
            'P12345_OLD': 'Q67890_NEW',
            # Agregar otros mapeos necesarios
        }
        return id_mapping.get(base_id, base_id)

    def fetch_sequence_with_retry(self, uniprot_id: str) -> Optional[str]:
        """Descarga secuencias con reintentos y delay automático."""
        normalized_id = self.normalize_uniprot_id(uniprot_id)
        url = f"{UNIPROT_API}/{normalized_id}.fasta"
        
        for attempt in range(MAX_RETRIES):
            try:
                time.sleep(DELAY_BETWEEN_REQUESTS)
                response = requests.get(url, timeout=REQUEST_TIMEOUT)
                response.raise_for_status()
                
                # Parseo seguro de FASTA
                lines = response.text.strip().splitlines()
                if len(lines) < 2:
                    return None
                
                sequence = "".join(lines[1:]).upper()
                if not all(aa in VALID_AMINOACIDS for aa in sequence):
                    print(f"Advertencia: Secuencia {uniprot_id} contiene AA no estándar")
                return sequence
                
            except requests.RequestException as e:
                print(f"Intento {attempt + 1} fallido para {uniprot_id}: {str(e)}")
                if attempt == MAX_RETRIES - 1:
                    return None
                time.sleep(2 ** attempt)  # Backoff exponencial

        return None

    def find_motifs_with_overlap(self, sequence: str) -> List[int]:
        """Busca todos los motivos, incluyendo solapamientos."""
        if not sequence:
            return []
            
        # Usamos lookahead positivo (?=...) para encontrar solapamientos
        pattern = re.compile(r"(?=(N[^P][ST][^P]))")
        return [match.start() + 1 for match in pattern.finditer(sequence)]

    def process_single_protein(self, uniprot_id: str) -> Optional[Dict[str, List[int]]]:
        """Procesa una proteína individual con caché."""
        if uniprot_id in self.motif_cache:
            return {uniprot_id: self.motif_cache[uniprot_id]}
            
        sequence = self.fetch_sequence_with_retry(uniprot_id)
        if not sequence:
            return None
            
        motifs = self.find_motifs_with_overlap(sequence)
        if motifs:
            self.motif_cache[uniprot_id] = motifs
            return {uniprot_id: motifs}
        return None

def load_input_ids(input_file: Path) -> List[str]:
    """Carga IDs desde archivo con validación básica."""
    try:
        with open(input_file, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: Archivo {input_file} no encontrado.")
        return []

def save_results(output_file: Path, results: Dict[str, List[int]]) -> None:
    """Guarda resultados en formato Rosalind con manejo de errores."""
    try:
        with open(output_file, 'w') as f:
            for protein_id, positions in sorted(results.items()):
                f.write(f"{protein_id}\n")
                f.write(" ".join(map(str, sorted(positions))) + "\n")
        print(f"✅ Resultados guardados en {output_file}")
    except IOError as e:
        print(f"❌ Error al guardar resultados: {str(e)}")

def main():
    # Configuración de rutas
    base_dir = Path(__file__).parent
    input_file = base_dir / "archivos descargados python village" / "rosalind_mprt.txt"
    output_file = base_dir / "archivos descargados python village" / "resultado_mprt.txt"
    
    # Cargar IDs
    uniprot_ids = load_input_ids(input_file)
    if not uniprot_ids:
        print("ℹ Usando datos de ejemplo...")
        uniprot_ids = [
            "A2Z669", "B5ZC00", "P07204_TRBM_HUMAN", 
            "P20840_SAG1_YEAST", "Q8ER84", "P07987_GUX2_TRIRE"
        ]

    # Procesamiento
    finder = ProteinMotifFinder()
    results = {}
    
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {
            executor.submit(finder.process_single_protein, pid): pid 
            for pid in uniprot_ids
        }
        
        for future in as_completed(futures):
            if result := future.result():
                results.update(result)
                print(f"✔ {list(result.keys())[0]}: {len(result[list(result.keys())[0]])} motivos")

    # Resultados finales
    print(f"\n📊 Resumen: {len(results)}/{len(uniprot_ids)} proteínas con motivos")
    save_results(output_file, results)

if __name__ == "__main__":
    main()