# Write a Python program to calculate an age in years.

from datetime import date,datetime 

BORN_DATE=date(2001,10,5)

def calculate_age(born_date:date) -> int():
	today_date=datetime.today()
	age=today_date.year-born_date.year
	if (today_date.month,today_date.day)<(born_date.month,born_date.day):
		age-=1
	return age

if __name__ == '__main__':	
	print(calculate_age(BORN_DATE))