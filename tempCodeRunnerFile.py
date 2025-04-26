num=int(input("Enter a number? "))
#initialize the factorial to 1
factorial=1
if num<0:
    print("there is no factorial for negative numbers")
elif num==0:
    print("factorial of is 1")
else:
    for i in range(1,num+1):#num+1 ensures that the stop number is also included
        factorial=factorial*i
print("The factorial is: ", factorial)