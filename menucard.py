total=0
while True:
    print("*****************************Menu Card***********************************")
    print(" V : \tVeg\n N :\tNon-Veg\n E :\tExit")
    ch=input("Enter Your Choice:----")

    if ch=='v':
        while True:
            
            print("********************* Veg Menu ******************************")
            print("S : \tStater\n M :\tMain Cource\n D :\tDessert\n E :\t Exit")
            vch=input("Enter Your Choice:----")
            if vch=='s':
                while True:
                    print("********************** Stater Menu ************************")
                    print(" M :\tManturian Fry \t250Rs\nS :\tSoyabin Fry \t200Rs\nP :\tPanner Fry \t300Rs\nE :\tExit")

                    stch=input("Enter Your Choice:----")
                    if stch=='m':
                        qty=int(input("Enter YOur Quntity"))
                        total=total+(250*qty)
                        print("Manturian Fry Added X",qty)
                    elif stch=='s':
                        qty=int(input("Enter YOur Quntity"))
                        total=total+(200*qty)
                        print("Soyabin Fry Added X",qty)    
                    elif stch=='p':
                        qty=int(input("Enter YOur Quntity"))
                        total=total+(350*qty)
                        print("Panner Fry Added X",qty)
                    else:
                        break
            elif vch=='m':
                while True:
                    print("********************** Main Cource Menu ************************")
                    print(" B :\tBhaji \t300Rs\nC :\tChapati \t25Rs\nR :\tRice \t150Rs\nE :\tExit")

                    mch=input("Enter Your Choice:----")
                    if mch=='b':
                        qty=int(input("Enter YOur Quntity"))
                        total=total+(300*qty)
                        print("Bhaji Added X",qty)
                    elif mch=='c':
                        qty=int(input("Enter YOur Quntity"))
                        total=total+(25*qty)
                        print("Chapati Added X",qty)    
                    elif mch=='r':
                        qty=int(input("Enter YOur Quntity"))
                        total=total+(150*qty)
                        print("Rice Added X",qty)
                    else:
                        break


                    
            elif vch=='d':
                while True:
                    print("********************** Dessert Menu ************************")
                    print(" G :\tGulab Jamun \t250Rs\nR :\tRasmalai \t300Rs\nI :\tIce-Creem \t200Rs\nE :\tExit")

                    dch=input("Enter Your Choice:----")
                    if dch=='g':
                        qty=int(input("Enter YOur Quntity"))
                        total=total+(250*qty)
                        print("Gulab Jamun X",qty)
                    elif dch=='r':
                        qty=int(input("Enter YOur Quntity"))
                        total=total+(300*qty)
                        print("Rasmalai Added X",qty)    
                    elif dch=='i':
                        qty=int(input("Enter YOur Quntity"))
                        total=total+(200*qty)
                        print("Ice-Creem X",qty)
                    else:
                        break

                    ################################################################################
    if ch=='n':
        while True:
            
            print("********************* Non-Veg Menu ******************************")
            print("S : \tStater\n M :\tMain Cource\n D :\tDessert\n E :\t Exit")
            nch=input("Enter Your Choice:----")
            if nch=='s':
                while True:
                    print("********************** Stater Menu ************************")
                    print(" C :\tChicken Fry \t300Rs\nM :\tMotton Fry \t500Rs\nF :\tFish Fry \t400Rs\nE :\tExit")

                    nstch=input("Enter Your Choice:----")
                    if nstch=='c':
                        qty=int(input("Enter YOur Quntity"))
                        total=total+(300*qty)
                        print("Chicken Fry Added X",qty)
                    elif nstch=='m':
                        qty=int(input("Enter YOur Quntity"))
                        total=total+(500*qty)
                        print("Motton Fry Added X",qty)    
                    elif nstch=='f':
                        qty=int(input("Enter YOur Quntity"))
                        total=total+(400*qty)
                        print("Fish Fry Added X",qty)
                    else:
                        break
            elif nch=='m':
                while True:
                    print("********************** Main Cource Menu ************************")
                    print(" B :\tChicken Bhaji \t300Rs\nC :\tChapati \t25Rs\nR :\tRice \t150Rs\nE :\tExit")

                    nmch=input("Enter Your Choice:----")
                    if nmch=='b':
                        qty=int(input("Enter YOur Quntity"))
                        total=total+(300*qty)
                        print("Chicken Bhaji Added X",qty)
                    elif nmch=='c':
                        qty=int(input("Enter YOur Quntity"))
                        total=total+(25*qty)
                        print("Chapati Added X",qty)    
                    elif nmch=='r':
                        qty=int(input("Enter YOur Quntity"))
                        total=total+(150*qty)
                        print("Rice Added X",qty)
                    else:
                        break


                    
            elif nch=='d':
                while True:
                    print("********************** Dessert Menu ************************")
                    print(" G :\tGulab Jamun \t250Rs\nR :\tRasmalai \t300Rs\nI :\tIce-Creem \t200Rs\nE :\tExit")

                    dch=input("Enter Your Choice:----")
                    if ndch=='g':
                        qty=int(input("Enter YOur Quntity"))
                        total=total+(250*qty)
                        print("Gulab Jamun X",qty)
                    elif ndch=='r':
                        qty=int(input("Enter YOur Quntity"))
                        total=total+(300*qty)
                        print("Rasmalai Added X",qty)    
                    elif ndch=='i':
                        qty=int(input("Enter YOur Quntity"))
                        total=total+(200*qty)
                        print("Ice-Creem X",qty)
                    else:
                        break                    
#########################################################################################################
    elif ch =='e':
        GST=total*0.18
        total=total+GST
        print("your gst is :", GST)
        print("thank you \nyour total bill is:",total)
        break
    else:
        print("Invalid Choice...!")
    ch8 = input("Do you want to continue (y/n) = ").lower()
    if ch8 =='y':
        continue
    elif ch8 =='n':
        break
    else:
        print("Invalid Choice")                                    
    break
