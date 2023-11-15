import heapq
from collections import defaultdict, Counter

class Nodo:
    def __init__(self, caracter, frecuencia):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia

def construir_arbol_huffman(datos):
    frecuencia_caracter = Counter(datos)
    cola_prioridad = [Nodo(caracter, frecuencia) for caracter, frecuencia in frecuencia_caracter.items()]
    heapq.heapify(cola_prioridad)

    while len(cola_prioridad) > 1:
        nodo_izquierdo = heapq.heappop(cola_prioridad)
        nodo_derecho = heapq.heappop(cola_prioridad)

        nodo_combinado = Nodo(None, nodo_izquierdo.frecuencia + nodo_derecho.frecuencia)
        nodo_combinado.izquierda = nodo_izquierdo
        nodo_combinado.derecha = nodo_derecho

        heapq.heappush(cola_prioridad, nodo_combinado)

    return cola_prioridad[0]

def construir_codigos_huffman(nodo, codigo_actual="", codigos={}):
    if nodo is None:
        return

    if nodo.caracter:
        codigos[nodo.caracter] = codigo_actual

    construir_codigos_huffman(nodo.izquierda, codigo_actual + "0", codigos)
    construir_codigos_huffman(nodo.derecha, codigo_actual + "1", codigos)

    return codigos

def codificar_huffman(datos):
    if not datos:
        raise ValueError("Los datos de entrada están vacíos.")

    raiz_arbol = construir_arbol_huffman(datos)
    codigos = construir_codigos_huffman(raiz_arbol)

    datos_codificados = "".join(codigos[caracter] for caracter in datos)
    return datos_codificados, raiz_arbol

def decodificar_huffman(datos_codificados, raiz_arbol):
    datos_decodificados = ""
    nodo_actual = raiz_arbol

    for bit in datos_codificados:
        if bit == "0":
            nodo_actual = nodo_actual.izquierda
        else:
            nodo_actual = nodo_actual.derecha

        if nodo_actual.caracter:
            datos_decodificados += nodo_actual.caracter
            nodo_actual = raiz_arbol

    return datos_decodificados

# Ejemplo de uso:
if __name__ == "__main__":
    datos = "este_es_un_ejemplo_de_arbol_de_huffman"
    
    datos_codificados, raiz_arbol = codificar_huffman(datos)
    print("Datos codificados:", datos_codificados)
    
    datos_decodificados = decodificar_huffman(datos_codificados, raiz_arbol)
    print("Datos decodificados:", datos_decodificados)