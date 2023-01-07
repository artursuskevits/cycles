
from math import *
from time import *
from random import * 

#while True:
#    try: #task 1
#        name = (input("what is your name? "))
#        if name.lower() == "juku" :
#            print("Lähme kinno")
#            vanus = int(input("kui vana sa oled? "))
#            if vanus<=0 or vanus >=100:
#                print("viga andmetega")
#            elif vanus <6:
#                print("tasuta")
#            elif vanus>=6 and vanus <=14:
#                print("lastepilet")
#            elif vanus>=15 and vanus <65:
#                print("täispilet")
#            elif vanus>=65:
#                print("sooduspilet")
#            break
#        else:
#            print("Otsime Juku")
#    except:
#        print("Vale Andmetüb") 
   

#while True: #task2
#    nimi1 = input("mis on sinu nimi ?") #task2
#    nimi2 = input("ja mis on sinu nimi? ")
#    if nimi1.isalpha() and nimi2.isalpha():
#        if nimi1.lower()=="dilan" and nimi2.lower()=="artur" or nimi1.lower()=="artur" and nimi2.lower()=="dilan":
#            print(f"{nimi1} ja {nimi2} istute koos ")
#            break
#        else:
#            print("wrong names")
#    else:
#        print("viga!")

#kek = 0
#while True:
#    try: #task3
#        a = float(input("külje pikkus a? ")) 
#        b = float(input("külje pikkus b? "))
#        if a>0 and b>0:
#            S=round(a*b,2)
#            print(f"põrandapind = {S}m2")
#            answer = int(input("soovite remonti teha? 1-jah, other-ei?"))
#            if answer==1:
#                metr=float(input("kui palju on ruutmeeter"))
#                if a>0:
#                    cost= round(S*metr,2)
#                    print (f"remont costa={cost} eurot")
#                    break
#                else:
#                    print("viga")
#            else:
#                print("kui kahju")
#                break      
#        else:
#            print("viga")
#    except:
#        print("viga")




#while True:
#    try: #task4
#        maksab = float(input("mis hinna on ? "))
#        if maksab >0:
#            if maksab >= 700:
#                hinna = (maksab*0.7,2)
#                print(f"Soodushind on {hinna} ")
#            else:
#                print("viga")
#        else: 
#            print("viga")
#    except:
#        print("viga")

#kek=1
#while True: #task5
#    while kek==1:
#        try: 
#            n=int(input("Mitu toa korteris? "))
#            break
#        except:
#            print("viga")
#    while kek==1:
#        try:
#            for i in range (1,n+1,1):
#                    temperatuur = float(input(f"{i}. mis temepreatuur on? ")) 
#                    if temperatuur >18 and temperatuur <30:
#                        print("see on hea temperatuur") 
#                    else:
#                        print("see ei ole hea temperatuur")
#                    kek +=1     
#        except:
#            print("viga")

#while True:
#    try: #task7
#        sugu= int(input("kas sa oled tüdrukud 1-JAH, OTHER - NO"))
#        if sugu==1:
#            pikkus = float(input("mis on sinu pikkus? "))
#            if pikkus <100 or pikkus >250:
#                print("vale pikkus")
#            elif pikkus >100:
#                print ("sa oled madal")
#            elif pikkus >=160 and pikkus <=180:
#                print ("sa oled keskmine")
#            elif pikkus >180:
#                print ("sa oled kõrge")
#        else:
#            pikkus = float(input("mis on sinu pikkus? "))
#            if pikkus <100 or pikkus >250:
#                print("vale pikkus")
#            elif pikkus >100:
#                print ("sa oled madal")
#            elif pikkus >=170and pikkus <=185:
#                print ("sa oled keskmine")
#            elif pikkus >190:
#                print ("sa oled kõrge")
#        break
#    except:
#        print("viga")

#try: #task6 for


#    madal = 0
#    keskmine = 0
#    kõrge=0
#    kogus=randint(1,20)
#    print(f"{kogus} inimsid")
#    for i in range(1,kogus+1,1):
#        sleep(0.5)
#        pikkus = randint(56,256)                     #float(input("mis on sinu pikkus? "))
#        if pikkus <56 or pikkus >256:
#           print(f"{pikkus} see ole viga")
#        elif  pikkus >56 and pikkus<160:
#           print (f"{pikkus} sa oled madal")
#           madal = madal + 1
#        elif pikkus >=160 and pikkus <=180:
#           print (f"{pikkus} sa oled keskmine")
#           keskmine = keskmine +1
#        elif pikkus >180 and pikkus <=256:
#           print (f"{pikkus} sa oled kõrge")
#           kõrge = kõrge +1
#    print("kõrge inimesid " + str(kõrge))
#    print("keskmine inimesid " + str(keskmine))
#    print("madal inimesid " + str(madal))
#except:
#    print("viga")

#try: #task6 while

#    madal = 0
#    keskmine = 0
#    kõrge=0
#    kogus=randint(1,20)
#    print(f"{kogus} inimsid")

#    while kogus>0:
#        kogus-=1
#        sleep(0.5)
#        pikkus = randint(56,256)                     #float(input("mis on sinu pikkus? "))
#        if pikkus <56 or pikkus >256:
#           print(f"{pikkus} see ole viga")
#        elif  pikkus >56 and pikkus<160:
#           print (f"{pikkus} sa oled madal")
#           madal = madal + 1
#        elif pikkus >=160 and pikkus <=180:
#           print (f"{pikkus} sa oled keskmine")
#           keskmine = keskmine +1
#        elif pikkus >180 and pikkus <=256:
#           print (f"{pikkus} sa oled kõrge")
#           kõrge = kõrge +1
        

