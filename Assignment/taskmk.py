#The Banking Sys

UserNo=int(input("Enter the  NO : "))
UserName=input("Enter Your Name : ")
UserSalary=input("Enter Your Salary : ")
class Bank:
    def User(self,UserNo,UserName,UserSalary):
        self.UserNo = UserNo
        self.UserName = UserName
        self.UserSalary = UserSalary

    def show(self):
        print("No : ",UserNo,"Name : ",UserName,"Salary : ",UserSalary)
class client:
    def credit(self,UserSalary):
        Updatesalary = UserSalary
        Updatesalary = Updatesalary + UserSalary
        print("The Update Salary Is :",Updatesalary)


obj=Bank()
obj.show()
obj=client()

obj.credit(2000)


    
