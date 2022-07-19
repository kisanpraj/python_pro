a=tuple(input("Enter the value :").split())
print(a)
alpha=["a","b","c","d"]
for i in range(len(a)):
    tv=alpha.index(a[i])
    if tv==len(alpha)-1:
        tv=0
        i=alpha[tv]
        print(i)
    else:
        i=alpha[tv+1]
        print(i)
