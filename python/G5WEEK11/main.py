import os
import datetime
import random as rd
from coffee import Db
from user import User
from report import Report
from inventory import Inventory

items = list(range(0, 25))
status = True
tht1='''
                     COFFEE IS A BEVERAGE THAT PUTS ONE TO SLEEP WHEN NOT 
                  ---------------------------------------------------------
                                         DRANK.
                                      ------------
                    '''
tht2='''
                          I HAVE MEASURED OUT MY LIFE WITH COFFEE SPOONS.
                          -----------------------------------------------
                           
                          
       '''
tht3='''
                        GOOD COMMUNICATION IS JUST AS STIMULATING
                     -------------------------------------------- 
                     AS BLACK COFFEE, AND JUST AS HARD TO SLEEP AFTER.
                     --------------------------------------------------
       '''
tht4=''' 
                        I NEVER DRINK COFFEE AT LUNCH.
                     -----------------------------------
                     I FIND IT KEEPS ME AWAKE FOR THE AFTERNOON.
                     -------------------------------------------

'''
tht5='''
                      IF THIS IS COFFEE, PLEASE BRING ME SOME TEA; 
                      ----------------------------------------
                    BUT IF THIS IS TEA, PLEASE BRING ME SOME COFFEE.
                    ------------------------------------------------
        '''
tht6='''
                  WAY TOO MUCH COFFEE. BUT IF IT WEREN'T FOR THE COFFEE,  
                  ------------------------------------------------------
                     I'D HAVE NO IDENTIFIABLE PERSONALITY WHATSOEVER.
                    -------------------------------------------------
                  '''

tht7='''
                        A MATHEMATICIAN IS A DEVICE 
                     ----------------------------------
                      FOR TURNING COFFEE INTO THEOREMS.
                    ------------------------------------
                               '''
tht8='''
                          HUMANITY RUNS ON COFFEE.
                     ------------------------------------
                                 '''
                                 
th=(tht1,tht2,tht3,tht4,tht5,tht6,tht7,tht8)
print("""  
               ___       ___   ___            ___     _____ ___       ___    ___
     |      | |    |    |   | |   | |\    /| |          |  |   |     |   |  |   |  
     |  /\  | |__  |    |     |   | | \  / | |__        |  |   |     |      |___
     | /  \ | |    |    |     |   | |  \/  | |          |  |   |     |          |
     |/    \| |___ |___ |___| |___| |      | |___       |  |___|     |___|  |___|
   _________________________________________________  __________    _________________________
                         
                      ___   ___   ___   ___   ___   ___
                     |   | |   | |     |     |     | 
                     |     |   | |___  |___  |__   |__ 
                     |     |   | |     |     |     |
                     |___| |___| |     |     |___  |___
                    ____________________________________________________                
          """)
d=datetime.date.today()
t=datetime.datetime.now()
print(" ")
print(" ")
print("        DATE:-",d.strftime("%A, %d %B %Y"))
print(" ")
print("        TIME:-",t.strftime("%H:%M:%S"))
print("")
print('')
choice=rd.choice(th)
print(choice)
print("""
##====================================##  
WELCOME: HERE IS OUR GUIDELINE 
Step 1 = Register to be members
Step 2 = Check in Membership 
Step 3 = Order Coffee
Step 4 = Print Your Receipt
##====================================## 
""")

