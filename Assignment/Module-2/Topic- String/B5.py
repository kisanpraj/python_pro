#How do you perform pattern matching in Python? Explain


#Ans==>

import re
phoneNumR=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo=phoneNumR.search("My num is 415-415-4141.")
#areacode,mainnumber=mo.groups()
print("phone num found: " ,mo.group())
#print(mainnumber)
