#Write a Python prog to check a list is empty or not.

#Ans==>

User=[0]
print(User)

if User != 0:
    print("Its Not Null")
else:
    print("Its Null")


def Check_empty(User):
    if len(User) == 0:
        return "The List is Empty"
    else:
        return "The list is Not Empty"
print(Check_empty(User))