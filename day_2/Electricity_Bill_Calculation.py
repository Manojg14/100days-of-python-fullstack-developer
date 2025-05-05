"""
Electricity Bill Calculation Project
Objective: Create a program to calculate the electricity bill amount based on the following inputs and rules:
Inputs:
EB Account Number: Input from the user.
Customer Name: Input from the user. The name must include both a first name and a last name.
Account Type Determination:
The EB account number determines the account type:
Residential: Account numbers ending with 77.
Commercial: Account numbers ending with 88.
Any other account number is invalid.
Units Consumed Calculation:
Use the length of the first name to calculate the total units consumed.
Formula: Total Units=(Length of First Name) ÷ 2.7 × 100
Round the result to the nearest integer.
Billing Rules:
Residential Accounts:
Units 0–100: No Charge (0 Rs/unit).
Units 101–200: 4 Rs/unit.
Units >200: 4.5 Rs/unit.
Commercial Accounts:
All units: 10 Rs/unit (flat rate).
Output:
The program should display:
Customer Name
EB Account Number
Account Type (Residential/Commercial)
Total Units Consumed
Total Bill Amount (formatted to two decimal places)
Additional Notes:
Ensure customer name validation (must include both first and last names separated by a space).
Account numbers must strictly end with 77 or 88 for valid input """

def Electricity_bill_calculation():
    # Customer name
    customer_firstname = input("Enter the Customer First Name: ")
    customer_lastname = input("Enter the Customer Last Name: ")
    # EB Account Number
    EB_Account_Number = int(input("Enter your EB Account Number: "))
    # Find total units and find the length of the string
    total_units = (len(customer_firstname) / 2.7) * 100
    # Residential Account
    #account_type = "null"
    if EB_Account_Number % 100 == 77:

        account_type = "Residential"


        # Find charges and Total Units
        if 0 <= total_units <= 100:
            charge = 0
            print(f"Charge: 0 Rs/Units")
        elif 101 <= total_units <= 200:
            charge = total_units * 4
            print(f"Charge: 4 Rs/Unit")
        elif total_units > 200:
            charge = total_units * 4.5
            print(f"Charge: 4.5 Rs/Unit")
        else:
            print("Invalid Units!..!")
    # Commercial Account
    elif EB_Account_Number % 100 == 88:
        charge = total_units * 10
        account_type = "commercial"

    else:
        print("Invalid Account Numbers!...")
    a = 'Electricity bill'
    print(a.center(40,'=')) # for display the output
    print(f"Customer Name: {customer_firstname} {customer_lastname}")
    print(f"EB Account Number: {EB_Account_Number}")
    print(f"ACCOUNT TYPE: {account_type}")
    print(f"TOTAL UNITS:{total_units:.2f}")
    print(f"TOTAL BILL: Rs.{int(charge)}")


Electricity_bill_calculation()








