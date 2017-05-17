import calendar

def getAge(currentAge,month,day):
    import datetime
    now = datetime.datetime.now()
    now = now.strftime("%Y")
    year = int(now) - int(currentAge)
    years = int(year)

    if int(month) in range(1, 13) and int(day) in range(1, 32):
     birthDate =  str(ordinal) + " " + str(month_name) + "," + str(year)
     print("Your birthday is :" + birthDate + '.')
    else:
     return "Please Enter Valid Day Or Month"

    return years


months = [

		'January',
		'February',
		'March',
		'April',
		'May',
		'June',
		'July',
		'August',
		'September',
		'October',
		'November',
		'December',
	]
endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
			  + ['st', 'nd', 'rd'] + 7 * ['th'] \
			  + ['st']

currentAge = input('Enter your Age:')
month = input('Enter your Month of birth:')
day = input('Enter your Date of birth:')
print("")

month_number = int(month)
month_name = months[month_number - 1]

day_number = int(day)
ordinal = day + endings[day_number - 1]

real_date = calendar.weekday(getAge(currentAge,month,day), month_number, day_number)
if(real_date == 0):
        a ="You were born on a Monday."
        print(a)
if(real_date == 1):
        a = "You were born on a Tuesday."
        print(a)
if(real_date == 2):
        a = "You were born on a Wednesday."
        print(a)

if(real_date == 3):
        a = "You were born on a Thursday."
        print(a)
if(real_date == 4):
        a = "You were born on a Friday."
        print(a)
if(real_date == 5):
        a = "You were born on a Saturday."
        print(a)

if(real_date == 6):
        a = "You were born on a Sunday."
        print(a)






