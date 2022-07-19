#list
a=list((1,2,3))
my_list=[1,2.5,'$',"kisan",3]
print((my_list))
print((a))
a.append(123)
a.extend(my_list)

if "kisan" in a:
    print("y")
print(a)

a[0:2]=["demon"]
print(a)

a.insert(1,"apple")
print(a)
a.remove("apple")
a.pop()
del a[:-1]
a.clear()
print(a)
a.append("a")
a.append("b")
a.append("c")
#a=[input("enter the value")]
for i in a:
    print(i)
print(type(a))
a=list(["apple","mango","grapes"])
for i in range(len(a)):
    print(a[i])
a=list(["apple","mango","grapes"])
i=1
while i < len(a):
    print(a[i])
    i+=1
#i=input("enter the value:")
a=list(["apple","mango","grapes"])
[print (i) for i in a]

a=list(["apple","mango","grapes","kis","xx"])
a.sort()
print(a)
b=[]
 
"""for i in a:
    if "k" in i:
        b.append(i)
        """
b=[i for i in a if i !="kis"]

k=[i for i in range(10)]
k.sort(reverse=1)
print(k)
