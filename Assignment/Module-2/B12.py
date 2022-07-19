#What is the purpose continue statement in python?

#Ans:
"""
    Continue statement is a loop control statement that forces to execute 
    the next iteration of the loop while skipping the rest of the code inside
    the loop for the current iteration only.
==> exm:
    when the continue statement is executed in the loop,the code inside the 
    loop  following the continue statement will be skipped for the current 
    iteration and the next iteration of the loop will begin.
"""
#exm continue prog
for i in range(1,11):
    if i==6:
        continue
    else:
        print(i,end=" ")