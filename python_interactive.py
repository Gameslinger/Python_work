#Second Python program!
import os
import time
import sys
from random import randint

def ask():
    #Asks questions!
    first = raw_input("So whats your name?\n    ")

    second = raw_input('Hello '+first+", do you like python(yes/no)\n    ")

    if (second.lower() == 'yes'):
        print "you know it!"
        print '_____\n|0 -|\n| - |'
    elif second == 'no':
        print "SPAM!!!"
        time.sleep(0.8)
        i = 1
        while i < 31:
            
            print "You need help! "+str(i)
            time.sleep(0.05)
            i +=1
    else:
            print 'Sorry didn\'t catch that. '
            ask()



    
def writing():
    #Writes/reads file
    filename = raw_input("What is the name of\nthe file you want to edit?:\n    ")
    edittype = raw_input("how do you want to edit it?:\n(r,w,r+,a, or ?)\n   ")
    if edittype == "?":
        print 'r is read, w is write,\nr+ is read and write,\nand a is append (add to the end)\n'
        writing()
    try:
        f = open(os.path.dirname(__file__)+'\\'+filename+'.txt',edittype)
    except:
        print ''
        print 'Only use r/r+ for existing files!'
        writing()
    if edittype == 'w' or edittype=='r+' or edittype == "a":
        mess = raw_input('What do you want to write?:\n     ')
        f.write(mess+' ')
        
    elif edittype == 'r':
        print ""
        print 'It says: "' + f.read() + '"'
        print ''
        start()
        
    delete = raw_input("want to delete the file?\n(y,n):     ")
    f.close()
    if delete == 'y':
        os.remove(os.path.dirname(__file__)+'\\'+filename+'.txt')





def game():
    #simple guessing game!
    print "you get 3 chances to guess what I am thinking"
    countto = raw_input("how high do you want me to guess?(not too high!)\n")
    if int(countto) <= 0:
        print ''
        print "That's too small!"
        print ''
        game()
    chances = 3
    rand = randint(1, int(countto))
    while chances > 0:
        print 'you have '+ str(chances)+' chances left!'
        guess = raw_input("What is your guess from 1-%s\n" %(str(countto)))
        
        if int(guess) == rand:
            print ""
            print '     !You did it!'
            print ""
            print ""
            start()
        else:
            if chances == 1:
                print 'The number was: '+str(rand)
                print '--------Game Over--------'
            else:
                print 'sorry try again!'
            chances -= 1
    start()
    

def calc():
    #basic calculator!
    ex = raw_input('Would you like to:\n multiply(*)\n  divide(/)\n  subtract(-)\n add(+)\n or leave(leave)\n')
    if ex == 'leave':
        start()
    elif ex != '*' or ex != '/' or ex != '-' or ex != '+':
        print "sorry didn't catch that!"
        calc()
    no1 = int(raw_input('What is the first number?\n    '))
    no2 = int(raw_input('What is the second number?\n   '))
    
    print ''
    if ex == '*':
        print no1 * no2
    elif ex == '/':
        if no2 == 0:
            print 'You can\'t divide by zero!'
            calc()
            
        else:
            print no1 / no2
    elif ex == '-':
        print no1 - no2
    elif ex == '+':
        print no1 + no2
    elif ex == 'leave':
        start()
    else:
        print 'Sorry try again'
        calc()
    print ''



def start():
    #calls this after started
    print ''
    doing = raw_input("what would you like to do?\n \
We can:\n  write or read a file(write)\n  tell me more about you(ask)\n \
play a guessing game(game)\n use a calculator(calc)\n  or leave(exit)\n     ")
    if doing.lower() == "write":
        writing()
    elif doing.lower() == "ask":
        ask()
    elif doing.lower() == "game":
        print ''
        print ''
        game()
        
    elif doing.lower() == "exit":
        print '--------Good Bye!--------'
        time.sleep(0.6)
        sys.exit()
    elif doing.lower() == 'calc':
        calc()
    else:
        print "sorry didn't catch that"
    print ''
    print ""
    
    start()


#STARTS HERE!!!!
print "welcome to Gabe's SECOND Python application"
start()





