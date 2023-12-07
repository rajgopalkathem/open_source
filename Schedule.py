class Schedule_Service:
    def __init__(self, name, phone):
        #cust_details = ["Rajagopal", "8585194197"]
        self.name = name
        self.phone = phone
        print("Initialize the data")        
        
    
    def validate_customer(self):
        print("Valid customer checking")
        #print(len(self.phone))
        if (self.phone == ""):
            print("Please enter the phone")
            return False
        elif (not self.phone.isnumeric()) or ((int(len(self.phone)) != 10)):
            print("Please enter the phone in numbers and it should be only 10 digits")
            return False        
        #elif ((int(len(self.phone)) > 10)):
         #   print("Please enter the phone in 10 digits")
         #   return False
        
        
        if(len(self.name) > 0):
            first_letter = self.name[0]
            print(self.name)
            
            if(not first_letter.isalpha()):
                print("Please enter your name correctly, first letter should be a numeric")
                return False
                
        return True
    
    def get_next_customer(self):
        #cust_details = ["Rajagopal", "8585194197"]
        #cust_details[0] = self.name
        #cust_details[1] = self.phone
        #check the customer if premium or not
        if(self.name == "Rajagopal"):
            print("Premium customer")
        else:
            print("Reguler customer")
        self.customer_checkin()
        #return cust_details
        
    def customer_checkin(self):
        try:
            if (self.validate_customer() == True):
                #insert the db
                print(self.name + " User inserted")
            else:
                print("Issue with the database insert")
        except Exception as err:
            print(err)
        finally:
            #close the db conn
            print("Clean up the system services")
                

#if(__name__ == __main__):
               
print("Please enter customer details")               
name = input()
phone = input()
#cust = Schedule_Service("Rajagopal", "8585194197")
cust = Schedule_Service(name, phone)

#cust_details = ["Rajagopal", "8585194197"]
#print(cust_details)
cust.get_next_customer()
#cust.validate_customer()

#cust = Schedule_Service("Rajagopal", "")
#cust.get_next_customer()