#    print("kõrge inimesid " + str(kõrge))
#    print("keskmine inimesid " + str(keskmine))
#    print("madal inimesid " + str(madal))
#except:
#    print("viga")

#while True:
#    try: #task8
#        piim = int(input("sa tahad piima osta 1-yes, other-no? "))
#        if piim == 1:
#            piimost = float(input("kui palju piim maksab? "))
#            if piimost>0:
#                saia = int(input("sa tahad saia osta 1-yes, other - no? "))
#                if saia == 1:
#                    saiaost = float(input("kui palju saia maksab? "))
#                    if saiaost>0:
#                        leiba = int(input("sa tahad leiba osta 1-yes, other - no? "))
#                        if leiba == 1 :
#                            leibaost = float(input("kui palju leiba maksab? "))
#                            if leibaost>0:
#                                summa= leibaost + piimost + saiaost
#                                print(f"sa kulutasid{summa} euro")
#                            print("viga")
#                        else:
#                            summa= piimost + saiaost
#                            print(f"sa kulutasid{summa} euro")
#                    else:
#                        print("viga")
#                else:
#                    leiba = int(input("sa tahad leiba osta 1-yes, other - no? "))
#                    if leiba == 1 :
#                        leibaost = float(input("kui palju leiba maksab? "))
#                        if leibaost>0:
#                            summa= leibaost + piimost
#                            print(f"sa kulutasid{summa} euro")
#                        else:
#                            print("viga")
#                    else:
#                        summa= piimost
#                        print(f"sa kulutasid{summa} euro")
#            else:
#                print("viga")
#        else:
#            saia = int(input("sa tahad saia osta 1-yes, other - no? "))
#            if saia == 1:
#                saiaost = float(input("kui palju saia maksab? "))
#                if saiaost>0:
#                    leiba = int(input("sa tahad leiba osta 1-yes, other - no? "))
#                    if leiba == 1 :
#                        leibaost = float(input("kui palju leiba maksab? "))
#                        if leibaost>0:
#                            summa= leibaost + saiaost
#                            print(f"sa kulutasid{summa} euro")
#                        else:
#                            print("viga")
#                    else:
#                        summa= saiaost
#                        print("sa kulutasid{summa} euro")
#                else:
#                    prins("viga")
#            else:
#                leiba = int(input("sa tahad leiba osta 1-yes, other - no? "))
#                if leiba == 1 :
#                    leibaost = float(input("kui palju leiba maksab? "))
#                    if leibaost>0:
#                        summa= leibaost
#                        print(f"sa kulutasid{summa} euro")
#                    else:
#                        print("viga")
#                else: 
#                    print("sa ei ostnud midagi")
#    except:
#        print("viga")
    
    
#viga=1 #task 9
#while True:
#    while viga :
#        try:
#            a  =float(input("külje pikkus a?"))
#            if a>0 or a.isdigit() :
#                viga +=1
#                break
#        except:
#            print("viga")
#    while viga :
#        try:
#            b=float(input("külje pikkus b?"))
#            if b>0 or b.isdigit() :
#                viga +=1
#                break
#        except:
#            print("viga")
#    while viga :
#        try:
#            c=float(input("külje pikkus c?"))
#            if c>0 or c.isdigit() :
#                viga +=1
#                break
#        except:
#            print("viga")
#    while viga :
#        try:
#            d=float(input("külje pikkus d?"))
#            if d>0 or d.isdigit() :
#                viga +=1
#                break
#        except: 
#            print("viga")
#    if a>0 and b>0 and c>0 and d>0:
#        if a== b and b==c and c==d:
#            print("see on Ruut")
#            break
#        else:
#            print("see ei ole ruut")
        
#while True:
#    try: #task 10
#        arv1 = float(input("kirjuta esimene number? "))
#        arv2 = float(input("kirjuta teine number? "))
#        mark= input("valige toiming +-*/")
#        if mark == "+":
#            summ = arv1+arv2
#            print(f"answer is {summ}")
#        elif mark == "/":
#            summ = arv1/arv2
#            print(f"answer is {summ}")
#        elif mark == "*":
#            summ = arv1*arv2
#            print(f"answer is {summ}")
#        elif mark == "-":
#            summ = arv1-arv2
#            print(f"answer is {summ}")
#        else:
#            print("viga")
#    except:
#        print("viga")

#while True:
#    try: #task 11
#        aeg = int(input("mis on sinu sünniaasta? "))
#        if aeg>1900:
#            aeg2 = 2022-aeg
#            if aeg2 // 10:
#                print(f"sul on arve!")
#            else:
#                print(f"sul ei ole arve")
#        else:
#            print ("viga")
         #break
#    except:
#        print("viga")

#while True:
#    try: #task 12
#        hind = int(input("kui palju toode maksab? "))
#        if hind >=10:
#            hind2 = round(hind * 0.8,2)
#            print(f"soodushind on {hind2}")
#        else:
#            hind2 = round(hind * 0.9,2)
#            print(f"soodushind on {hind2}")
#        break
#    except :
#        print("viga!")

#while True:
#    try: #task 13
#        sugu = input("kas sa oled mees või naine? ")
#        if sugu == "naine":
#            print ("sa ei saa olla jalgpallimeeskonnas")
#        elif sugu == "mees":
#            aeg = int(input("kui vanu sa oled? "))
#            if aeg == 16 or aeg == 17 or aeg == 18:
#                print("sa oled jalgpallimeeskonnas")
#            else:
#                print("sa ei saa olla jalgpallimeeskonnas")
#        else:
#            print("viga")
#    except :
#        print("viga")

