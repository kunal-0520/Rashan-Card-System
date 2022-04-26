from ast import While
import re
#first name
#last name 
#dob
#ration no

class family():


    def fam1(self):
        
        print(" ")
        print("          *** Enter your Family Details ***     ")
        print(" ")
        print ("Enter your family member details ")
        print(" ")


        #First name starts 

        while True:    
            self.firstname1 = input("Enter your First name: ")
            if re.fullmatch("^[A-Za-z]*$",self.firstname1):
                break

            self.firstname1 = input("Re enter your First name: ")        
            if re.fullmatch("^[A-Za-z]*$",self.firstname1):
                break

            else:
                print(" *** Too many attempts *** ")
                exit()

        #First name ends


        #Last name starts
        while True:    
            self.Lastname1 = input("Enter your Last name: ")
            if re.fullmatch("^[A-Za-z]*$",self.Lastname1):
                break

            self.Lastname1 = input("Re enter your Last name: ")        
            if re.fullmatch("^[A-Za-z]*$",self.Lastname1):
                break

            else:
                print(" *** Too many attempts *** ")
                exit()            

            # Last name ends




        #Dob Starts

        regex = ("^([0-9][0-9]|19[0-9][0-9]|20[0-9][0-9])(\.|-|/)([1-9]|0[1-9]|1[0-2])(\.|-|/)([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])$")

        while True :
            self.dob1 = input("Date of Birth: ")
            if re.fullmatch(regex,self.dob1):
                break

            self.dob1 = input("Re-enter your Date of Birth:")
            if re.fullmatch(regex,self.dob1):
                break
            else:
                print("*** TOO MANY ATTEMPTS ***")
                exit()    

        #Dob ends 

        
        #Ration card starts

        while True:

            self.ration_card1 = 200001

            rc = int(input("Ration card no: "))

            if self.ration_card1 == rc:
                print(" ")
                print("   Go ahead")
                break
            
            rc = int(input("Re - enter your ration card no: "))
            if self.ration_card1 == rc:
                break
            else:
                print(" ")
                print("*** TOO MANY ATTEMPTS ***")
                exit()

        #Ration card end'''


  # Do you want to add another member 
  # input yes or no
  # if yes then call fam
  # if no exit()  


    def fam_det1(self):
        print(" ")
        print(" -- Family details of member 1 -- ")
        print(" ")

        print("Firstname : ", self.firstname1)
        print("Lastname : ", self.Lastname1)
        print("Date of birth id : ", self.dob1)
        print("Ration no: ",self.ration_card1)
        print(" ")
        print(" ")



    def fam2(self):
        
        print(" ")
        print ("Enter your family member details ")
        print(" ")
        while True:    
            self.firstname2 = input("Enter your First name: ")
            if re.fullmatch("^[A-Za-z]*$",self.firstname2):
                break

            self.firstname2 = input("Re enter your First name: ")        
            if re.fullmatch("^[A-Za-z]*$",self.firstname2):
                break

            else:
                print(" *** Too many attempts *** ")
                exit()

        #First name ends


        #Last name starts
        while True:    
            self.Lastname2 = input("Enter your Last name: ")
            if re.fullmatch("^[A-Za-z]*$",self.Lastname2):
                break

            self.Lastname2 = input("Re enter your Last name: ")        
            if re.fullmatch("^[A-Za-z]*$",self.Lastname2):
                break

            else:
                print(" *** Too many attempts *** ")
                exit()            

            # Last name ends




        #Dob Starts

        regex = ("^([0-9][0-9]|19[0-9][0-9]|20[0-9][0-9])(\.|-|/)([1-9]|0[1-9]|1[0-2])(\.|-|/)([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])$")

        while True :
            self.dob2 = input("Date of Birth: ")
            if re.fullmatch(regex,self.dob2):
                break

            self.dob2 = input("Re-enter your Date of Birth:")
            if re.fullmatch(regex,self.dob2):
                break
            else:
                print("*** TOO MANY ATTEMPTS ***")
                exit()    

        #Dob ends 

        
        #Ration card starts

        while True:

            self.ration_card2 = 200001

            rc = int(input("Ration card no: "))

            if self.ration_card2 == rc:
                print(" ")
                print("   Go ahead")
                break
            
            rc = int(input("Re - enter your ration card no: "))
            if self.ration_card2 == rc:
                break
            else:
                print(" ")
                print("*** TOO MANY ATTEMPTS ***")
                exit()

        #Ration card end'''


    
    def fam_det2(self):
        print(" ")
        print(" -- Family detail of member 2 -- ")
        print(" ")

        print("Firstname : ", self.firstname2)
        print("Lastname : ", self.Lastname2)
        print("Date of birth id : ", self.dob2)
        print("Ration card no: ",self.ration_card2)
        print(" ")
        print(" ")


obj_family = family()

obj_family.fam1()

while True:
    print(" ")
    print("Do you want to add more members ? ")
    choice = input("")
    if choice == "Y":
        obj_family.fam2()
    if choice == "N":
        obj_family.fam_det1()
        obj_family.fam_det2()
        break