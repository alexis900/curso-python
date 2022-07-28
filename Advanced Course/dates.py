from datetime import datetime

my_time = datetime.now()
my_day = datetime.today()

print(my_time)
print(my_day)

print(f'Year: {my_day.year}')
print(f'Month: {my_day.month}')
print(f'Day: {my_day.day}')

my_str = my_time.strftime('Formato España: %d/%m/%Y')
print(my_str)

my_str = my_time.strftime('Formato EEUU: %m/%d/%Y')
print(my_str)