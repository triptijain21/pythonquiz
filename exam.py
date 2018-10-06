import os
import logregmod
import exammod

def main():
    ans=True
    while ans:
        os.system('cls')
        print("                COMPUTER QUIZ")
        print("********************************************************")
        print("  1. Login")
        print("  2. Register")
        print("  3. Exit")
        print("********************************************************")
        ch=int(input("Enter Choice(1-3) :"))
        print("********************************************************")
        if ch==1:
            usid=logregmod.login()
            if usid !="":
                exammod.home(usid)
        elif ch==2:
            logregmod.register()
        elif ch==3:
            ans=False
        else:
            print("Invalid Choice")
        input("Press any key to continue....")

if __name__=="__main__":main()
