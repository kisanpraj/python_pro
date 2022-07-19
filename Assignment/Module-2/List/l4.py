#Write a Python fun that takes two list and return True if the y 
 #have at least one common member.

#Ans==>

list1=[1,2,3,4]
list2=[6,7,8,9]


def Check_com(list1,list2):
    check=False
    for i in list1:
        for j in list2:
            if i == j:
                check=True
                return check
            else:
                return check
print(Check_com(list1,list2))
