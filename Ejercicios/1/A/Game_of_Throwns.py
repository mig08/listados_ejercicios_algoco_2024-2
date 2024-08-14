numeros_iniciales = input()
comandos = input()

comandos_separados = []
numeros_iniciales = numeros_iniciales.split()

#print(numeros_iniciales)

cant_estudiantes = int(numeros_iniciales[0])
cant_comandos = int(numeros_iniciales[1])


comandos_separados = comandos.split()
comandos_separados_real = []

#print(comandos_separados)

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

#print(comandos_separados_real)

fila_estudiantes = []

cont_2 = 0

while cont_2 < cant_estudiantes:

    fila_estudiantes.append(cont_2)
    cont_2 += 1

#print(fila_estudiantes)

huevo = 0
comandos_usados = []

for x in comandos_separados_real:
    if isinstance(x, int):
        #print("Se suma:", x % cant_estudiantes)
        huevo += (x % cant_estudiantes)
        comandos_usados.append(x)
    else:
        cont = 0
        undo = x.split()
        cant_undo = int(undo[1])
        while cont < cant_undo:
            comando_anterior = comandos_usados.pop()
            huevo -= (comando_anterior % cant_estudiantes)
            cont += 1

if huevo < cant_estudiantes:
    print(fila_estudiantes[huevo])
else:
    posi_huevo = huevo % cant_estudiantes
    print(fila_estudiantes[posi_huevo])
        
        








