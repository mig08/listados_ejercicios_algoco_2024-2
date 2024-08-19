primer_input = input()
primer_input = primer_input.split() 

cant_obs = int(primer_input[0])
obs_contados = int(primer_input[1])

obs_encontrados = []

cont= 0
while cont < obs_contados:
    obs = input()
    obs_encontrados.append(int(obs))
    cont += 1

cont = 0
cant_obs_encontrados = 0
while cont < cant_obs:
    if cont not in obs_encontrados:
            print(cont)
            cont += 1
    else:
         cont += 1
         cant_obs_encontrados += 1

print("Mario got", cant_obs_encontrados, "of the dangerous obstacles.")