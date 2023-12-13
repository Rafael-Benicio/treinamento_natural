import math
import functools 
from datetime import date

date_1=(2014, 7, 2)
date_2=(2014, 7, 5)

# Usando datetime

days_dif = date(2014, 7, 5) - date(2014, 7, 2)

print(f'{days_dif.days} days')

# Aqui basicamente checa se a dt2 é posterior a dt1
# def check_dt(date_1,date_2):
#      if date_1[0]>date_2[0] or date_1[0]==date_2[0] and date_1[1]>date_2[1] or date_1[0]==date_2[0] and date_1[1]<=date_2[1] and date_1[2]>date_2[2]:
#           print("Não é possivel")
#           exit()

# def diff_days(date_1,date_2):
#      n_days=0
#      YEAR=365
#      # Quantos dias tem cada mês
#      MONTH=[31,28,31,30,31,30,31,31,30,31,30,31]
#      # Calcular a diferença entre os dias
#      if date_1[2]<=date_2[2]:
#           n_days+=date_2[2]-date_1[2]
#      elif date_1[2]>date_2[2]:
#           date_1_mes=MONTH[date_1[1]-1]-date_1[2]
#           n_days+=date_1_mes+date_2[2]
#      # Calcular a diferença em dias dos meses
#      if date_1[1]<=date_2[1] and date_1[2]<=date_2[2]:
#           n_days+=functools.reduce(lambda x, y: x + y, MONTH[(date_1[1]-1):(date_2[1]-1)],0)
#      elif date_1[1]>date_2[1]:
#           n_days+=YEAR-functools.reduce(lambda x, y: x + y, MONTH[(date_2[1]-1):(date_1[1]-1)],0)
#      # Calcular a diferença em dias dos YEARs
#      if date_1[0]>date_2[0] and date_1[1]>date_2[1] or date_1[0]>date_2[0] and date_1[2]>date_2[2]:
#           n_days+=((date_2[0]-1)-date_1[0])*YEAR
#           print(n_days)
#      elif date_1[0]<=date_2[0]:
#           n_days+=(date_2[0]-date_1[0])*YEAR
     
#      return n_days
     
# check_dt(date_1,date_2)
# print(diff_days(date_1,date_2))

# Tarefa : diferença de dias entre datas

# Isso ficou desecessariamente grande, diferente do execicio três, não passou aqui pela minha cabeça que a bibliote 'datetime' deveria ter um metodo pra lidar com esse processo

# Dado isso, eu gastei mais tempo aqui do que com qualquer outra questão, produzi um codigo grande, ruim de ler, e que concerteza tem problemas que a implementação da biblioteca não tem
