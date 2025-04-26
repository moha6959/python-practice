n=int(input("Enter a number? "))
#initialize sum to 0
sum=0
while n!=0:
    digit=n%10 #gets the last digit of n
    sum+=digit
    n=n//10  #removes the last digit of n
print("The sum of the digits is: ",sum)