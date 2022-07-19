#Write the python prog to remove duplicates from list.

#Ans==>

User=[10,20,30,20,10,40,50,60,70]
dub_User=set()
uniq_User=[]

for i in User:
    if i not in dub_User:
        uniq_User.append(i)
        dub_User.add(i)

print(uniq_User)