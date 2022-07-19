class my:
    var1=15
    def __init__(self,a):
        self.a=a
        print("in const")

    def show(self):
        print(self.a,'in const')

    @classmethod
    def classmeth(cls,self):
        print(cls.var1)
        

obj=my(50)

obj.show()
obj.classmeth(12)
