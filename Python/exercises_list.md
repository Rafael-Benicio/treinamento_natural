# Exercícios 

### Exercícios Basicos
 
[**Exercicio 3**](./Python_exercises/Basic/3.py) : Escreva um programa Python para mostrar a data e hora atual

Exemplo de saida :
~~~
2014-07-05 14:34:14
~~~
---
[**Exercicio 6**](./Python_exercises/Basic/6.py)  : Escreva um programa Python que aceita uma sequancia de numeros separados por virgulas e gera uma lista e uma tupla apartir desses numeros

Exemplo de Entrada : 
~~~
3, 5, 7, 23
~~~
Saida :
~~~
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
~~~
---
[**Exercicio 14**](./Python_exercises/Basic/14.py): Escreva um programa Python para calcular o numero de dias entre duas datas

Exemplo de datas : 
~~~
(2014, 7, 2), (2014, 7, 11)
~~~
Saida : 
~~~
9 days
~~~
---
[**Exercicio 25**](./Python_exercises/Basic/25.py): Escreva um programa Python que checa se um valor especificado está contido dentro de um grupo de valores

Dados :
~~~
3  ->[1, 5, 8, 3]
-1 ->[1, 5, 8, 3]
~~~

Saida :
~~~
True
False
~~~
---
[**Exercicio 27**](./Python_exercises/Basic/27.py): Escreva um programa Python que concatena todos os elementos de uma lista dentro de uma string e retorna ela

Dado :
~~~
[1,5,1,2,2]
~~~
Saida :
~~~
15122
~~~
---
[**Exercicio 28**](./Python_exercises/Basic/28.py): Escreva um programa Python que emprime todos os valores pares de uma dada lista na lista e para a impressão depois de imprimir o valor 237 na sequencia

Exemplo de lista de numeros :
~~~
numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]
~~~

Saida :
~~~
386                                                                                                        
462                                                                                                        
418                                                                                                        
344                                                                                                        
236                                                                                                        
566                                                                                                        
978                                                                                                        
328                                                                                                        
162                                                                                                        
758                                                                                                        
918  
237 
~~~
---
[**Exercicio 29**](./Python_exercises/Basic/29.py): Escreva um programa Python que imprime todas as cores da ´´´color_list_1´´´ que não estão presente na ´´´color_list_2´´´

Dados de Teste :
~~~
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
~~~
Saida esperada :
~~~
{'Black', 'White'}
~~~
---
[**Exercicio 73**](./Python_exercises/Basic/73.py): Escreve um programa Python para calcular um ponto médio de uma linha

---
[**Exercicio 75**](./Python_exercises/Basic/75.py): Escreva um programa Python para obter as informações de copyright no codigo Python

---
[**Exercicio 90**](./Python_exercises/Basic/90.py): Escreva um programa Python para que faz uma copia do proprio código

### Exercícios Dicionário

[**Exercicio 3**](./Python_exercises/Dictionary/3.py): Escreva um script Python que concatene os dicionarios a seguir e crie um novo

Dicionários :
~~~
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
~~~

Resultado Esperado : 
~~~
{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
~~~
---
[**Exercicio 7**](./Python_exercises/Dictionary/7.py): Escreva um script Python para imprimir um dicionário, onde as chaves são numeros entre 1 e 15 (ambos inclusos) e os valores são o quadrado da chave

Exemplo de Saida :
~~~
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
~~~

---
[**Exercicio 19**](./Python_exercises/Dictionary/19.py): Escreva um programa que combine dois dicionários e some os valores que tem chaves em comum

Dados :
~~~
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
~~~

Saida : 
~~~
Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
~~~
---
[**Exercicio 20**](./Python_exercises/Dictionary/20.py): Escreva um programa que imprime todos os valores distintos no dicionário:

Dados :
~~~
[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
~~~
Saida esperada :
~~~
{'S005', 'S002', 'S007', 'S001', 'S009'}
~~~
---
[**Exercicio 30**](./Python_exercises/Dictionary/30.py): Escreva um programa para pegar os três maiores valores de itens numa loja

Dados :
~~~
{'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
~~~
Saida :
~~~
item4 55
item1 45.5
item3 41.3
~~~
---
[**Exercicio 38**](./Python_exercises/Dictionary/38.py): Escreva um programa que compara os valores das chaves em dois dicionários

Dados : 
~~~
{'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
~~~
Saida : 
~~~
key1: 1 está presente  em  dict_1 e dict_2
~~~
---
[**Exercicio 46**](./Python_exercises/Dictionary/46.py): Escreva um programa para criar um dicionário que agrupe as sequências de pares chave-valor em um dicionario de listas:

Lista Original:
~~~
[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
~~~
Saida Esperada:
~~~
{'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}
~~~
---