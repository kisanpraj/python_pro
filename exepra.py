age=18
id=0
while True:
    try:
        U_age=input("Enter the Value :")
        U_id=input("Enter the Voter_Id :")
        U_age=int(U_age)
        
        print("Your current age is :",U_age,"or id is :",U_id)
        

        if U_age>=age:
            print("It's valid for vote")
            break
        elif U_id==id:
            print("You are not valid for vote")
            break

    except Exception:
        print("It's Not Valid")


    else:
        print("Try Next Year")
        break
    