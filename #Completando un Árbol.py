#Completando un Árbol

import os
from collections import defaultdict

def main():
    # Configuración de rutas (ajusta según tu sistema)
    os.chdir(r"C:\Users\gabri\Documents\SCRIPTS_ESTUDIO_PYTHON\archivos descargados python village")
    input_file = 'rosalind_tree.txt'
    output_file = 'resultado_tree.txt'
    
    try:
        with open(input_file, 'r') as f:
            lines = f.readlines()
            n = int(lines[0].strip())
            edges = [tuple(map(int, line.strip().split())) for line in lines[1:]]
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {input_file}")
        return
    except (IndexError, ValueError):
        print("Error: El formato del archivo debe ser:\n<n>\n<edge1>\n<edge2>\n...")
        return
    
    # Construir el grafo como lista de adyacencia
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Contar componentes conectados usando BFS
    visited = set()
    components = 0
    
    for node in range(1, n+1):
        if node not in visited:
            components += 1
            queue = [node]
            visited.add(node)
            
            while queue:
                current = queue.pop(0)
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
    
    # El mínimo número de aristas necesarias es (componentes - 1)
    result = components - 1
    
    # Guardar resultado
    with open(output_file, 'w') as f:
        f.write(f"{result}\n")
    
    print(f"Número mínimo de aristas necesarias: {result}")
    print(f"Resultado guardado en: {os.path.abspath(output_file)}")

if __name__ == "__main__":
    main()