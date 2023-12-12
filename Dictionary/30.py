from heapq import nlargest
from operator import itemgetter

items={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}

for name, value in nlargest(3, items.items(), key=itemgetter(1)):
    print(name, value) 

# Tarefa : Fazer a impressão de 3 itens de uma lista, sendo que esses items são os com as maiores chaves

# o metodo nlargest aqui faz o trabalho de ordenação do maior para o menor sendo limitado pelo seu primeiro parametro
# Depois tem o usa segundo paramelhor que cria um dicionario de itens, visto que o metodo nlarger não convsegue lidar diretamente com um dicinario
# Por fim o metodo itemgetter(1), serve pra apontar qual dado do para (chave , valor ) está sendo usado pra ordenar os valores em questão

