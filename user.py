import sys
import json

class user:
    def __init__(self):
        self.sign_details = {}
    
    def User_Signing(self):
        while True:
            name = input("Enter Your Name Here :")
            Ph_Num = input("Enter Your Mobile Number :")
            
            if len(Ph_Num) < 9 :
                print("Invalid Phone Number ")
                break
            
            else:
                email_address = input("Enter Your Mail ID :")
                Address = input("Enter Your Current Address :")
            
                while True:
                    Password = input("Enter Your Password :" )
                    if len(Password) < 8 :
                        print("Password Containt Must be 8 Character")
            
                    else:
                        self.sign_details = {"Name":name,"Phone Number":Ph_Num,"Email Address":email_address,"Address":Address,"Password":Password}
                        with open("User_details.json","w") as f:
                            json.dump(self.sign_details,f,indent=4)
                            print("Your Json Got Created")
                            break
    def login(self,email,password):
        with open("User_details.json","r") as f:
            self.temp = json.load(f)
        
        if email != self.temp["Email Address"]:
            print("Invalid Login ID ❌")
            sys.exit()
        else:
        
            if password != self.temp["Password"]:
                print("Please Enter a Correct Password")
            
            else:
                print("Login Successfully")
                return ""
      
    def update_profile(self):
        with open("User_details.json","r") as f:
            self.temp = json.load(f)
    
        while True:
            print("+="*55)
            print("Pree 0 for Exit")
            print("Pree 1 for Update Name")
            print("Pree 2 for Update Mobile Number")
            print("Pree 3 for Update Email Address ")
            print("Pree 4 for Update Current Address")
            print("Pree 5 for Update Passowrd")
            print("+="*55)
            
            user_input = int(input("Prees a Button ->>"))

            if user_input ==1:
                ename = input("Enter Your New Name :")
                self.temp["Name"] = ename
                with open("User_details.json","w") as f:
                    json.dump(self.temp,f,indent= 4)
                print("Your Name Got Update")
            
            if user_input ==2:
                while True:
                    n_num = input("Enter Your New Mobile Number :")
                    if len(n_num) < 10:
                        print("Invalid Mobile Number")
                    else:
                        self.temp["Phone Number"] = n_num
                        with open("User_details.json","w") as f:
                            json.dump(self.temp,f,indent= 4)
                        print("Your Phone Number Got Update")
                        break
                    
            if user_input ==3:
                nmail = input("Enter Your New Mail ID :")
                self.temp["Email Address"] = nmail
                with open("User_details.json","w") as f:
                    json.dump(self.temp,f,indent= 4)
                print("Your Email ID Got Update")
            
            if user_input ==4:
                naddres = input("Enter Your New Address ID :")
                self.temp["Address"] = naddres
                with open("User_details.json","w") as f:
                    json.dump(self.temp,f,indent= 4)
                print("Your Address Got Update")
                        
            if user_input ==5:
                while True:
                    epass = input("Enter Your Password :" )
                    if len(epass) < 8 :
                        print("Password Containt Must be 8 Character")
                    else:
                        self.temp["Password"] = epass
                        with open("User_details.json","w") as f:
                            json.dump(self.temp,f,indent= 4)
                        print("Your Name Password Update")
                        break    

            if user_input ==0:
                print(self.temp)
                sys.exit()

                
User=user()
print(User.login)

