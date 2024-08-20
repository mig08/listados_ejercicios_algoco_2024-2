from collections import deque
import sys
input = sys.stdin.read

def process_case(program, lst):
    deq = deque(lst)
    error = False
    reverse_flag = False
    
    for command in program:
        if command == 'R':
            reverse_flag = not reverse_flag
        elif command == 'D':
            if not deq:
                error = True
                break
            if reverse_flag:
                deq.pop()  # Elimina del final si está en modo reverso
            else:
                deq.popleft()  # Elimina del principio si está en modo normal
    
    if reverse_flag:
        deq.reverse()  # Solo hacer una reversión al final si es necesario
    
    return deq, error

def main():
    data = input().splitlines()
    index = 0
    t = int(data[index])
    index += 1
    
    results = deque()  # Usar deque para resultados también, aunque en este caso no es tan necesario
    
    for _ in range(t):
        program = data[index]
        index += 1
        n = int(data[index])
        index += 1
        
        if n > 0:
            lst = list(map(int, data[index][1:-1].split(',')))
        else:
            lst = []
        index += 1
        
        result_list, error = process_case(program, lst)
        
        if error:
            results.append("error")
        else:
            results.append(f"[{','.join(map(str, result_list))}]")
    
    print("\n".join(results))

if __name__ == "__main__":
    main()