while status == True:
    print("""
    
##====================================##  
||                                    ||
|| CHOOSE ONE OF THE GIVEN OPTION :-  ||
||____________________________________||
||                                    ||
|| 1. Sell coffee                     ||
|| 2. Report                          ||
|| 3. Inventory                       ||
|| 4. Exit                            ||                           
||                                    ||
##====================================##
""")
    try:       
        menu_option = int(input("\n Select your option: "))
        
        if menu_option == 1:
            os.system("cls||clear")
            print("\n What would you like to order?")
            print("\n Here are your options: ")
            Db().show_coffee()

            def sell_coffee(): 
                status = True
                while status == True:
                    print("""
    
##====================================##  
||                                    ||
|| CHOOSE ONE OF THE GIVEN OPTION :-  ||
||____________________________________||
||                                    ||
|| 1. Register                        ||
|| 2. Member                          ||
|| 3. Guest                           ||
|| 4. Back                            ||                           
||                                    ||
##====================================##
""")
                    choice = input("\n Select your option: ")
                    
                    if choice == "":
                        print("\n~!~!~!~WRONG CHOICE PLEASE ENTER A VALID VALUE~!~!~!~")
                        continue

                    elif choice == "1":
                        
                        first = input("\n First Name: ")
                        if first == "":
                             print("\n~!~!~!~WRONG CHOICE PLEASE ENTER A VALID VALUE~!~!~!~")
                             continue 

                        last = input("\n Last Name: ")
                        if last == "":
                             print("\n~!~!~!~WRONG CHOICE PLEASE ENTER A VALID VALUE~!~!~!~")
                             continue 

                        phone = input("\n Phone Number: ")
                        if phone == "" or None:
                             print("\n~!~!~!~WRONG CHOICE PLEASE ENTER A VALID VALUE~!~!~!~")
                             continue 

                        User().register(firstname=first, lastname=last, phonenumber=phone)

                    elif choice == "2":
                        
                        check = input("\n Have you registered as a member? (y/n): ")
                        low_check = check.lower()

                        if low_check == "y":
                            member_phone = input('\n Type your phone number: ')

                            if member_phone == "" or member_phone.isalpha():
                                    print("\n~!~!~!~WRONG CHOICE PLEASE ENTER A VALID VALUE~!~!~!~")
                                    break
                
                            else:
                                User().is_member(phonenumber=member_phone)
                                member_coffee = input('\n Coffee ID (1,2,3): ')

                                if member_coffee == "" or member_coffee.isalpha():
                                    print("\n~!~!~!~WRONG CHOICE PLEASE ENTER A VALID VALUE~!~!~!~")
                                    continue                           
                            
                                elif member_coffee >= "4":
                                    print("\n~!~!~!~WRONG CHOICE PLEASE ENTER A VALID VALUE~!~!~!~")
                                    continue
                                
                                else:
                                    member_id = input("\n membership ID: ")
          
                                    if member_id == "" or member_coffee.isalpha():
                                        print("\n~!~!~!~WRONG CHOICE PLEASE ENTER A VALID VALUE~!~!~!~")
                                        continue
                                    
                                    else:
                                        User().checkout_member(coffee_id=member_coffee, user=member_id)
                        
                        elif low_check == "n":

                            guest_coffee = input('\n Coffee ID (1,2,3): ')
                            
                            if guest_coffee >= "4":
                                print("\n~!~!~!~WRONG CHOICE PLEASE ENTER A VALID VALUE~!~!~!~")
                                continue
                            
                            else:
                                User().checkout_not_member(user=26, coffee_id=guest_coffee)
                        
                        else:
                            print("\n~!~!~!~WRONG CHOICE PLEASE ENTER A VALID VALUE~!~!~!~")
                            continue

                    elif choice == "3":
                        
                        check = input("\n Want to be our member? (y/n): ")
                        low_check = check.lower()

                        if check == "y":
                            first = input('\n Firstname: ')
                            last = input('\n Lastname: ')
                            phone = int(input("\n Phonenumber: "))
                            User().register(firstname=first, lastname=last, phonenumber=phone)
                            
                        elif check == "n":
                            guest_coffee = input('\n Coffee ID(1,2,3): ')
                            if guest_coffee >= "4":
                                print("\n~!~!~!~WRONG CHOICE PLEASE ENTER A VALID VALUE~!~!~!~")
                                continue
                            else:
                                User().checkout_not_member(user=26, coffee_id=guest_coffee)
                        
                        else:
                            print("\n~!~!~!~WRONG CHOICE PLEASE ENTER A VALID VALUE~!~!~!~")
                            continue
                    
                    elif choice == "4":
                        status = False
                        os.system("cls||clear")

                    else:
                        status = False
                        os.system("cls||clear")
                        break

            sell_coffee()
        
        elif menu_option == 2:
            os.system("cls||clear")
            def show_report():
                status = True        
                
                while status == True:
                    print("""
    
##====================================##  
||                                    ||
|| CHOOSE ONE OF THE GIVEN OPTION :-  ||
||____________________________________||
||                                    ||
|| 1. Resource Report                 ||
|| 2. Sale Report                     ||
|| 3. Customer Report                 ||
|| 4. Back                            ||                           
||                                    ||
##====================================##
""")
                    choice = input("\n Type an option: ")

                    if choice == "1":
                        os.system("cls||clear")
                        report = Report()
                        report.gen_resource()

                    elif choice == "2":
                        os.system("cls||clear")
                        
                        report = Report()
                        print("""
    
##====================================##  
||                                    ||
|| CHOOSE ONE OF THE GIVEN OPTION :-  ||
||____________________________________||
||                                    ||
|| 1. One day's sale Report           ||
|| 2. Date Range Report               ||
|| 3. All sale Report                 ||
|| 4. Back                            ||                           
||                                    ||
##====================================##
""")
                        
                        print("\n Note: Please format your date request like this: MM/DD/YYYY.")
                        swap = input("\n Type an option: ")
                        report.gen_sale(swap=swap)

                    elif choice == "3":
                        os.system("cls||clear")
                        report = Report()
                        print("""
    
##====================================##  
||                                    ||
|| CHOOSE ONE OF THE GIVEN OPTION :-  ||
||____________________________________||
||                                    ||
|| 1. Specific Customer Report        ||
|| 2. All member Report               ||
|| 3. Back                            ||                        
||                                    ||
##====================================##
""")
                        
                        swap = input("\n Type an option: ")
                        report.gen_member(swap=swap)
                    
                    elif choice == "4":
                        status = False
                        os.system("cls||clear")
                    
                    else:
                        status = False
                        os.system("cls||clear")
                        break
            
            print("\n Select a report to open.")
            show_report()

        elif menu_option == 3:
            os.system("cls||clear")
            
            def display_inventory():
                
                status = True

                while status == True:
                    print("""
    
##====================================##  
||                                    ||
|| CHOOSE ONE OF THE GIVEN OPTION :-  ||
||____________________________________||
||                                    ||
|| 1. Water                           ||
|| 2. Sugar                           ||
|| 3. Coffee Beans                    ||
|| 4. Back                            ||                           
||                                    ||
##====================================##
""")
                    choice = input("\n Type an option: ")

                    if choice == "1":
                        os.system("cls||clear")
                        adding = input("\n Enter a number to refill: ")
                        Inventory().refill(user="1", adding=adding)

                    elif choice == "2":
                        os.system("cls||clear")
                        adding = input("\n Enter a number to refill: ")
                        Inventory().refill(user="2", adding=adding)

                    elif choice == "3":
                        os.system("cls||clear")
                        adding = input("\n Enter a number to refill: ")
                        Inventory().refill(user="3", adding=adding)
                    
                    elif choice == "4":
                        status = False
                        os.system("cls||clear")

                    else:
                        status = False
                        os.system("cls||clear")
                        break

            print("\n Select a resource to refill.")
            display_inventory()
        
        elif menu_option == 4:
            os.system("cls||clear")

            while True:

                reuse_tool = input("\n REALLY WANNA EXIT? Y or N: ")
                reuse_tool_UP = reuse_tool.upper()
                
                if reuse_tool_UP == 'N': 
                    break
                
                elif reuse_tool_UP == 'Y':
                    print("\n"
              "      \n"
              "   ##======================================================##\n"
              "   || _____        ___                          ___        ||\n"
              "   ||   |   |   | |   | |\   | |  /      |   | |   | |   | ||\n"
              "   ||   |   |___| |___| | \  | |_/       |___| |   | |   | ||\n"
              "   ||   |   |   | |   | |  \ | | \           | |   | |   | ||\n"
              "   ||   |   |   | |   | |   \| |  \       ___| |___| |___| ||\n"
              "   ##======================================================##\n"
              "\n")

                    quit()

                else:
                    print("~!~!~!~WRONG CHOICE PLEASE ENTER A VALID VALUE~!~!~!~")

        else:
            os.system("cls||clear")
            print("~!~!~!~WRONG CHOICE PLEASE ENTER A VALID VALUE~!~!~!~")

    except ValueError:
        print("\n"
              "      \n"
              "   ##======================================================##\n"
              "   || _____        ___                          ___        ||\n"
              "   ||   |   |   | |   | |\   | |  /      |   | |   | |   | ||\n"
              "   ||   |   |___| |___| | \  | |_/       |___| |   | |   | ||\n"
              "   ||   |   |   | |   | |  \ | | \           | |   | |   | ||\n"
              "   ||   |   |   | |   | |   \| |  \       ___| |___| |___| ||\n"
              "   ##======================================================##\n"
              "\n")
