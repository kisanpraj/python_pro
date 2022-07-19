"""#Write a Python prog that will return true if the two given int values
are equal or their sum or deifference is 5.
"""
#==>

a=int(input("Enter the value of a :"))
b=int(input("Enter the value of b :"))
def check_sum(a,b):
    global sum
    sum=a+b
    print("The SUM Is :",sum)
def check_def():
    d=sum//5
    print("The divide of 5 :",d)
print(check_sum(a,b))
print(check_def())