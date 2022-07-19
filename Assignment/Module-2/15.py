#Write a python prog to compute the value of a specified principal
#amount, rate of interest, and a number of years.

#==>
amount=int(input("Enter the value of Amount :"))
rate=int(input("Enter the rate of Interest :"))
years=int(input("Enter the num of years :"))

def Check_In(amount,rate,years):
    prn=amount*rate*years/100
    print("find the interest :",prn)

print(Check_In(amount,rate,years))
