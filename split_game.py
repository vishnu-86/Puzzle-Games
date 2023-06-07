import random
c1=1
c2=1
p1=1
p2=1
l=["split","11","21","12","22"]
def prin(c1,c2,p1,p2):
    print("")
    print(c1,"  ",c2)
    print("")
    print(p1,"  ",p2)
#prin(c1,c2,p1,p2)
def inp():
    a=input("-")
    if a=="s" or a=="S":
        return 0
    elif a=="11":
        return 1
    elif a=="12":
        return 2
    elif a=="21":
        return 3
    elif a=="22":
        return 4
    else:
        return -1

def win(c1,c2,p1,p2):
    if p1==0 and  p2==0:
        return 1
    elif c1==0 and c2==0:
        return 2
    else:
        return 0

def end(c1,c2,p1,p2):
    c1,c2,p1,p2=bal(c1,c2,p1,p2)
    if p1==0:
        if p2+c1==5:
            return 3
        elif p2+c2==5:
            return 4
    elif p2==0:
        if p1+c1==5:
            return 1
        elif p1+c2==5:
            return 2
    return 0

def bal(c1,c2,p1,p2):
    if c1>4:
        c1=-5+c1
    if c2>4:
        c2=-5+c2
    if p1>4:
        p1=-5+p1
    if p2>4:
        p2=-5+p2
    return c1,c2,p1,p2

def spl(g,h):
    if g==0 and h in [2,4]:
        g=h//2
        h=h//2
    if h==0 and g in [2,4]:
        h=g//2
        g=g//2
    return g,h

def pbrain(c1,c2,p1,p2):
    l1=posc(c1,c2,p1,p2)
    c1,c2,p1,p2=bal(c1,c2,p1,p2)
    if p1!=0 and c1!=0:
        if end(p1+c1,p2,c1,c2) !=0:
            l1.remove(1)
    if p1!=0 and c2!=0:
        if end(p1+c2,p2,c1,c2) !=0:
            l1.remove(2)
    if p2!=0 and c1!=0:
        if end(p1,p2+c1,c1,c2) !=0:
            l1.remove(3)
    if p2!=0 and c2!=0:
        if end(p1,p2+c2,c1,c2) !=0:
            l1.remove(4)
    if (c1==0 and c2 in [2,4]) or (c2==0 and c1 in [2,4]):
        l1.append(0)
    
    return l1

def posc(c1,c2,p1,p2):
    l1=[1,2,3,4]
    c1,c2,p1,p2=bal(c1,c2,p1,p2)
    if c1==0:
        if 1 in l1:
            l1.remove(1)
        if 3 in l1:
            l1.remove(3)
    if c2==0:
        if 2 in l1:
            l1.remove(2)
        if 4 in l1:
            l1.remove(4)
    if p1==0:
        if 1 in l1:
            l1.remove(1)
        if 2 in l1:
            l1.remove(2)
    if p2==0:
        if 4 in l1:
            l1.remove(4)
        if 3 in l1:
            l1.remove(3)
    return l1

def sbrain(c1,c2,p1,p2):
    l1=posc(c1,c2,p1,p2)
    c1,c2,p1,p2=bal(c1,c2,p1,p2)
    for i in l1:
        if i==1:
            if pbrain(p1+c1,p2,c1,c2)==[]:2
                return 1
        if i==2:
            if pbrain(p1+c2,p2,c1,c2)==[]:
                return 2
        if i==3:
            if pbrain(p1,p2+c1,c1,c2)==[]:
                return 3
        if i==4:
            if pbrain(p1,p2+c2,c1,c2)==[]:
                return 4
        if (c1==0 and c2 in [2,4]) or (c2==0 and c1 in [2,4]):
            c3,c4=spl(c1,c2)
            if pbrain(p1,p2,c3,c4)==[]:
                return 0
    return -1

def splc(c1,c2,p1,p2):
    if (c1==0 and c2==2) or (c2==0 and c1==2):
        if p1==4 and p2==4:
            return -1
        else:
            return 0
    elif (c1==0 and c2==4) or (c2==0 and c1==4):
        return 0
    return -1

def tbrain(c1,c2,p1,p2):
    l1=posc(c1,c2,p1,p2)
    c1,c2,p1,p2=bal(c1,c2,p1,p2)
    l2=[]
    for i in l1:
        if i==1:
            if  sbrain(p1+c1,p2,c1,c2)==-1:
                l2.append(1)
        if i==2:
            if  sbrain(p1+c2,p2,c1,c2)==-1:
                l2.append(2)
        if i==3:
            if  sbrain(p1,p2+c1,c1,c2)==-1:
                l2.append(3)
        if i==4:
            if  sbrain(p1,p2+c2,c1,c2)==-1:
                l2.append(4)
        if (c1==0 and c2 in [2,4]) or (c2==0 and c1 in [2,4]):
            c3,c4=spl(c1,c2)
            if sbrain(p1,p2,c3,c4)==-1:
                l2.append(0)
    return l2

