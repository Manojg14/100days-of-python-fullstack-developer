from faker import Faker
import csv

fake = Faker()

def generate_bank_card_data(filename='bank_cards.csv', records=50):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Card Type", "Card Number", "Expiration Date", "CVV"])

        print("Sample Bank Card Details:\n")
        for _ in range(records):
            name = fake.name()
            card_type = fake.credit_card_provider()
            card_number = fake.credit_card_number(card_type=None)
            card_expire = fake.credit_card_expire()
            card_security = fake.credit_card_security_code()

            print(f"Name: {name}")
            print(f"Card Type: {card_type}")
            print(f"Card Number: {card_number}")
            print(f"Expiration Date: {card_expire}")
            print(f"CVV: {card_security}")
            print("-" * 40)

            writer.writerow([name, card_type, card_number, card_expire, card_security])


generate_bank_card_data()
