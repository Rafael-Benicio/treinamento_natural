# Write a Python program to get days between two dates.
# Sample Dates : 2000,2,28, 2001,2,28
# Expected Output : 366 days, 0:00:00

from datetime import datetime


def main():
	date_1=datetime(2000,2,28)
	date_2=datetime(2001,2,28)

	diff_between_dates = date_2 - date_1

	print(diff_between_dates)


if __name__ == '__main__':
	main()