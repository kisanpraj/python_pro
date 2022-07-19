"""#Write a Python prog to sum of three given int.
 howwver, if two values are equal sum will be zero."""

 #==>
a=int(input("enter the value of a :"))
b=int(input("enter the value of b :"))

def check_sum(a,b):
    sum=0
    if a==b:
        print("The two values ",a," or ",b," are equal : ")
        return sum   
    else:
        sum=a+b
        print("The SUM is :",sum)
print(check_sum(a,b))