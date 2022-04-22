import re

class Customer():
    
    def __init__(self):
        pass
    
    def userID(self):
            
        
        print("************ENTER CREDAINTAILS*********************** ")
        
        '''Phone no starts'''

        regex = "\d{10}"

        while True:
            self.phone_no = input(" Enter Registerd Phone no: ")
            if re.fullmatch("\d{10}", self.phone_no):
                break
            self.phone_no = print("Wrong number")
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
            rc = int(input(" Ration card no as Password: "))

            if self.ration_card == rc:
                print(" ")
                print("         *** VERIFIED ***")
                break
            
            rc = int(input("Re - enter your ration card no: "))
            if self.ration_card == rc:
                print(" ")
                print("         *** VERIFIED ***")
                break
            else:
                print(" ")
                print("*** TOO MANY ATTEMPTS ***")
                exit()
        '''Ration card end'''
# 1. transcation history
# 2. current month allocation 
# 3. logout 


    # def view_user(self):
        
        # print("            ")
        # # print("------------------Display user ------------")
        # print("            ")    
        # print("User ID is : ",self.phone_no)
        # print("Passward: ", self.ration_card)

obj_Customer = Customer()
obj_Customer.userID()
# obj_Customer.view_user()