def pwbrain(c1,c2,p1,p2):
    l1=posc(c1,c2,p1,p2)
    c1,c2,p1,p2=bal(c1,c2,p1,p2)
    for i in l1:
        if i==1:
            if  tbrain(p1+c1,p2,c1,c2)==[]:
                return 1
        if i==2:
            if  tbrain(p1+c2,p2,c1,c2)==[]:
                return 2
        if i==3:
            if  tbrain(p1,p2+c1,c1,c2)==[]:
                return 3
        if i==4:
            if  tbrain(p1,p2+c2,c1,c2)==[]:
                return 4
        if (c1==0 and c2 in [2,4]) or (c2==0 and c1 in [2,4]):
            c3,c4=spl(c1,c2)
            if tbrain(p1,p2,c3,c4)==[]:
                return 0
    return -1
    
def pw1brain(c1,c2,p1,p2):
    l1=posc(c1,c2,p1,p2)
    c1,c2,p1,p2=bal(c1,c2,p1,p2)
    l2=[]
    for i in l1:
        if i==1:
            if pwbrain(p1+c1,p2,c1,c2)==-1:
                l2.append(1)
        if i==2:
            if  pwbrain(p1+c2,p2,c1,c2)==-1:
                l2.append(2)
        if i==3:
            if  pwbrain(p1,p2+c1,c1,c2)==-1:
                l2.append(3)
        if i==4:
            if  pwbrain(p1,p2+c2,c1,c2)==-1:
                l2.append(4)
        if (c1==0 and c2 in [2,4]) or (c2==0 and c1 in [2,4]):
            c3,c4=spl(c1,c2)
            if pwbrain(p1,p2,c3,c4)==-1:
                l2.append(0)
    return l2

