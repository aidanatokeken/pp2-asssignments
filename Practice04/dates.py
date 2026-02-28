#1
import datetime
today = datetime.date.today()
print(today)

#2
from datetime import date
my_date = date(2025, 12, 25)
print(my_date)

#3
from datetime import date
d = date(2025, 12, 25)
print(d.year)
print(d.month)
print(d.day)

#4
from datetime import date
d1 = date(2025, 1, 1)
d2 = date(2024, 12, 31)
print(d1 > d2)

#5
from datetime import date
today = date.today()
print(today.strftime("%d/%m/%Y"))