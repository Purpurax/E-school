from datetime import date
import pyautogui, time, subprocess, os, datetime, playsound, wmi

p = pyautogui

updatingAnimation = [
    '[.  ]     ',
    '[.. ]     ',
    '[...]     '
]

updatingFrame = 0
sleepTime = 60
subjectIndex = 0
music = False

def OpenPage(url):
    playsound.playsound('C:/1/PROJECTS/Sound/message-loud.mp3')
    time.sleep(5)
    p.moveRel(0, -50)
    if(LocateImage('chrome-selected.png', 0) and url != None):
        print('opening new tab')
        p.hotkey('ctrl', 't')
        time.sleep(0.5)
        p.write('https://{private-id}moodle.belwue.de/moodle/course/view.php?id=' + url)
        p.press('enter')
        time.sleep(3)
    elif(LocateImage('chrome-opened.png', 0) and url != None):
        LocateImage('chrome-opened.png', 2)
        print('opening new tab') 
        p.hotkey('ctrl', 't')
        time.sleep(0.5)
        p.write('https://{private-id}.moodle.belwue.de/moodle/course/view.php?id=' + url)
        p.press('enter')
        time.sleep(3)
    else:
        print('opening Chrome')
        p.hotkey('ctrl', '2')
        time.sleep(5)
    LocateImage('login.png', 1)
    time.sleep(3)

def CheckSubject():
    global music
    print('[---]', end='\r')
    time.sleep(3)
    if(date.today().weekday() == 0): #monday
        Monday()
    elif(date.today().weekday() == 1): #tuesday
        Tuesday()
    elif(date.today().weekday() == 2): #wednesday
        Wednesday()
    elif(date.today().weekday() == 3): #thursday
        Thursday()
    elif(date.today().weekday() == 4): #friday
        Friday()
    if(cac(now.hour, now.minute) <= cac(7, 45) and music == False): #school didn't started yet
        music = True
        OpenPage(None)
        time.sleep(1)
        LocateImage('chrome-opened.png', 2)
            
def Monday():
    global subjectIndex
    currentTime = (now.hour * 60 + now.minute)
    if(currentTime >= cac(7, 45)): #1,2 or more
        if(currentTime >= cac(9, 35)): # 3,4 or more
            if(currentTime >= cac(11, 25)): #5 or more
                if(currentTime >= cac(12, 10)): #6 or more
                    if(currentTime >= cac(14, 0)): #8,9 or more
                        if(currentTime >= cac(15, 40)): #10,11 or more
                            school = False
                            if(currentTime >= cac(17, 10)): #end script
                                exit()
                            elif(subjectIndex != 6): #wbs
                                subjectIndex = 6
                                print('WBS  ')
                                OpenPage('192')
                                Search(False, True)
                                exit()
                        elif(subjectIndex != 5): #informatics
                            subjectIndex = 5
                            print('Informatics')
                            OpenPage('344')
                            Search(True, True)
                    elif(subjectIndex != 4): #math
                        subjectIndex = 4
                        print('Math')
                        OpenPage('49')
                        Search(True, True)
                elif(subjectIndex != 3):  #english
                    subjectIndex = 3
                    print('English')
                    OpenPage('491')
                    Search(True, True)
            elif(subjectIndex != 2): #russian
                subjectIndex = 2
                print('russian')
                OpenPage('291')
                Search(True, True)
        elif(subjectIndex != 1): #ethic
            subjectIndex = 1
            print('Ethic')
            OpenPage('339')
            Search(True, True)

def Tuesday():
    global subjectIndex
    currentTime = (now.hour * 60 + now.minute)
    if(currentTime >= cac(7, 45)): #1 or more
        if(currentTime >= cac(8, 30)): #2 or more
            if(currentTime >= cac(9, 35)): #3,4 or more
                if(currentTime >= cac(11, 25)): #5,6 or more
                    if(currentTime >= cac(14, 0)): #8,9 or more
                        if(currentTime >= cac(15, 40)): #10,11 or more
                            school = False
                            if(currentTime >= cac(17, 10)): #end script
                                exit()
                            elif(subjectIndex != 6): #chemistry
                                subjectIndex = 6
                                print('Chemistry')
                                OpenPage('326')
                                Search(True, True)
                                exit()
                        elif(subjectIndex != 5): #gk
                            subjectIndex = 5
                            print('GK   ')
                            OpenPage('191')
                            Search(True, True)
                    elif(subjectIndex != 4): #physics
                        subjectIndex = 4
                        print('Physics')
                        OpenPage('578')
                        Search(True, True)
                elif(subjectIndex != 3): #sport
                    subjectIndex = 3
                    print('Sport')
                    OpenPage('203')
                    Search(False, False)
            elif(subjectIndex != 2): #latin
                subjectIndex = 2
                print('Latin')
                OpenPage('149')
                Search(True, True)
        elif(subjectIndex != 1): #linguistic
            subjectIndex = 1
            print('Linguistic')
            OpenPage('190')
            Search(True, True)