def pw2brain(c1,c2,p1,p2):
    l1=posc(c1,c2,p1,p2)
    c1,c2,p1,p2=bal(c1,c2,p1,p2)
    for i in l1:
        if i==1:
            if  pw1brain(p1+c1,p2,c1,c2)==[]:
                return 1
        if i==2:
            if  pw1brain(p1+c2,p2,c1,c2)==[]:
                return 2
        if i==3:
            if  pw1brain(p1,p2+c1,c1,c2)==[]:
                return 3
        if i==4:
            if  pw1brain(p1,p2+c2,c1,c2)==[]:
                return 4
        if (c1==0 and c2 in [2,4]) or (c2==0 and c1 in [2,4]):
            c3,c4=spl(c1,c2)
            if pw1brain(p1,p2,c3,c4)==[]:
                return 0
    return -1

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
    print("WELCOME TO VISHNU' S SPLIT..")
    print("")
    print("1: PLAY")
    print("2:QUIT")
    a=int(input("enter ur choice: "))
    if a==2:
        break
    if a!=1:
        print("invalid choice")
        continue
    if luck()==1:
        print("U WON THE TOSS AND U CAN START THE GAME")
        b=1
    else:
        print("U LOOSE THE TOSS AND COMPUTER WILL START THE GAME")
        b=2
    prin(c1,c2,p1,p2)
    try:
        if b==1:
            while True:
                print("UR TURN")
                c=inp()
                l1=posc(c1,c2,p1,p2)
                if c==0:
                    if (p1==0 and p2 in [2,4]) or (p2==0 and p1 in [2,4]):
                        p1,p2=spl(p1,p2)
                    else:
                        print("it cant be splited..")
                        continue
                if c==1:
                    if 1 in l1:
                        c1=c1+p1
                    else:
                        print("invalid choice")
                        continue
                if c==2:
                    if 2 in l1:
                        c2=c2+p1
                    else:
                        print("invalid choice")
                        continue
                if c==3:
                    if 3 in l1:
                        c1=c1+p2
                    else:
                        print("invalid choice")
                        continue
                if c==4:
                    if 4 in l1:
                        c2=c2+p2
                    else:
                        print("invalid choice")
                        continue
                c1,c2,p1,p2=bal(c1,c2,p1,p2)
                print("")
                prin(c1,c2,p1,p2)
                if win(c1,c2,p1,p2)!=0:
                    if win(c1,c2,p1,p2)==1:
                        print("AI WINS...BETTER LUCK NEXT TIME..")
                        print("")
                        break
                    else:
                        print("U WON..WELL DONE!!")
                        print("")
                        break
                d=-1
                la=posc(c1,c2,p1,p2)
                if end(c1,c2,p1,p2)!=0:
                    d=end(c1,c2,p1,p2)
                else:
                    if splc(c1,c2,p1,p2)==0:
                        d=0
                    else:
                        if len(pbrain(c1,c2,p1,p2))==1:
                            d=pbrain(c1,c2,p1,p2)[0]
                        else:
                            if sbrain(c1,c2,p1,p2)!=-1:
                                d=sbrain(c1,c2,p1,p2)
                            else:
                                if pwbrain(c1,c2,p1,p2)!=-1:
                                    d=pwbrain(c1,c2,p1,p2)
                                elif pw2brain(c1,c2,p1,p2)!=-1:
                                    d=pw2brain(c1,c2,p1,p2)
                                else:
                                    for i in la:
                                        if i==1:
                                            if pw2brain(p1+c1,p2,c1,c2)!=-1:
                                                la.remove(1)
                                        elif i==2:
                                            if pw2brain(p1+c2,p2,c1,c2)!=-1:
                                                la.remove(2)
                                        elif i==3:
                                            if pw2brain(p1,p2+c1,c1,c2)!=-1:
                                                la.remove(3)
                                        elif i==4:
                                            if pw2brain(p1,p2+c2,c1,c2)!=-1:
                                                la.remove(4)
                if d==-1:
                    if len(la)==0:
                        la=posc(c1,c2,p1,p2)
                    x2=random.randint(0,len(la)-1)
                    d=la[x2]
                print("")
                print("AI played ",l[d])
                print("")
                if d==0:
                    c1,c2=spl(c1,c2)
                if d==1:
                    p1=p1+c1
                elif d==2:
                    p1=p1+c2
                elif d==3:
                    p2=p2+c1
                elif d==4:
                    p2=p2+c2
                
                c1,c2,p1,p2=bal(c1,c2,p1,p2)
                print("")
                prin(c1,c2,p1,p2)
                if win(c1,c2,p1,p2)!=0:
                    if win(c1,c2,p1,p2)==1:
                        print("AI WINS...BETTER LUCK NEXT TIME..")
                        print("")
                        break
                    else:
                        print("U WON..WELL DONE!!")
                        print("")
                        break
                                        
        elif b==2:
            while True:
                d=-1
                la=posc(c1,c2,p1,p2)
                if end(c1,c2,p1,p2)!=0:
                    d=end(c1,c2,p1,p2)
                else:
                    if splc(c1,c2,p1,p2)==0:
                        d=0
                    else:
                        if len(pbrain(c1,c2,p1,p2))==1:
                            d=pbrain(c1,c2,p1,p2)[0]
                        else:
                            if sbrain(c1,c2,p1,p2)!=-1:
                                d=sbrain(c1,c2,p1,p2)
                            else:
                                if pwbrain(c1,c2,p1,p2)!=-1:
                                    d=pwbrain(c1,c2,p1,p2)
                                elif pw2brain(c1,c2,p1,p2)!=-1:
                                    d=pw2brain(c1,c2,p1,p2)
                                else:
                                    for i in la:
                                        if i==1:
                                            if pw2brain(p1+c1,p2,c1,c2)!=-1:
                                                la.remove(1)
                                        elif i==2:
                                            if pw2brain(p1+c2,p2,c1,c2)!=-1:
                                                la.remove(2)
                                        elif i==3:
                                            if pw2brain(p1,p2+c1,c1,c2)!=-1:
                                                la.remove(3)
                                        elif i==4:
                                            if pw2brain(p1,p2+c2,c1,c2)!=-1:
                                                la.remove(4)
                if d==-1:
                    if len(la)==0:
                        la=posc(c1,c2,p1,p2)
                    x2=random.randint(0,len(la)-1)
                    d=la[x2]
                print("")
                print("AI played ",l[d])
                print("")
                if d==0:
                    c1,c2=spl(c1,c2)
                if d==1:
                    p1=p1+c1
                elif d==2:
                    p1=p1+c2
                elif d==3:
                    p2=p2+c1
                elif d==4:
                    p2=p2+c2
                
                c1,c2,p1,p2=bal(c1,c2,p1,p2)
                print("")
                prin(c1,c2,p1,p2)
                if win(c1,c2,p1,p2)!=0:
                    if win(c1,c2,p1,p2)==1:
                        print("AI WINS...BETTER LUCK NEXT TIME..")
                        print("")
                        break
                    else:
                        print("U WON..WELL DONE!!")
                        print("")
                        break
                print("UR TURN")
                while True:
                    c=inp()
                    l1=posc(c1,c2,p1,p2)
                    if c==0:
                        if (p1==0 and p2 in [2,4]) or (p2==0 and p1 in [2,4]):
                            p1,p2=spl(p1,p2)
                            break
                        else:
                            print("it cant be splited..")
                            continue
                    if c not in l1:
                        print("invalid choice")
                        continue
                    if c==1:
                        if 1 in l1:
                            c1=c1+p1
                            break
                    if c==2:
                        if 2 in l1:
                            c2=c2+p1
                            break
                    if c==3:
                        if 3 in l1:
                            c1=c1+p2
                            break
                    if c==4:
                        if 4 in l1:
                            c2=c2+p2
                            break
                c1,c2,p1,p2=bal(c1,c2,p1,p2)
                print("")
                prin(c1,c2,p1,p2)
                if win(c1,c2,p1,p2)!=0:
                    if win(c1,c2,p1,p2)==1:
                        print("AI WINS...BETTER LUCK NEXT TIME..")
                        print("")
                        break
                    else:
                        print("U WON..WELL DONE!!")
                        print("")
                        break
    except:
        print("Unexpected error occured..")
exit()                    