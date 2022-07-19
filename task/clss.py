#make a task first two num is Even or odd.



len('abcd')
print(len('abcd'))
class Check_Myclass:2
    
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d

    def my_method(self):
        print("a:",self.a)
        print("b:",self.b)
        print("c:",self.c)
        print("d:",self.d)

    def Odd_Even(self):
        if self.a%2==0 or self.b%2==0 and self.c%2==0 or self.d%2==0:
            print(self.a,self.b,self.c,self.d,"Is Even Number")
            return True

        else:
            print(self.a,self.b,self.c,self.d,"Is Odd Number")
            return False


a=int(input("enter the value of a: "))
b=int(input("enter the value of b: "))
c=int(input("enter the value of c: "))
d=int(input("enter the value of d: "))

k=Check_Myclass(a,b,c,d)
k.my_method()
k.Odd_Even()