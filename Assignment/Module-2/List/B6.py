#How will you compare two lists?

#Ans==>
def comparelist(l1,l2):
    l1.sort()
    l2.sort()
    if(l1==l2):
        return "Equal"
    else:
        return "Non equal"
l1=list(input("Enter the value : "))
l2=list(input("Enter the value : "))
print("The compare l1 and l2 Ans is : ",comparelist(l1,l2))