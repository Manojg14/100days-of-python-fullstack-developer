import csv
import logging
from datetime import datetime


logging.basicConfig(
    filename="error_log.log",
    level=logging.ERROR,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

class PaymentMethod:
    def validate(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def process_payment(self, amount):
        raise NotImplementedError("Subclasses must implement this method.")

class CreditCardPayment(PaymentMethod):
    def validate(self):
        return True

    def process_payment(self, amount):
        # Simulate payment logic
        pass

class UPIPayment(PaymentMethod):
    def validate(self):
        return True

    def process_payment(self, amount):
        pass

class PayPalPayment(PaymentMethod):
    def validate(self):
        return True

    def process_payment(self, amount):
        pass

class PaymentGateway:
    def make_payment(self, payment_method: PaymentMethod, amount: float, payment_type: str):
        try:
            if payment_method.validate():
                payment_method.process_payment(amount)
                self.log_transaction(payment_type, amount, "Success")
            else:
                self.log_transaction(payment_type, amount, "Validation Failed")
        except Exception as e:
            self.log_error(f"Exception during {payment_type} payment of ₹{amount}: {str(e)}")

    def log_transaction(self, method, amount, status):
        try:
            with open("successful_transactions.log", mode='a') as file:
                file.write(f"{datetime.now()} | {method} | Rs.{amount} | {status}\n") # ₹
        except Exception as e:
            self.log_error(f"Error writing successful transaction: {str(e)}")

    def log_error(self, error_msg):
        logging.error(error_msg)


if __name__ == "__main__":
    gateway = PaymentGateway()
    gateway.make_payment(CreditCardPayment(), 2500.0, "Credit Card")
    gateway.make_payment(UPIPayment(), 400.0, "UPI")
    gateway.make_payment(PayPalPayment(), 999.0, "PayPal")
