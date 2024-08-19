# Leer todas las palabras de la entrada estándar
words = []
try:
    while True:
        line = input().strip()
        if line:
            words.extend(line.split())
except EOFError:
    pass

# Crear un conjunto para almacenar palabras compuestas únicas
compound_words = set()

# Crear todas las combinaciones posibles de palabras compuestas
word_set = set(words)  # Convertimos a set para búsqueda más rápida
for word1 in words:
    for word2 in word_set:
        if word1 != word2:
            compound_words.add(word1 + word2)

# Imprimir las palabras compuestas en orden alfabético
print("\n".join(sorted(compound_words)))
