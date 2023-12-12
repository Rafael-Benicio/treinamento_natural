colors_and_values=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

colors_dict={pair[0]:[] for pair in colors_and_values}

for pair in colors_and_values:
     colors_dict[pair[0]].append(pair[1])

print(colors_dict)

# Tarefa : Agrupar os valores que fazem par com as cores em um dicinario na logica {'cor':[valores]}

