#Write a Python prog to convert a list of Characters into a string.

#ans==>
User=['abcd']
a=['a','b','c','d']
print(a)

def convert(a):
    str1=" "
    return(str1.join(a))
print(convert(a))

def con(User):
    str1=" "
    for i in User:
        str1 += i
    return str1
print(con(User))


