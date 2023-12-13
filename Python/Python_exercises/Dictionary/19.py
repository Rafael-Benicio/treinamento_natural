from collections import Counter

dict_1 = {'a': 100, 'b': 200, 'c':300}
dict_2 = {'a': 300, 'b': 200, 'd':400}

# Usando Counter

dict_3=Counter(dict_1)+Counter(dict_2)

print(dict_3)

# --------------------------------------
# dict_3=dict_1.copy()
# dict_3.update(dict_2)

# for key in dict_1:
#      if key in dict_2:
#           dict_3[key] = dict_2[key] + dict_1[key]

# print(dict_3)

# Tarefa : Combinar dois dicionarios e somar os valores que eles tem chaves em comum

# O ponto aqui fica mais na questão da resulução oferecida pelo site, que usa o Counter, que realmente simplifica o processo em relação ao que eu fiz e vale dar uma estudada sobre