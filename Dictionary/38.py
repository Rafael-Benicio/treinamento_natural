list_dicts = [
     {'valor_1': 70, 'valor_2': 82},
     {'valor_1': 73, 'valor_2': 74},
     {'valor_1': 75, 'valor_2': 86}
]

for dict in list_dicts:
     value_v = dict.pop('valor_1')
     value_vi = dict.pop('valor_2')
     dict['Final'] = (value_v + value_vi) / 2

print(list_dicts) 

# Tarefa : Pegar a lista contendo dicinoarios e tirar a media de dois valores dentro dele

