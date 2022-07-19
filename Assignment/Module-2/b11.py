#write a Python program to get the Fibonacci series of given number?

Fnum=int(input("How Many terms ? :"))
no1,no2=0,1
count=0
if Fnum<=0:
    print("Sorry, pls enter a positive int",Fnum)
elif Fnum==1:
    print("Fibonacci sequence upto.",Fnum,":")
    print(n1)
else:
    print("Fibonacci Sequence:")
    while count < Fnum:
        print(no1)
        nth=no1+no2
        #update value
        no1=no2
        no2=nth
        count+=1