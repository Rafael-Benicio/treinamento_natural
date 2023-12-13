# Write a Python program to convert a string to datetime.

from datetime import datetime

# %b → mês abreviado
# %Y → ano
# %d → Dia
# %I → Hora para relogio de 12
# %M → Minutos
# %p → AM ou PM

def main():
	converted_datetime_string = datetime.strptime('Jan 1 2010 7:46PM', '%b %d %Y %I:%M%p')

	print(converted_datetime_string)


if __name__=='__main__':	
	main()