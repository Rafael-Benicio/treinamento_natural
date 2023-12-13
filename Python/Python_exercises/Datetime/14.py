# Write a Python program to find the date of the first Monday of a given week.
# Sample Year and week : 2015, 50
# Expected Output : Mon Dec 14 00:00:00 2015

from datetime import datetime,datetime

DATE='2015, 50'

def main():
	monday_of_week=datetime.strptime(DATE+' 1','%Y, %W %w')

	print(monday_of_week.strftime('%a %b %d %H:%M:%S %Y'))

if __name__ == '__main__':
	main()