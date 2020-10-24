from operator import pow, truediv, mul, add, sub  

operators = {
  '+': add,
  '-': sub,
  '*': mul,
  '/': truediv
}

def calculate(s):
    if s.isdigit():
        return float(s)
    for c in operators.keys():
        left, operator, right = s.partition(c)
        if operator in operators:
            return operators[operator](calculate(left), calculate(right))

calc = input("Type calculation:\n")
print("Answer: " + str(calculate(calc)))

'''while True:
    print("*********Calculator**********")
    print("+ for add")'
    print("- for sub")
    print("* for mul")
    print("/ for div")
    print("e for exit")
    ch=input("Enter your choice ==>")
    if ch =='+'
            print("Additon")
            x=int(input("Enter First Value:---"))
            y=int(input("Enter Secound Value:---"))

            z=x+y
            print("Addion is {}=>",z)
        elif ch =='-'
            print("Sub")
            x=int(input("Enter First Value:---"))
            y=int(input("Enter Secound Value:---"))

            z=x-y
            print("sub is {}=>",z)   
            
        elif ch =='*'
            print("mul")
            x=int(input("Enter First Value:---"))
            y=int(input("Enter Secound Value:---"))

            z=x*y
            print("mul is {}=>",z)
        elif ch =='/'
            print("Sub")
            x=int(input("Enter First Value:---"))
            y=int(input("Enter Secound Value:---"))

            z=x/y
            print("div is {}=>",z)

        c=input("Do you want to continue ")
        if c=='y' or  c=='Y':
        continue
        if c=='n' or c=='N':
        break
    else:
        print("Try again later")
    '''

