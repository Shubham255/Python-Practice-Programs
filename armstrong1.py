num = int(input("Enter a number: "))

sum = 0

temp = num
while temp > 0:
   rem=temp%10
   sum+=rem**3
   temp//=10

if num == sum:
   print("Given no {}is an Armstrong number".format(num))
else:
   print("Given no {} is not an Armstrong number".format(num))
