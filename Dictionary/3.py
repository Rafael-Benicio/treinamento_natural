dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

# Fazendo o uso do operdor de União

dic4=dic1|dic2|dic3

print(dic4)

# -------------------------------------
# dic4={}

# for i in (dic1,dic2,dic3):
#      dic4.update(i)

# print(dic4)

# Tarefa : Concatena os dicinarios 1,2 e 3 e criar um novo

# Aqui foi um ponto, visto que essa questão me pegou pelo fato de que nunca ter chegado a ter que trabalhar com essa coisa de concatenar listas, o que me levou a tomar conhecimento do metodo 'update()', que seguindo a logica de Python, torna esse processo muito tranquilo
