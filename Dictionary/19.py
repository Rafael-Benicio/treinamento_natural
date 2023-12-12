d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

d3=d1.copy()
d3.update(d2)

for i in d1:
     if i in d2:
          d3[i]=d2[i]+d1[i]

print(d3)

# Tarefa : Combinar dois dicionarios e somar os valores que eles tem chaves em comum

# O ponto aqui fica mais na questão da resulução oferecida pelo site, que usa o Counter, que realmente simplifica o processo em relação ao que eu fiz e vale dar uma estudada sobre