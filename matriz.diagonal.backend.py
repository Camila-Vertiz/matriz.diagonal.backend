import os

def diagonalDifference(arr):
    suma_diagonal_izquierda = 0
    suma_diagonal_derecha = 0
    
    n = len(arr)  # Tamaño de la matriz (n x n)
    
    for i in range(n):
        suma_diagonal_izquierda += arr[i][i]          # Elementos de la diagonal izquierda a derecha
        suma_diagonal_derecha += arr[i][n - 1 - i]    # Elementos de la diagonal derecha a izquierda
    
    # Calculamos la diferencia absoluta entre las sumas de las diagonales
    return abs(suma_diagonal_izquierda - suma_diagonal_derecha)


def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))

    input_file = os.path.join(current_dir, 'problema_02_input.txt')
    output_file = os.path.join(current_dir, 'output.txt')

    try:
        with open(input_file, 'r') as br:
            with open(output_file, 'w') as fw:
                for line in br:
                     # Limpiar la línea y dividirla por ';' para separar las filas
                    matrices_str = line.strip().split(';')
                    
                    # Filtrar filas vacías
                    matrices_str = [fila for fila in matrices_str if fila.strip()]
                    
                    # Convertir cada fila de la matriz en una lista de enteros, validando que no haya valores vacíos
                    try:
                        arr = [list(map(int, fila.split(','))) for fila in matrices_str]
                    except ValueError as ve:
                        print(f"Error al procesar la fila. Error: {ve}")
                        continue
                    
                    # Calcular la diferencia de las diagonales
                    diferencia = diagonalDifference(arr)
                    
                    # Escribir el resultado en el archivo de salida
                    fw.write(f"{diferencia}\n")
                    
    except FileNotFoundError as e:
        print(f"Archivo no encontrado: {e}")
    except IOError as e:
        print(f"Error de E/S: {e}")

if __name__ == "__main__":
    main()