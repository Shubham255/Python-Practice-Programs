    bal=1000
while True:
    print("*******Banking********")
    print("w for withdrow")
    print("d for deposite")
    ch=input("Entre Your Choice---")
    if ch in('W','w'):
        amt=float(input("Enter Amount to withdrow"))
        if amt>bal:
            print("Insuficiant Balence to withdrow")
        elif amt>25000:
            print("Per day limit is 25000")
        elif bal<1000:
            print("not sufficiant balence")
        else:
            bal=bal-amt
            print("Balance is",bal)
            
    if ch in('d','D'):
        
        amt=float(input("Enter amount to diposite"))
        bal=bal+amt
        print("Balance is ",bal)
    

else:
    print("Invalid Choice.......")
    
           
        
