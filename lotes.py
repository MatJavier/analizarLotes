# Definir una función para analizar las combinaciones
def analizar_combinaciones(lote):
    # Separar el lote en combinaciones individuales
    combinaciones = lote.split()
    
    # Crear un diccionario para almacenar la frecuencia de cada combinación
    frecuencia_combinaciones = {}
    
    # Recorrer todas las combinaciones
    for combinacion in combinaciones:
        # Crear una lista de números a partir de la cadena de la combinación
        numeros = list(map(int, combinacion.split("-")))
        
        # Ordenar la lista de números
        numeros_ordenados = sorted(numeros)
        
        # Convertir la lista ordenada de números en una cadena para poder almacenarla en el diccionario
        combinacion_ordenada = "-".join(list(map(str, numeros_ordenados)))
        
        # Actualizar la frecuencia de la combinación ordenada en el diccionario
        if combinacion_ordenada in frecuencia_combinaciones:
            frecuencia_combinaciones[combinacion_ordenada] += 1
        else:
            frecuencia_combinaciones[combinacion_ordenada] = 1
    
    # Imprimir los resultados
    print("Combinaciones analizadas:", len(combinaciones))
    print("Combinaciones repetidas:")
    for combinacion, frecuencia in frecuencia_combinaciones.items():
        if frecuencia > 1:
            print(combinacion, ":", frecuencia, "veces")


# Ejemplo de uso de la función
lote = "01-05-08-07-20-26-36 02-11-09-13-20-26-38 01-05-08-07-23-26-36 03-11-09-13-20-26-38"
analizar_combinaciones(lote)
