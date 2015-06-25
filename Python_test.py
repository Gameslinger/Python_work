#first Python program!
import time
def start():
    first = raw_input("Hello whats your name?\n    ")

    second = raw_input('Hello '+first+", do you like python(yes/no)\n    ")

    if (second.lower() == 'yes'):
        print "you know it!"
        print '_____\n|0 -|\n| - |'
    else:
        print "good bye!"
        time.sleep(0.5)
        i = 1
        while i < 31:
            print "You need help!"+str(i)
            i +=1
    time.sleep(1.5)
start()


