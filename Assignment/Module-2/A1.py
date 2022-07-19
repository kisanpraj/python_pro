#Write a prog to sort three int without using conditional statements and loops.

Num1=int(input("Enter the value of num1 :"))
Num2=int(input("Enter the value of num1 :"))
Num3=int(input("Enter the value of num1 :"))

N1=max(Num1,Num2,Num3)
print("The Max num is :",N1)

N3=min(Num1,Num2,Num3)
print("The Min num is :",N3)

N2=(Num1+Num2+Num3)-N1-N3
print("Num is sorted order :",N1,N2,N3)