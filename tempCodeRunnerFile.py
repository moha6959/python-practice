num=int(input("Enter a number? "))
factorial=1
if num<0:
    print("there is no factorial for negative numbers")
elif num==0:
    print("factorial of is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
print("The factorial is: ", factorial)