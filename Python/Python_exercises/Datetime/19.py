# Write a Python program to get the date of the last Tuesday.


from datetime import datetime,timedelta

def main():
	current_day=datetime.today()
	days_diff = (current_day.weekday()-1)%7 
	lst_tuesday = current_day - timedelta(days=days_diff)
	print(lst_tuesday)

	
if __name__ == '__main__':
	main()