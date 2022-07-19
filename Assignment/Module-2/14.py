#write a prog to test whether a passed letter is a vowel or not 

#==>
"""
User=input("Enter the value :")
a=0
numa=0
nume=0
numi=0
numo=0
numu=0

while a < len(User):
    if User[a] == 'a' or User[a] == 'A':
        numa += 1
    if User[a] == 'e' or User[a] == 'E':
        nume =+ 1
    if User[a] == 'i' or User[a] == 'i':
        nume =+ 1
    if User[a] == 'o' or User[a] == 'O':
        nume =+ 1
    if User[a] == 'u' or User[a] == 'U':
        nume =+ 1
    else:
        pass
    a += 1
print(numa,nume,numi,numo,numu)
"""


"""
Ustr=input("Enter the letter :")

if Ustr=='a' or Ustr=='A':
    print("The Vowels of a or A :",Ustr)
if Ustr=='e' or Ustr=='E':
    print("The Vowels of e or E :",Ustr)
if Ustr=='i' or Ustr=='I':
    print("The Vowels of i or I :",Ustr)
if Ustr=='o' or Ustr=='O':
    print("The Vowels of o or O :",Ustr)
if Ustr=='u' or Ustr=='U':
    print("The Vowels of u or U :",Ustr)
else:
    print("try again")
"""
string=input("Enter the Value :")
def Check_v(string,vowels):
    final=[x for x in string if x in vowels]
    print(len(final))
    
    print(final)
vowels='AaEeIiOoUu'
print(Check_v(string,vowels))














    
        