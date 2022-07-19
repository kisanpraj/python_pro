#write a Python program to get the Factorial num of given num ?
a=int(input("Enter the Number :"))
factorial=1
if a < 0:
    print("sorry,factorial does not exit Negative Number")
elif a == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,a+1):
        factorial=factorial*i
    print("The Factorial Number ",a,"is",factorial)
        