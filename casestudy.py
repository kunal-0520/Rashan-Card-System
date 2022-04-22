import re

class admin():
    
    def __init__(self):
        print("Admin created")
    
    def add_user(self):
            
        print("            ")
        print("**************** RATION CARD DISTRIBUTION SYSTEM ****************")
        print("            ")
        print("------------------ User registration details------------")
        print("            ")
        print("ENTER CUSTOMER DETAILS: ")
        
        while True :
            self.name = input("Name: ")
            if re.fullmatch('^[a-z A-Z]*$',self.name):
                break    
            
            self.name = input("Re enter your name: ")
            if re.fullmatch('^[a-z A-Z]*$',self.name):
                break
            else:
                print("*** TOO MANY ATTEMPTS ***")
                exit()    


        ''' DOB verification starts '''
       
        # Only this type of format is allowed - "dd/mm/yyyy"

        
        regex = ("^([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])(\|-|/)([1-9]|0[1-9]|1[0-2])(\|-|/)([0-9][0-9]|19[0-9][0-9]|20[0-9][0-9])$|^([0-9][0-9]|19[0-9][0-9]|20[0-9][0-9])(\|-|/)([1-9]|0[1-9]|1[0-2])(\|-|/)([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])$")


        while True :
            self.dob = input("Date of Birth: ")
            if re.fullmatch(regex,self.dob):
                break

            self.dob = input("Re-enter your Date of Birth:")
            if re.fullmatch(regex,self.dob):
                break
            else:
                print("*** TOO MANY ATTEMPTS ***")
                exit()    

        ''' DOB verification end'''



        ''' Gender validation for male starts '''
        

        gender_ver = ("^(?:m|M|male|Male|f|F|female|Female)$")

        while True:
            self.gender = input("Enter your gender: ")
            if re.fullmatch(gender_ver,self.gender):
                break
            
            self.gender = input("Re-enter your gender: ")
            if re.fullmatch(gender_ver,self.gender):
                break

            else:
                print(" *** TOO MANY ATTEMTS *** ")        
                exit()


        ''' Gender validation ends '''


        '''Area verification starts '''    
        while True:
            self.area = input("Area name: ")
            if re.match('^[a-z A-Z]*$', self.area):
                break

            self.area = input("Re enter area name: ")
            if re.match('^[a-z A-Z]*$', self.area):
                break
            else:
                print(" *** TOO MANY ATTEMPTS *** ")
                exit()
        pass
        '''Area verifiation ends'''
        
        
        '''Phone no starts'''
        regex = "\d{10}"
        while True:
            self.phone_no = input("Phone no: ")
            if re.fullmatch("\d{10}", self.phone_no):
                break
            
            self.phone_no = input("Re-enter your phone-no: ")
            
            if re.fullmatch("\d{10}", self.phone_no):
                break
            else:
                pass
                print(" ")
                print("*** Too many attempts *** ")
                exit()

        '''Phone no end'''



        '''Ration card starts'''

        while True:

            self.ration_card = 123456
            rc = int(input("Ration card no: "))

            if self.ration_card == rc:
                print(" ")
                print("         *** VERIFIED ***")
                break
            
            rc = int(input("Re - enter your ration card no: "))
            if self.ration_card == rc:
                break
            else:
                print(" ")
                print("*** TOO MANY ATTEMPTS ***")
                exit()
        '''Ration card end'''



    def view_user(self):
        
        print("            ")
        print("------------------Display user ------------")
        print("            ")    
        print("Name of user is: ", self.name)
        print("Date of birth of user is: ", self.dob)
        print("Gender of user is: ", self.gender)
        print("Area of user is: ", self.area)
        print("Phone number of user is : ",self.phone_no)
        print("Ration card no of user is: ", self.ration_card)

obj_admin = admin()

obj_admin.add_user()

obj_admin.view_user()





