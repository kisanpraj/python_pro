#Explain split(),sub(),subn() methods of "re" module in python?

#Ans==>
#split()

User="How are you ?"
admin=User.split()
print(admin)

#==>
#sub()

import re
text="how are u? u in u in u uu u uuu"
print(re.sub(r'\b[Uu]\b','you',text))

#==>
#subn()

import re
text="how are u? u in u in u uu u uuu"
print(re.subn(r'\b[Uu]\b','you',text))
