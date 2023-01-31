email="santosh@gmail.com"
pword=1234
otp=5678
cemail=input("Enter the mail : ")
cpword=int(input("enter the password : "))
if(email==cemail and pword==cpword):
    print("Login successfully")
    cotp=int(input("Enter the otp : "))
    if(otp==cotp):
        print("your Order placed successfully")
    else:
        print("Order failed due to wrong otp")
elif(email!=cemail and pword==cpword):
    print("Login failed due to wrong mail")
elif(email==cemail and pword!=cpword):
    print("Login failed due to wrong password")
else:
    print("Login failed due to wrong mail and password")
