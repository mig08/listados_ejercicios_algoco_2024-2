from collections import deque


numero_casos = int(input())

results = deque()

for x in range(numero_casos):

    entrada = input()
    

    numero_lista = int(input())
    

    if numero_lista > 0:
        lst = list(map(int, input()[1:-1].split(',')))
    else:
        lst = input()
        lst = []
    

    deq = deque(lst)
    error = False
 

    for instruccion in entrada:
        if instruccion == 'R':
            deq.reverse()

        elif instruccion == 'D':
            if not deq:
                error = True
                break
            deq.popleft()
    


    if error:
        results.append("error")
    else:
        results.append('[' + ','.join(map(str, deq)) + ']')



print("\n".join(results))
