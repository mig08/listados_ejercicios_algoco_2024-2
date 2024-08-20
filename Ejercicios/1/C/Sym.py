from collections import deque

def procesar_simulacion_editor_texto(caso_de_prueba):
    pila_izquierda = deque()  # Caracteres a la izquierda del cursor
    pila_derecha = deque()  # Caracteres a la derecha del cursor
    for char in caso_de_prueba:
        if char == '[':  # Mover cursor al inicio
            pila_derecha.extendleft(reversed(pila_izquierda))
            pila_izquierda.clear()
        elif char == ']':  # Mover cursor al final
            pila_izquierda.extend(pila_derecha)
            pila_derecha.clear()
        elif char == '<':  # Retroceso (Backspace)
            if pila_izquierda:
                pila_izquierda.pop()
        else:  # Carácter regular
            pila_izquierda.append(char)

    # Combinar las pilas izquierda y derecha para obtener la cadena final
    return ''.join(pila_izquierda) + ''.join(pila_derecha)


cantidad_casos = int(input())

for _ in range(cantidad_casos):
    linea = input()
    resultado = procesar_simulacion_editor_texto(linea)
    print(resultado)



