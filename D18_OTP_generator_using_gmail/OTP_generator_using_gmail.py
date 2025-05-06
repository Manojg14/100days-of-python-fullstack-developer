import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class OTPGenerator:
    def generate_otp(self, length=6):
        return ''.join(str(random.randint(0, 9)) for _ in range(length))

class EmailSender:
    def send_email(self, sender_email, app_password, receiver_email, subject, body):
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, app_password)
            server.send_message(message)
            server.quit()
            print(f"Email sent to {receiver_email}")
        except Exception as e:
            print("Failed to send email:", e)

class OTPService(OTPGenerator, EmailSender):
    def send_otp(self, sender_email, app_password, receiver_email):
        otp = self.generate_otp()
        subject = "Your OTP Code"
        body = f"Your OTP is: {otp}"
        self.send_email(sender_email, app_password, receiver_email, subject, body)
        return otp


if __name__ == "__main__":
    sender = "manojggm14@gmail.com"
    app_pass =  "hafrydizwwblhtqo"
    receiver = input("Enter recipient email: ")

    service = OTPService()
    generated_otp = service.send_otp(sender, app_pass, receiver)

    user_input = input("Enter the OTP you received: ")
    if user_input == generated_otp:
        print("OTP verified successfully.")
    else:
        print("Incorrect OTP.")
