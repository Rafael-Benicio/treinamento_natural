# Write a Python program to convert the date to datetime (midnight of the date) in Python.
# Sample Output : 2015-06-22 00:00:00
from datetime import datetime

DATE='13/12/2023'

def main():
	date_object=datetime.strptime(DATE,'%d/%m/%Y')
	print(date_object)

if __name__ == '__main__':
	main()