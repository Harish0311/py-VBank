import helpers

"""
Hint:
use helpers.clearConsole() to clear the console.
"""

n = 0
db =[]
isLoggedIn = False
while n != 3 :
    print("Welcome to VBank\n\n\n\n")
    print("What do u wanna do ? : ")
    if not(isLoggedIn):
        print("1). Create account     2). Login      3). Quit")
        n = int(input("Enter Here : "))
    
        if n == 1 :
            name = input("Name     : ")
            no   = input("Number   : ")
            pwd  = input("Password : ")
            data ={
                "Name" : name,
                "Number" : no,
                "Password" : pwd
            }
            length = len(db)
            flag = 0
            for i in range(length):
                if(db[i]["Number"]==no):
                    flag = 1
                    break
                
            if flag==1 :
                print("Account already exists ! ")
                
            else :
                db.append(data)
                print("Account created Successfully !")
            reset = input("Press Enter to continue")
            helpers.clearConsole()
        elif n == 2 :
            no   = input("Number   : ")
            pwd  = input("Password : ")
            length = len(db)
            for i in range(length):
                if(db[i]["Number"]==no):
                    if(db[i]["Password"]==pwd):
                        helpers.clearConsole()
                        isLoggedIn = True
                    else :
                        print("Wrong password")
                        rprint("Account created Successfully !")
                        reset = input("Press Enter to continue")
                        helpers.clearConsole()

    else:
    
        print("1). Transfer money     2). Logout      3). Quit")
        n = int(input("Enter Here : "))
    
                   


    

