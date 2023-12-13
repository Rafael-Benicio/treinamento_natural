# Write a Python program to subtract five days from the current date.
# Current Date : 2015-06-22
# 5 days before Current Date : 2015-06-17
from datetime import datetime,timedelta

def main():
	current_date=datetime.now()
	date_variation=current_date - timedelta(days=5)

	print(f'Data atual : {current_date.strftime("%Y-%m-%d")}')
	print(f'Data atual - 5 dias : {date_variation.strftime("%Y-%m-%d")}')


if __name__ == '__main__':
	main()