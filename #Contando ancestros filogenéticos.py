#Contando ancestros filogenéticos
# Contando Ancestros Filogenéticos - Solución Final
import os
from pathlib import Path

def calcular_nodos_internos(n_hojas):
    """
    Calcula el número de nodos internos en un árbol binario no enraizado.
    Fórmula: nodos_internos = n_hojas - 2
    """
    if not 3 <= n_hojas <= 10000:
        raise ValueError("El número de hojas debe estar entre 3 y 10000")
    return n_hojas - 2

def main():
    # Configuración de directorios (ajustar según necesidad)
    DIR_BASE = Path(r"C:\Users\gabri\Documents\SCRIPTS_ESTUDIO_PYTHON\archivos descargados python village")
    DIR_BASE.mkdir(exist_ok=True)  # Crea el directorio si no existe
    
    ARCHIVO_ENTRADA = DIR_BASE / "rosalind_inod.txt"
    ARCHIVO_SALIDA = DIR_BASE / "resultado_inod.txt"
    
    # Manejo de archivo de entrada
    try:
        with open(ARCHIVO_ENTRADA, 'r') as f:
            n = int(f.read().strip())
    except FileNotFoundError:
        print(f"⚠️ Archivo de entrada no encontrado. Creando archivo de ejemplo...")
        with open(ARCHIVO_ENTRADA, 'w') as f:
            f.write("4")  # Valor de ejemplo del problema
        n = 4
    except ValueError:
        print("❌ Error: El archivo debe contener solo un número entero")
        return
    
    # Cálculo y guardado de resultados
    try:
        resultado = calcular_nodos_internos(n)
        
        with open(ARCHIVO_SALIDA, 'w') as f:
            f.write(f"{resultado}\n")
        
        # Mostrar resumen de ejecución
        print("\n" + "═"*50)
        print(f"🔹 Número de hojas leído: {n}")
        print(f"🔹 Nodos internos calculados: {resultado}")
        print(f"🔹 Archivo de salida generado: {ARCHIVO_SALIDA}")
        print("═"*50 + "\n")
        
    except ValueError as e:
        print(f"❌ Error: {e}")
        return

if __name__ == "__main__":
    main()