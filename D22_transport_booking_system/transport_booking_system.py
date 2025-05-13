import csv
import os
import logging

file_path = 'tickets.csv'


logging.basicConfig(
    filename='transport_booking_system.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Transport:
    def __init__(self, passenger_name):
        self.passenger_name = passenger_name

    def book_ticket(self):
        raise NotImplementedError("Subclasses must override book_ticket()")

    def get_ticket_info(self):
        raise NotImplementedError("Subclasses must override get_ticket_info()")

    def get_bill(self):
        name, mode, seat, fare = self.get_ticket_info()
        print("\n============ TICKET BILL ==========")
        print(f"Passenger Name : {name}")
        print(f"Transport Mode : {mode}")
        print(f"Seat / Coach   : {seat}")
        print(f"Fare           : {fare}")
        print("====================================\n")


class Bus(Transport):
    def book_ticket(self):
        print(f"Bus ticket booked for {self.passenger_name}. Seat No: B12. Fare: ₹350")

    def get_ticket_info(self):
        return [self.passenger_name, "Bus", "B12", "₹350"]


class Train(Transport):
    def book_ticket(self):
        print(f"Train ticket booked for {self.passenger_name}. Coach: S3. Fare: ₹750")

    def get_ticket_info(self):
        return [self.passenger_name, "Train", "S3", "₹750"]


class Flight(Transport):
    def book_ticket(self):
        print(f"Flight ticket booked for {self.passenger_name}. Seat: 22A. Fare: ₹3200")

    def get_ticket_info(self):
        return [self.passenger_name, "Flight", "22A", "₹3200"]


class Operation:
    def __init__(self):
        self.bookings = []
        self.load_bookings()

    def load_bookings(self):
        if os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding='utf-8') as file:
                    reader = csv.reader(file)
                    next(reader, None)  # Skip header
                    self.bookings = list(reader)
            except Exception as e:
                logging.error(f"Error loading bookings: {e}")
                print("Error loading bookings, please check the log file.")

    def save_ticket_to_csv(self, ticket_data):
        try:
            file_exists = os.path.isfile(file_path)
            with open(file_path, 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                if not file_exists:
                    writer.writerow(["Passenger Name", "Transport Mode", "Seat/Coach", "Fare"])
                writer.writerow(ticket_data)
        except Exception as e:
            logging.error(f"Error saving ticket to CSV: {e}")
            print("Error saving ticket, please check the log file.")

    def save_all_bookings(self):
        try:
            with open(file_path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["Passenger Name", "Transport Mode", "Seat/Coach", "Fare"])
                writer.writerows(self.bookings)
        except Exception as e:
            logging.error(f"Error saving all bookings to CSV: {e}")
            print("Error saving bookings, please check the log file.")

    def confirm_booking(self, transport_obj: Transport):
        try:
            transport_obj.book_ticket()
            ticket_info = transport_obj.get_ticket_info()
            self.save_ticket_to_csv(ticket_info)
            self.bookings.append(ticket_info)
            print(f"Ticket saved to {file_path}\n")
            transport_obj.get_bill()
        except Exception as e:
            logging.error(f"Error confirming booking for {transport_obj.passenger_name}: {e}")
            print("Error confirming booking, please check the log file.")

    def process_booking(self):
        try:
            name = input("Enter passenger name: ")
            print("\nChoose transport:\n1. Bus\n2. Train\n3. Flight")
            choice = input("Enter your choice (1/2/3): ")

            if choice == '1':
                transport = Bus(name)
            elif choice == '2':
                transport = Train(name)
            elif choice == '3':
                transport = Flight(name)
            else:
                print("Invalid transport choice!\n")
                return

            self.confirm_booking(transport)
        except Exception as e:
            logging.error(f"Error processing booking: {e}")
            print("Error processing booking, please check the log file.")

    def view_bookings(self):
        try:
            if not self.bookings:
                print("No bookings to show.\n")
                return
            print("\n======== Existing Bookings ========")
            for i, booking in enumerate(self.bookings, start=1):
                print(f"{i}. Passenger: {booking[0]}, Mode: {booking[1]}, Seat: {booking[2]}, Fare: {booking[3]}")
        except Exception as e:
            logging.error(f"Error viewing bookings: {e}")
            print("Error viewing bookings, please check the log file.")

    def modify_booking(self):
        try:
            self.view_bookings()
            if not self.bookings:
                return

            booking_index = int(input("Enter the booking number to modify: ")) - 1
            if booking_index < 0 or booking_index >= len(self.bookings):
                print("Invalid booking number!")
                return

            print("\nModify booking details:")
            print("1. Change Transport Mode")
            print("2. Change Seat/Coach")
            print("3. Cancel Booking")

            choice = input("Enter your choice (1/2/3): ")

            transport_details = {
                '1': {'mode': 'Bus', 'seat': 'B12', 'fare': '₹350'},
                '2': {'mode': 'Train', 'seat': 'S3', 'fare': '₹750'},
                '3': {'mode': 'Flight', 'seat': '22A', 'fare': '₹3200'}
            }

            if choice == '1':
                print("\nChoose new transport mode:\n1. Bus\n2. Train\n3. Flight")
                transport_choice = input("Enter your choice: ")

                if transport_choice in transport_details:
                    self.bookings[booking_index][1] = transport_details[transport_choice]['mode']
                    self.bookings[booking_index][2] = transport_details[transport_choice]['seat']
                    self.bookings[booking_index][3] = transport_details[transport_choice]['fare']
                else:
                    print("Invalid transport choice!")
                    return

            elif choice == '2':
                new_seat = input("Enter new seat/coach: ")
                self.bookings[booking_index][2] = new_seat

            elif choice == '3':
                del self.bookings[booking_index]
                print("Booking canceled successfully!")
                self.save_all_bookings()
                return

            else:
                print("Invalid choice!")
                return

            self.save_all_bookings()
            print("Booking modified successfully!")

        except Exception as e:
            logging.error(f"Error modifying booking: {e}")
            print("Error modifying booking, please check the log file.")

    def main(self):
        while True:
            try:
                print("======== Transport Booking System ========")
                print("1. Book Ticket")
                print("2. Modify Booking")
                print("3. Exit")

                option = input("Enter your choice (1/2/3): ")

                if option == '1':
                    self.process_booking()
                elif option == '2':
                    self.modify_booking()
                elif option == '3':
                    print("Thank you for using the Transport Booking System!")
                    break
                else:
                    print("Invalid menu option. Please try again.\n")
            except Exception as e:
                logging.error(f"Error in main loop: {e}")
                print("An unexpected error occurred. Please check the log file.")


if __name__ == '__main__':
    operation = Operation()
    operation.main()
