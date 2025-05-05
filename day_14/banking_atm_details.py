import csv
import logging

logging.basicConfig(filename="Balance_error.log", level=logging.ERROR)

class BankAccount:
    def __init__(self, account_number,password,balance):
        self.account_number = account_number
        self.password = password
        self.balance = balance

# deposit the value function
    def deposit(self, amount):
        try:
            amount = float(input("enter your Deposit Amount:"))

            if amount > 0 :
                self.balance += amount
                with open("deposit_balance_enquire.txt", 'w') as file:
                    file.write(f"Your current balance amount is {self.balance}")
                print(f"Your current balance amount is {self.balance}")
            else:
                print(f" Deposit the valid number")
        except ValueError as e:
            logging.error(f"Deposit error: {e}")
        finally:
            print("Closing the file!...")
            if 'file' in locals():
                file.close()

# withdraw the value function
    def withdraw(self,amount):
        try:
            amount = float(input("enter your Withdraw Amount:"))

            if amount > self.balance :
                raise ValueError("Insufficient balance")
            self.balance -= amount
            with open("withdraw_balance_enquire.txt", 'w') as file:
                file.write(f"Your current balance amount is {self.balance}")
            print(f"Your current balance amount is {self.balance}")
        except ValueError :
            logging.error(f"your Account Balance is Negative and your balance is {self.balance}")
        finally:
            print("Closing the file!...")
            if 'file' in locals():
                file.close()

# balance Enquire the value function
    def balance_enquire(self):
        with open("balance_enquire.txt", 'w') as file:
            file.write(f"Your account Balance is {self.balance}")
        print(f"Your account Balance is {self.balance}")

class AtmBalance(BankAccount):

    def __init__(self, account_number, password,balance = 0):
        super().__init__(account_number, password,balance)

    def bank_acc_details(self):
            file_name = "datafile.csv"
            acc_number = input("enter the acc number:")
            password =  input("enter the password:")
            with open(file_name, 'r', newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["AccountNumber"] == acc_number and row["Password"] == password:
                            print(f"match found {row}")

                            while True:
                                print( " 1.Deposit \n 2.Withdraw \n 3.Balance_Enquire \n 4.Exit")
                                choice = int(input("Your Choice is(1,2,3,4): "))
                                if choice == 1:
                                    self.deposit(0)
                                elif choice == 2:
                                    self.withdraw(0)
                                elif choice == 3:
                                    self.balance_enquire()
                                elif choice == 4:
                                    print("Thank You for logging our Server!...")
                                    return
                                else:
                                    print("your choice is out of the condition")
                else :
                    print("no match found")
                    file_name = "datafile.csv"
                    new_id = int(input("enter the new_id id:"))
                    new_acc_number = input("enter the acc number:")
                    new_password = input("enter the new_password:")

                    with open(file_name, mode='a', newline="") as file:
                        writer = csv.writer(file)
                        writer.writerow([new_id,new_acc_number,new_password])
                        print("New user data has been updated successfully!...")


atm_balance = AtmBalance(account_number="",password="",balance=5000)
atm_balance.bank_acc_details()








