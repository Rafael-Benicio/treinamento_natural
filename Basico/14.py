import math
import functools 

d1=(2014, 7, 2)
d2=(2014, 7, 2)

# Aqui basicamente checa se a dt2 é posterior a dt1
def check_dt(d1,d2):
     if d1[0]>d2[0] or d1[0]==d2[0] and d1[1]>d2[1] or d1[0]==d2[0] and d1[1]<=d2[1] and d1[2]>d2[2]:
          print("Não é possivel")
          exit()

def diff_days(d1,d2):
     n_dias=0
     ANO=365
     # Quantos dias tem cada mês
     MES=[31,28,31,30,31,30,31,31,30,31,30,31]
     # Calcular a diferença entre os dias
     if d1[2]<=d2[2]:
          n_dias+=d2[2]-d1[2]
     elif d1[2]>d2[2]:
          d1_mes=MES[d1[1]-1]-d1[2]
          n_dias+=d1_mes+d2[2]
     # Calcular a diferença em dias dos meses
     if d1[1]<=d2[1] and d1[2]<=d2[2]:
          n_dias+=functools.reduce(lambda x, y: x + y, MES[(d1[1]-1):(d2[1]-1)],0)
     elif d1[1]>d2[1]:
          n_dias+=ANO-functools.reduce(lambda x, y: x + y, MES[(d2[1]-1):(d1[1]-1)],0)
     # Calcular a diferença em dias dos anos
     if d1[0]>d2[0] and d1[1]>d2[1] or d1[0]>d2[0] and d1[2]>d2[2]:
          n_dias+=((d2[0]-1)-d1[0])*ANO
          print(n_dias)
     elif d1[0]<=d2[0]:
          n_dias+=(d2[0]-d1[0])*ANO
     
     return n_dias
     
check_dt(d1,d2)
print(diff_days(d1,d2))

# Tarefa : diferença de dias entre datas

# Isso ficou desecessariamente grande, diferente do execicio três, não passou aqui pela minha cabeça que a bibliote 'datetime' deveria ter um metodo pra lidar com esse processo

# Dado isso, eu gastei mais tempo aqui do que com qualquer outra questão, produzi um codigo grande, ruim de ler, e que concerteza tem problemas que a implementação da biblioteca não tem
