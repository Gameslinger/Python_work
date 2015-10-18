#Tick tack toe multiplayer!

import socket
import sys
#     0   1   2
A = [" "," "," "]
B = [" "," "," "]
C = [" "," "," "]
Space = "-----"

def win():
    leave = False
    # wins: -
    if A[0] != " " and A[1] == A[0] and A[2] == A[0]:
        print "We have a winner!"
        leave = True
    elif B[1] != " " and B[1] == B[0] and B[2] == B[0]:
        print "We have a winner!"
        leave = True
    elif C[0] != " " and C[1] == C[0] and C[2] == C[0]:
        print "We have a winner!"
        leave = True
    if leave == True:
        print "We have a winner!"
        raw_input()
        sys.exit()
    

    #wins |
    if A[0] != " " and B[0] == A[0] and C[0] == A[0]:
        print "We have a winner!"
        leave = True
    elif A[1] != " " and B[1] == B[0] and C[1] == B[0]:
        print "We have a winner!"
        leave = True
    elif A[2] != " " and B[2] == C[0] and C[2] == C[0]:
        print "We have a winner!"
        leave = True

    #wins \ or /
    if A[0] != " " and B[1] == A[0] and C[2] == A[0]:
        print "We have a winner!"
        leave = True
    elif A[2] != " " and B[1] == A[3] and C[0] == A[3]:
        print "We have a winner!"
        leave = True
    

def prbr():
    print A[0]+"|"+A[1]+"|"+A[2]
    print Space
    print B[0]+"|"+B[1]+"|"+B[2] 
    print Space
    print C[0]+"|"+C[1]+"|"+C[2] 
    print ""

def move(place, mark):
    try:
        if place[0].lower() == "a" and A[int(place[1])-1] == " ":
            A[int(place[1])-1] = mark
        elif place[0].lower() == "b" and B[int(place[1])-1] == " ":
            B[int(place[1])-1] = mark
        elif place[0].lower() == "c" and C[int(place[1])-1] == " ":
            C[int(place[1])-1] = mark
        else:
            print "Invalid move! Lost your Turn!"
    except:
        print "Not a place! Lost your Turn!"

#Starting point!
print "Welcome to Gabe's Lan multiplayer"
print "Tick Tack Toe Game!\n"
print "You select a square by typing its row and colom!\
It looks like this:\n"
print "a1 | a2 | a3"
print "-------------"
print "b1 | b2 | b3"
print "-------------"
print "c1 | c2 | c3"
connect = raw_input("Would you like to host(h) or join(j) a game: ")

if connect == "h":

    try:
        server = socket.socket()            
        server.bind(("127.0.0.1", 4030))        
        server.listen(5)
    except:
        print "Could not bind port!"
        raw_input()
        sys.exit()
    print "Waiting for player!"
    while True:
       #got connection
       c, addr = server.accept()
       try:
           while True:
               prbr()
               win()
               choice = raw_input("What is your move: ")
               move(choice,"O")
               prbr()
               win()
               print "Other players turn!"
               c.send(choice)
               move(c.recv(1024),"X")
               
       except:
           print "Client left..."
           c.close()
       
elif connect == "j":
    #found server
    connection = False
    print "Looking for host!"
    while not connection:
        try:
            
            client = socket.socket()         
            client.connect(("127.0.0.1", 4030))
            connection = True
        except:
            pass
        
    try:
        prbr()
        while True:
               print "Other players turn!"
               move(client.recv(1024),"O")
               prbr()
               win()
               choice = raw_input("What is your move: ")
               client.send(choice)
               move(choice,"X")
               prbr()
               win()
    except:
        print "Host left..."
        client.close
    
else:
    print "Sorry what was that?"
