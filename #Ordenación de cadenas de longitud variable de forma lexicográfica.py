# Ordenación de cadenas de longitud variable de forma lexicográfica

import os
from pathlib import Path

def generar_cadenas_prefijo(alfabeto, n, prefijo="", resultado=None):
    """Genera cadenas explorando completamente cada prefijo antes de pasar al siguiente"""
    if resultado is None:
        resultado = []
    if len(prefijo) > 0:
        resultado.append(prefijo)
    if len(prefijo) < n:
        for letra in alfabeto:
            generar_cadenas_prefijo(alfabeto, n, prefijo + letra, resultado)
    return resultado

def main():
    # Configuración de directorios
    directorio = Path(r"C:\Users\gabri\Documents\SCRIPTS_ESTUDIO_PYTHON\archivos descargados python village")
    archivo_entrada = directorio / "rosalind_lexv.txt"
    archivo_salida = directorio / "resultado_lexv.txt"
    
    directorio.mkdir(parents=True, exist_ok=True)
    
    try:
        # Leer archivo de entrada
        with open(archivo_entrada, 'r') as f:
            lineas = [linea.strip() for linea in f if linea.strip()]
            alfabeto = lineas[0].split()
            n = int(lineas[1])
        
        # Validación
        if not alfabeto:
            raise ValueError("El alfabeto no puede estar vacío")
        if n < 1:
            raise ValueError("n debe ser al menos 1")
        
        # Generar cadenas con el orden de prefijo completo
        resultados = generar_cadenas_prefijo(alfabeto, n)
        
        # Escribir resultados
        with open(archivo_salida, 'w') as f:
            f.write('\n'.join(resultados) + '\n')
        
        print("\n✅ Resultados generados correctamente:")
        print(f"Primeras 10 cadenas: {resultados[:10]}")
        print(f"Últimas 10 cadenas: {resultados[-10:]}")
        print(f"Total de cadenas: {len(resultados)}")
        print(f"Archivo guardado en: {archivo_salida}")
    
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        return

if __name__ == "__main__":
    main()