#Write a python prog to Generate and print a list of first and last 5 elements when
#the values are square of numbers between 1 and 30.

#Ans==>

def printValues():
    l = list()
    for i in range(1,30):
        l.append(i**2)
    print(l[:5])
    print(l[-5:])

printValues()