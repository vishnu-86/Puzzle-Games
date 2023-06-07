import random
d={1:[[1,2],[3,6]],5:[[-1,1],[-2,2],[-3,3],[-4,4]],9:[[-1,-2],[-3,-6]]}
k=[1,5,9]
p={1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9"}
dif=2
def prin(p):
    a1=1
    for i in range(3):
        for j in range(2):
            print("")
        print(p[a1],end="")
        a1+=1
        print(" "*7,end="")
        print(p[a1],end="")
        a1+=1
        print(" "*7,end="")
        print(p[a1],end="")
        a1+=1
        if a1==10:
            print("")
            print("")  
def win(l,wi):
    for i in k:
        if wi==1:
            break
        else:
            if i in l:
                for j in d[i]:                    
                    if (j[0]+i) in l:
                        if (j[1]+i) in l:
                            if wi==0:
                                print("")
                                if l==l1:
                                    print("YOU WON")
                                else:
                                    print("YOU LOOSE")
                            wi=1
                            return 1
                            break
def play(l,a,p,j):
    while True:
        z=int(input("enter the position in which u want to play: "))
        if z<1 or z>9:
            print("number should be between 0 and 10")
            continue
        if z not in a:
            print("position already occupied")
            print("unoccupied possitions are: ",a)
            continue
        else:
            break
    l1.append(z)
    a.remove(z)
    p[z]=j

def pred(l,a):
    lb=[]
    for i in k:
        if i in l:
            for j in d[i]:                    
                if (j[0]+i) in l or (j[1]+i) in l:
                    if (j[0]+i) in l and (j[1]+i) in a:                        
                        lb.append(j[1]+i)  
                    else:
                        if (j[0]+i) in a and (j[0]+i) in a:
                            lb.append(j[0]+i)                            
        else:
            l.append(i)
            wi=2
            if win(l,wi)==1 and i in a:
                l.remove(i)
                lb.append(i)
            else:
                l.remove(i)
    return lb
def dp(a,l):
    l3=[]
    for j in range(0,len(a)):
        i=a[0]
        l.append(i)
        a.remove(i)
        pr=pred(l,a)
        if len(pr)>=2:
            if pr==3:
                l3.append(i)
            else:
                if pr[0]==pr[1]:
                    pass
                else:
                    l3.append(i)
        l.remove(i)
        a.append(i)
    return l3

def ddp(a,l1,l2):
    l3=[1,3,7,9,5]
    l4=[]
    l5=[]
    l6=[]
    for i in l2:
        l4.append(i)
    for i in a:
        l6.append(i)
    for i in l1:
        l5.append(i)
    for i in l3:
        if i not in a:
            l3.remove(i)
    for i in l3:
        l2.append(i)
        if i in a:
            a.remove(i)
        pr=pred(l2,a)
        if len(pr)!=0:
            a.remove(pr[0])
            l1.append(pr[0])
            pr1=(dp(a,l2))
            if len(pr1)!=0:
                for k in pr1:
                    if len(pred(l1,a))==0 or ((pred(l1,a))[0])==k:
                        for j in l2:
                            if j not in l4:
                                l2.remove(j)
                        for j in a:
                            if j not in l6:
                                a.remove(j)
                        for j in l1:
                            if j not in l5:
                                l1.remove(j)
                        return i
        for i in l2:
            if i not in l4:
                l2.remove(i)
        for j in l6:
                    if j not in a:
                        a.append(j)
        for j in l1:
                        if j not in l5:
                            l1.remove(j)
    return 0
def omo(a,l1,l2):
    l3=[1,3,7,9]
    l4=[2,4,6,8]
    y=0
    if len(l1)==1 and len(l2)==0:
        if l1[0]!=5:
            y=5
        else:
            y1=random.randint(0,3)
            y=l3[y1]
        return y
    if len(dp(a,l2))!=0:
        pr=dp(a,l2)
        return (pr[0])
    if len(l1)==2 and len(l2)==1:
        for i in l1:
            if i in l3:
                l3.remove(i)
            else:
                break
        if len(l3)==2:
            if l2[0]==5:
                y1=random.randint(0,3)
                y=l4[y1]
                return y
    return 0        
    
def xmo(a,l1,l2):
    l3=[1,3,7,9]
    y=0    
    if len(l1)==0 and len(l2)==0:
        y1=random.randint(1,3)
        y=l3[y1]
        return y
    if len(dp(a,l2))!=0:
        pr=dp(a,l2)
        return (pr[0])
    if 5 not in l1:
        pr=ddp(a,l1,l2)
        if pr!=0:
            return pr
    if 5 in l1:
        l4=[]
        for i in a:
            l2.append(i)
            if len(pred(l2,a))!=1:
                l4.append(i)
            l2.remove(i)
        if len(l4)>1:
            y1=random.randrange(0,len(l4)-1)
            y=l4[y1]
    return y                                        
                
def luck():
    print("1:HEAD")
    print("2:TAIL")
    x2=random.randint(1,2)
    while True:
        x1=int(input("enter ur choice: "))
        if x1 in [1,2]:
            break
        else:
            print("Invalid choice")
    if x1==x2:
        return 1
    else:
        return 0
    
while True:
    a=[1,2,3,4,5,6,7,8,9]
    l1=[]
    l2=[]
    wi=0
    p={1:"-",2:"-",3:"-",4:"-",5:"-",6:"-",7:"-",8:"-",9:"-"}
    while True:
        print("")
        print("WELCOME TO VISHNU'S X-O..")
        print("")
        print("1 : START GAME")
        print("")
        print("2 : CHOOSE DIFFICULTY")
        print("")
        print("3 : HOW TO PLAY")
        print("")
        print("4 : QUIT")
        print("")
        while True:
            ho=int(input("enter ur choice: "))
            if ho in [1,2,3,4]:
                break
            else:
                print("Invalid choice")
                print("")
        if ho==1:
            if luck()==1:
                j1="X"
                j2="O"
                print("U GOT 'X' AND U CAN START THE GAME")
            else:
                j1="O"
                j2="X"
                print("U GOT 'O' AND COMPUTER WILL START THE GAME")
            print("")
            break
        elif ho==2:
            if dif==1:
                print("CHOSEN DIFFICULTY IS EASY")
            elif dif==2:
                print("CHOSEN DIFFICULTY IS NORMAL")
            else:
                print("CHOSEN DIFFICULTY IS HARD")
            print("")
            print("1 : WANT TO CHANGE IT..!")
            print("")
            print("2 : BACK TO HOME PAGE")
            while True:
                print("")
                pp=int(input(" enter ur choice: "))
                if pp in [1,2]:
                    break
                else:
                    print("invalid choice")
            if pp==2:
                continue
            else:
                print("CHOOSE UR DIFFICULTY")
                print("")
                print("1:EASY")
                print("2:NORMAL")
                print("3:HARD")
                print("")
                while True:
                    pb=int(input("Enter ur choice: "))
                    if pb not in [1,2,3]:
                        print("invalid choice")
                        continue
                    else:
                        if pb==1:
                            dif=1
                        elif pb==2:
                            dif=2
                        else:
                            dif=3
                        break
        elif ho==3:
            p={1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9"}
            prin(p)
            print(" * The numbers mark  in the boxes denotes to the respective positions")
            print(" * U have to input the number given in the position for  which u have to play")
            print(" * Difficulty of the game can be changed from home page")
            print(" * If u win the toss, u will be 'X'")
            print(" * If u get 'X',U can start the game...otherwise computer will start the game")
            print("")
            print("press 1 to go back to home page:")
            while True:
                if (int(input()))==1:
                    break
                else:
                    print("not valid")
        else:
            exit()            
            
    print("")
    try:
        while True:
            yl=[]
            y=0
            l9=[]
            for i in a:
                l9.append(i)
            if j1=="X":
                play(l1,a,p,j1)
                prin(p)
                if win(l1,wi)==1:
                    break
                if len(a)==0:
                    print("DRAW MATCH")
                    break
                print("NOW ITS COMPUTERS PLAY...")
                yl=pred(l2,a)
                if len(yl)==0 and dif!=1:
                    yl=pred(l1,a)
                if len(yl)==0:
                    y=omo(a,l1,l2)
                    if y==0:
                        for i in [1,3,7,9]:
                            if i in a:
                                if dif==3:
                                    y=i
                                    break
                        if y==0:
                            y1=random.randint(0,len(a)-1)
                            y=a[y1]
                if y==0:
                    y1=random.randint(0,len(yl)-1)
                    y=yl[y1]
                a=[]
                for i in l9:
                    if i not in l1:
                        a.append(i)
                a.remove(y)
                l2.append(y)
                for i in l2:
                    l2.remove(i)
                    if i not in l2:
                        l2.append(i)
                p[y]=j2
                prin(p)
                if win(l2,wi)==1:
                    break
                if len(a)==0:
                    print("DRAW MATCH")
                    break
            if j2=="X":
                l9=[]
                for i in a:
                    l9.append(i)
                yl=pred(l2,a)
                if len(yl)==0 and dif!=1:
                    yl=pred(l1,a)
                if len(yl)==0:
                    if dif==3:
                        y=xmo(a,l1,l2)
                    if y==0:
                        y1=random.randint(0,len(a)-1)
                        y=a[y1]
                if y==0:
                    y1=random.randint(0,len(yl)-1)
                    y=yl[y1]
                a=[]
                for i in l9:
                    a.append(i)
                a.remove(y)
                l2.append(y)
                p[y]=j2
                prin(p)
                if win(l2,wi)==1:
                    break
                if len(a)==0:
                    print("DRAW MATCH")
                    break
                play(l1,a,p,j1)
                prin(p)
                if win(l1,wi)==1:
                    break
                print("NOW ITS COMPUTERS PLAY...")
        print("")
    except:
        print("SOME ERROR OCCURED")