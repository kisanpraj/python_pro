#Write a python prog to count the number of strings where the string length is
#2 or more and the first and last character are same from a given list of strings.

#Ans==>

Ulist=["lol","oppo","kik"]

print("The String count is :",Ulist.count(Ulist))
print("The Length is : ",len(Ulist))

def match_char(words):
    ctr=0

    for i in words:
        if len(i) > 1 or i[0]==i[-1]:
            ctr += 1
    return ctr
print(match_char(input(["Enter the value"])))