def Wednesday():
    global subjectIndex
    currentTime = (now.hour * 60 + now.minute)
    if(currentTime >= cac(7, 45)): #1,2 or more
        if(currentTime >= cac(9, 35)): # 3,4 or more
            if(currentTime >= cac(11, 25)): #5,6 or more
                school = False
                if(currentTime >= cac(13, 0)): #end script
                    exit()
                elif(subjectIndex != 3): #latin
                    subjectIndex = 3
                    print('Latin')
                    OpenPage('149')
                    Search(True, True)
                    exit()
            elif(subjectIndex != 2): #linguistic
                subjectIndex = 2
                print('Linguistic')
                OpenPage('190')
                Search(True, True)
        elif(subjectIndex != 1): #history
            subjectIndex = 1
            print('History')
            OpenPage('150')
            Search(True, True)

def Thursday():
    global subjectIndex
    currentTime = (now.hour * 60 + now.minute)
    if(currentTime >= cac(7, 45)): #1,2 or more
        if(currentTime >= cac(9, 35)): #3 or more
            if(currentTime >= cac(10, 20)): #4 or more
                if(currentTime >= cac(11, 25)): #5,6 or more
                    school = False
                    if(currentTime >= cac(13, 0)): #end script
                        exit()
                    elif(subjectIndex != 4): #russian
                        subjectIndex = 4
                        print('Russian')
                        OpenPage('291')
                        Search(True, True)
                        exit()
                elif(subjectIndex != 3): #math
                    subjectIndex = 3
                    print('Math')
                    OpenPage('49')
                    Search(True, True)
            elif(subjectIndex != 2): #linguistic
                subjectIndex = 2
                print('Linguistic')
                OpenPage('190')
                Search(True, False)
        elif(subjectIndex != 1): #biology
            subjectIndex = 1
            print('Biology')
            OpenPage('901')
            Search(True, True)

def Friday():
    global subjectIndex
    currentTime = (now.hour * 60 + now.minute)
    if(currentTime >= cac(7, 43)): #1,2 or more
        if(currentTime >= cac(9, 35)): # 3,4 or more
            if(currentTime >= cac(11, 25)): #5,6 or more
                school = False
                if(currentTime >= cac(13, 0)): #end script
                    exit()
                elif(subjectIndex != 3): #english
                    subjectIndex = 3
                    print('English')
                    OpenPage('491')
                    Search(True, True)
                    exit()
            elif(subjectIndex != 2): #art
                subjectIndex = 2
                print('Art  ')
                OpenPage('888')
                Search(True, False)
        elif(subjectIndex != 1): #math
            subjectIndex = 1
            print('Math')
            OpenPage('49')
            Search(True, True)

def Move(x, y):
    p.click(x, y)
    time.sleep(3)

def cac(x, y):
    x *= 60
    return (x + y)

def LocateImage(x:str, locType:int):
    if(locType == 0): #just check if the picture is there
        if(p.locateCenterOnScreen('C:/1/PROJECTS/Python/School/Image/' + x)):
            return True
        else:
            return False
    elif(locType == 1): #try clicking without error
        result = p.locateCenterOnScreen('C:/1/PROJECTS/Python/School/Image/' + x)
        try: Move(result.x, result.y)
        except: pass
    elif(locType == 2): #try clicking with error
        result = p.locateCenterOnScreen('C:/1/PROJECTS/Python/School/Image/' + x)
        try: Move(result.x, result.y)
        except: print("Couldn't find " + x)

def Search(oneattendence, onemeeting):
    if(oneattendence == True):
        print("Attendence confirming")
        LocateImage('attendence.png', 2)
        for i in range(5):
            if(LocateImage('confirm-attendence.png', 0)):
                LocateImage('confirm-attendence.png', 1)
                break
            elif(LocateImage('confirm-attendence-1.png', 0)):
                LocateImage('confirm-attendence-1.png', 1)
                break
            else:
                p.scroll(-1000)
            if(i == 4):
                playsound.playsound('C:/1/PROJECTS/Sound/error-loud.mp3')
                print('Attendence confirmation failed')
                time.sleep(10)
        LocateImage('flip-attendence.png', 2)
        LocateImage('capture-attendence.png', 2)
        p.scroll(10000)
        Move(530, 235) #go back to default subject screen
    else:
        playsound.playsound('C:/1/PROJECTS/Sound/error-loud.mp3')
        print('Check for Attendence in this subject')
    if(onemeeting == True):
        print("Meeting confirming")
        LocateImage('meeting.png', 2)
        time.sleep(3)
        if(LocateImage('confirm-meeting.png', 0)):
            LocateImage('confirm-meeting.png', 2)
            time.sleep(5)
            Move(715, 550) #headphones (no mic)
    else:
        playsound.playsound('C:/1/PROJECTS/Sound/error-loud.mp3')
        print('Check for Meeting in this subject')


while True:
    now = datetime.datetime.now()
    if((updatingFrame % 3) == 0): #plays an animation in the command line
        CheckSubject()
    print(updatingAnimation[updatingFrame % len(updatingAnimation)], end='\r')
    time.sleep(0.8)
    updatingFrame += 1