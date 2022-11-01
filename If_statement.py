from hashlib import algorithms_guaranteed

#how to use if and else
#name = input("Enter the name of the person at the door ")
#if (name == "Tiny"):
    #print(f"Hello {name}")
#elif (name =="Bunmi"):
    #print("Hello {name}")
#else:
   # print(f"Go back {name}")

#How to use elif
userName =input("Enter your username")
password = input("Enter your password")

if userName == "admin" and password == "1234@admin" :
    print(f"hello you are logged in as admin")
else:
    print("Invalid password or username.Kindly try again." )


