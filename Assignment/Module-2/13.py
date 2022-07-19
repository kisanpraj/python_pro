#write the prog find the area 

#1>Triangle(Base & Height)

#==>
print("Triangle of Area :")
Height=int(input("Enter the value of Height :"))
print("The Value of Hight :",Height)
Base=int(input("Enter the value of Base :"))
print("The Value of Hight :",Base)

def Triangle(Height,Base):
    t=1/2*Height*Base
    print("The Area of Triangle is :",t)
    
print(Triangle(Height,Base))


#2>Circle

#==>
print("Area of Circle :")
Radius=int(input("Enter the value of Radius :"))
def Circle(Radius):
    a=3.14*Radius*Radius
    print("The area of Circle is :",a)
print(Circle(Radius))