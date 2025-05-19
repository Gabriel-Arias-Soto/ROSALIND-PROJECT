# Solution to Fibonacci-like Rabbit Population Problem

import os

# Cambiar al directorio donde está el archivo
os.chdir(r"C:\Users\gabri\Documents\SCRIPTS_ESTUDIO_PYTHON\archivos descargados python village")

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