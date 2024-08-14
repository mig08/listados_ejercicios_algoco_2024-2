numeros_iniciales = input()
comandos = input()

comandos_separados = []
numeros_iniciales = numeros_iniciales.split()

print(numeros_iniciales)

cant_estudiantes = int(numeros_iniciales[0])
cant_comandos = int(numeros_iniciales[1])


comandos_separados = comandos.split()
comandos_separados_real = []

print(comandos_separados)

cont = 0
for x in comandos_separados:

    if x == " ":
        cont += 1

    elif x != "undo":
        comandos_separados_real.append(int(x))
        cont += 1
    
    else:
        comandos_separados_real.append(x+ " "+comandos_separados[cont+1])
        comandos_separados[cont+1] = " "
        cont += 1

print(comandos_separados_real)

fila_estudiantes = []

cont_2 = 0

while cont_2 < cant_estudiantes:

    fila_estudiantes.append(cont_2)
    cont_2 += 1

print(fila_estudiantes)

huevo = 0

for x in comandos_separados_real:
    if x is not str:
        huevo += x % cant_estudiantes
    else:
        
        








