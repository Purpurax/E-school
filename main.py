import subprocess, os, datetime

def cac(x, y):
    x *= 60
    return (x + y)

def CheckHoliday(x, y, _y, z, _z): #year, month, monthEnd, day, dayEnd
    days = (datetime.date(x, y, z) - datetime.date.today()).days
    _days = (datetime.date(x, _y, _z) - datetime.date.today()).days
    if(days <= 0 and _days >= 0):
        return True
    else:
        return False

def Holiday(): #manually typed holidays
    if(CheckHoliday(2021, 3, 4, 31, 11)):
        return True
    elif(CheckHoliday(2021, 5, 5, 13, 14)):
        return True
    elif(CheckHoliday(2021, 5, 6, 24, 4)):
        return True
    elif(CheckHoliday(2021, 7, 9, 29, 11)):
        return True
    else:
        return False
if(datetime.date.today().weekday() >= 5 or Holiday() == True):
    if(datetime.datetime.now().hour <= 10):
        print('Weekend Starting')
        #playing music through other scripts
elif(datetime.date.today().weekday() <= 4):
    print('School starting')
    #playing music through other scripts
    subprocess.run('python school.py')
