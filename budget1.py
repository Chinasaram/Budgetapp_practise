"""
Creating a budget app using classes and objects. Got hooked defining the transfer method
"""

class Budget:

    def __init__(self, category, balance):
        self.category = category
        self.balance = balance


    def deposit(self):
        userDeposit = int(input("How much would you like to deposit?: "))
        self.balance += userDeposit
        if userDeposit > 1000:
            print("Deposit successful! \nCurrent Balance for", self.category, "is", self.balance)
        else:
            print("Input a valid amount")
     

    def withdrawal(self):
        userWithdrawal = int(input("How much would you want to withdraw?: "))
        if userWithdrawal <= self.balance:
            self.balance -= userWithdrawal
            print("Withdrawal successful \nYour current balance for", self.category, "is", self.balance)
        else:
            print("Insufficient funds! Try again")


    def check_balance(self):
        print(f"Your current balance for {self.category} is {self.balance}")

    

    def transfer(self):

        withdrawFrom = input("What category would you want to transfer from?: ")
        amountTransfer = int(input("How much would you want to transfer? "))
        if withdrawFrom in ["Food", "Clothing", "Housing", "Personal Care", "Data", "Transportation"] and amountTransfer <= self.balance:
             self.balance -= amountTransfer
             print(f"Your current balance for {self.category} is {self.balance}")
        else:
            print("Please select a valid category!")
        transferTo = input("What category would you want to tranfer to?: ")

"""
Still struggling to understand the concept of objects and how you can manipulate their parameters. I'll do more research and update my code on this budget app 
subsequently. I understand my codes are sort of everywhere at the moment, but I'll sure get better. What follows is a way of testing my codes, however I know
this is not the proper way to do it but I'll learn that too.
"""
        
        



foodBudget = Budget("Food", 5000)
housingBudget = Budget("Housing", 0)
clothingBudget = Budget("Clothing", 0) 
personalCareBudget = Budget("Personal Care", 0)
dataBudget = Budget("Data", 0)
transportationBudget = Budget("Transportation", 0)


database = {
    'Budcustomer': ['Elon', 'Musk', '2222', 'budgetapp_practice@zuriteam.co' ]
}


print("=" * 60)   
import time
print("   ~~~~~~~~~~~  WELCOME TO BUGETTI  ~~~~~~~~~~~")  
print("Today is a good day to budget your earnings, login to get started!")
time.sleep(2)
print("  >>>> Input your details to login <<<<  ")

userIdFromUser = input("UserID: ")
passwordFromUser = input("Password: ")
for userId, userDetails in database.items():
    if(userId == userIdFromUser) and (userDetails[2] == passwordFromUser):

        print("Hello {}, what would you want to do today? Select an option to begin.".format(database['Budcustomer'][0]))
        print("1. Deposit")
        print("2. Withdrawal")
        print("3. Transfer")
        print("4. Check Balance")
        print("These are the available categories: \n-Food \n-Clothing \n-Housing \n-Personal Care \n-Data \n-Transportation")
        userSelection = int(input("Select an option: "))
        print("=" * 60)

        if(userSelection == 1):
            userCategory = input("What Budget category would you want to deposit into? ")
            if userCategory in ["food", "Food"]:
                foodBudget.deposit()
                print("Thanks for using Budgetti")

            elif userCategory in ["cloth", "Cloth", "Clothing", "clothing"]:
                clothingBudget.deposit()
                print("Thanks for using Budgetti")

            elif userCategory in ["housing", "rent", "Housing", "Rent"]:
                housingBudget.deposit()
                print("Thanks for using Budgetti")

            elif userCategory in ["Personal Care", "personal care", "Personal care", "personal Care"]:
                personalCareBudget.deposit()
                print("Thanks for using Budgetti")

            elif userCategory in ["Transportation", "transportation"]:
                transportationBudget.deposit()
                print("Thanks for using Budgetti")

            elif userCategory in ["Data", "data"]:
                dataBudget.deposit()
                print("Thanks for using Budgetti")

            else:
                print("You have chosen an invalid category!")


        elif userSelection == 2:
            userCategory = input("What Budget category would you want to witdraw from? ")
            if userCategory in ["food", "Food"]:
                foodBudget.withdrawal()
                    

            elif userCategory in ["cloth", "Cloth", "Clothing", "clothing"]:
                clothingBudget.withdrawal()
                    

            elif userCategory in ["housing", "rent", "Housing", "Rent"]:
                housingBudget.withdrawal()
                   

            elif userCategory in ["Personal Care", "personal care", "Personal care", "personal Care"]:
                personalCareBudget.withdrawal()
                    

            elif userCategory in ["Transportation", "transportation"]:
                transportationBudget.withdrawal()
                    

            elif userCategory in ["Data", "data"]:
                dataBudget.withdrawal()
                    
            else:
                print("You have selected an invalid category!")

        elif userSelection == 3:
            pass

        elif userSelection == 4:
            userCategory = input("What Budget category would you want to check for balance? ")
            if userCategory in ["food", "Food"]:
                foodBudget.check_balance()
                    

            elif userCategory in ["cloth", "Cloth", "Clothing", "clothing"]:
                clothingBudget.check_balance()
            

            elif userCategory in ["housing", "rent", "Housing", "Rent"]:
                housingBudget.check_balance()
                    

            elif userCategory in ["Personal Care", "personal care", "Personal care", "personal Care"]:
                personalCareBudget.check_balance()
                    

            elif userCategory in ["Transportation", "transportation"]:
                transportationBudget.check_balance()
                    

            elif userCategory in ["Data", "data"]:
                dataBudget.check_balance()
                   

            else:
                print("You have chosen an invalid category!")
                

        else:
            print("Please select a valid option, try again!")


    else:
        print('Invalid account or password')
