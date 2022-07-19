#Write a pyton fun that takes a list and returns a new list with unique elements of the first list.

#Ans==>

def unique_list(User):
    a=[]
    for i in User:
        if i not in a:
            a.append(i)
            
    return a
print(unique_list([1,2,3,3,3,4,5]))