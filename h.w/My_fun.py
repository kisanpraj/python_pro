def my_fun(a):
    print("Hello world"+" "+a)
my_fun("Demon\n")

k=input("Enter The Value : ")
def Check(k):
    if type(k)==str:
        k=int(k)
        return str(k*2)
    else:
        return (k*2)
print(Check(k))
        
        