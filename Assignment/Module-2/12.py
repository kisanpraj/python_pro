#write prog find odd or even num
a=int(input("Enter the Number"))
if a==0 or a==1:
    print("pls enter more than 0 or 1")
elif a%2==0:
    print("is even number",a)
else:
    print("is odd number",a)
