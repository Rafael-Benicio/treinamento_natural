# Write a Python program to get a list of dates between two dates.

from datetime import timedelta, date

DATE_1=date(2010,1,2)
DATE_2=date(2010,2,2)

def list_of_dates_between_two_dates(first_date:date,final_date:date) -> list[date]:
     diff_of_days=(final_date+timedelta(days=1))-first_date
     return [first_date+timedelta(days=day) for day in range(diff_of_days.days)]


if __name__=="__main__":
     for date_item in list_of_dates_between_two_dates(DATE_1,DATE_2):
          print(date_item)