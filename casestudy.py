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


        ''' Age verification starts '''
        
        while True :
            self.age = int(input("Age: "))
            if self.age < 100:
                break
        pass

        ''' Age verification end'''



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
        print("Age of user is: ", self.age)
        print("Area of user is: ", self.area)
        print("User phone no is : ",self.phone_no)
        print("Ration card no of user is: ", self.ration_card)

obj_admin = admin()

obj_admin.add_user()

obj_admin.view_user()

# obj_admin.check_rationno()




