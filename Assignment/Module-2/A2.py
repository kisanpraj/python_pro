"""#Write a prog that accept an int (n) and computes the value of 
n+nn+nnn"""

#==>
n=int(input("Enter the value of n :"))
def my_fun(n):
    a=n
    b=n*n
    c=n*n*n
    print("n :",a,"n+nn :",b,"n+nn+nnn :",c)
print(my_fun(n))