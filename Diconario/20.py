lis=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

out=set()

for i in lis:
     out.add(list(i.values())[0])
print(out)

# Tarefa : Obter uma lista não repetida dos valores nos dicionarios dentro da lista

# A dificuldade aqui ficou no fato de ter que obter os valores dentro dos dicionarios da lista, não porque seja dificil, mas porque adiciona pelo menos na minha visão, uma camada inconveniente ao processo, que seria um for aninhado

# A resolução do site vai por essa via, mas eu optei por, partindo do ponto que eu só queria o primeiro valor dos dicionarios, eu poderia jogar o resto fora