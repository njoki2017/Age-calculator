from datetime import date
import calendar
AGE = int(input('enter your age: '))
YEAR = int(input('enter the current year: '))
DOB= int(input('date of birth(1-31): ')) 
month = int(input('month(1-12): '))
current_date = 18,5
if DOB >18  and month > 5:
    b = YEAR - AGE - 1
else:
    b = YEAR - AGE
birthday = date(b,month,DOB)
print(birthday.strftime('you were born on %d %A %b %Y'))
input('end of the program')
