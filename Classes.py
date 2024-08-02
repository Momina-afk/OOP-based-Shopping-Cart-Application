from abc import ABC, abstractmethod
from datetime import datetime
import os
from GUIintro import show_welcome_and_website
from GUIending import show_Goodbye
# Class to handle user data
class Carry_you:
    def __init__(self):
        self.users = self.load_users()
    def load_users(self):
        users = {}
        try:
            with open('users.txt', 'r') as file:
                for line in file:
                    try:
                        user_id, password = line.strip().split(',')
                        users[user_id] = password
                    except ValueError:
                        print("Error: Invalid format in users.txt")
        except FileNotFoundError:
            print("Warning: users.txt not found.")
        return users
    def login(self, user_id, password):
        if user_id in self.users and self.users[user_id] == password:
            return True
        elif user_id not in self.users:
            print(f"User ID '{user_id}' not found. Would you like to sign up? (yes/no)")
            if input().lower() == 'yes':
                self.signup(user_id, password)
                return True
            else:
                print("Login failed. Exiting program.....")
                return False      
        else:
            print("Incorrect password. Try again")
            return False
    def signup(self, user_id, password):
        self.users[user_id] = password
        with open('users.txt', 'a') as file:
            file.write(f'{user_id},{password}\n')
# Abstract class to handle flight data
class List_of_flights(ABC):
    def __init__(self):
        self.flights = self.load_flights()
    def load_flights(self):
        flights = []
        try:
            with open('flights2.txt', 'r') as file:
                for line in file:
                    try:
                        data = line.strip().split(',')
                        if len(data) == 9:
                            flight = {
                                "departure_city": data[0].strip(), "arrival_city": data[1].strip(), "airline_name": data[2].strip(),
                                "schedule": data[3].strip(), "date": data[4].strip(), "duration":data[5].strip(),
                                "class_type": data[6].strip(), "price": float(data[7].strip()), "flight_number": data[8].strip()
                            }
                            flights.append(flight)
                        else:
                            print(f"Error: Invalid format in flights.txt - {line.strip()}")
                    except (ValueError, IndexError):
                        print(f"Error: Unable to parse line in flights.txt - {line.strip()}")
        except FileNotFoundError:
            print("Warning: flights.txt not found.")
        return flights
    @abstractmethod
    def ask_departure_city(self):
        pass
    @abstractmethod
    def ask_arrival_city(self):
        pass
    @abstractmethod
    def ask_ticket_quantity(self):
        pass
# Class to handle flight operations
class Flight(List_of_flights):
    def __init__(self):
        super().__init__()
    def ask_departure_city(self):
        while True:
            self.departure_city = input("Enter departure city: ").strip()
            if self.departure_city:
                break
            else:
                print("Error: Please enter a valid departure city.")
    def ask_arrival_city(self):
        while True:
            self.arrival_city = input("Enter arrival city: ").strip()
            if self.arrival_city:
                break
            else:
                print("Error: Please enter a valid arrival city.")
    def ask_ticket_quantity(self):
        while True:
            try:
                self.ticket_quantity = int(input("Enter quantity of tickets: "))
                if self.ticket_quantity > 0:
                    break
                else:
                    print("Error: Quantity must be greater than zero.")
            except ValueError:
                print("Error: Please enter a valid number.")
    def check_available_flights(self):
        print(f"Searching for flights from {self.departure_city} to {self.arrival_city}....")
        available_flights = []
        for flight in self.flights:
            if flight["departure_city"].lower() == self.departure_city.lower() and flight["arrival_city"].lower() == self.arrival_city.lower():
                available_flights.append(flight)
        if available_flights:
            for flight in available_flights:
                print(f"Flight Number: {flight['flight_number']}, Airline: {flight['airline_name']}, Schedule: {flight['schedule']}, Date: {flight['date']}, Duration: {flight['duration']}, Class: {flight['class_type']}, Price: {flight['price']}")
            return available_flights
        else:
            print("No flights available.")
            return []
# Class to handle passenger details
class Passenger:
    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email
    def add_phone(self, phone):
        while True:
            if phone.isdigit() and len(phone) == 10:  # Validate phone number format
                self.phone = phone
                break
            else:
                print("Error: Please enter a valid 10-digit phone number.")
                phone = input("Enter passenger phone: ")
                self.phone=phone

# Class to handle ticket history
class History:
    def __init__(self, user_id):
        self.user_id = user_id
        self.history = self.load_history()
    def load_history(self):
        history = []
        filename = f'{self.user_id}_history.txt'
        try:
            with open(filename, 'r') as file:
                for line in file:
                    try:
                        ticket_info = eval(line.strip())
                        history.append(ticket_info)
                    except SyntaxError:
                        print(f"Error: Invalid format in {self.user_id}_history.txt - {line.strip()}")
        except FileNotFoundError:
            print(f"Warning: {self.user_id}_history.txt not found.")
        return history
    def add_to_history(self, ticket_info):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ticket_info['timestamp'] = timestamp
        self.history.append(ticket_info)

    def display_history(self):
        if self.history:
            for ticket in self.history:
                print(f"Timestamp: {ticket['timestamp']}, Flight Number: {ticket['flight_number']}, Airline: {ticket['airline_name']}, Schedule: {ticket['schedule']}, Date: {ticket['date']}, Price: {ticket['price']}, Passenger: {ticket['passenger_name']}, Gmail: {ticket['passenger_email']}, Contact: {ticket['passenger_phone']}")
        else:
            print("No history available.")

    def save_history(self):
        filename = f'{self.user_id}_history.txt'
        with open(filename, 'w') as file:
            for ticket in self.history:
                file.write(f"{ticket}\n")

    def delete_ticket_history(self, flight_number):
        filename = f'{self.user_id}_{flight_number}_history.txt'
        try:
            with open(filename, 'r') as file:
                # Read the file to confirm its existence and contents (optional step)
                pass
        except FileNotFoundError:
            print(f"History file for flight {flight_number} not found.")
            return
        
        # If file exists, perform actions to delete it
        try:
            os.remove(filename)
            print(f"History file for flight {flight_number} deleted.")
        except Exception as e:
            print(f"Error deleting history file for flight {flight_number}: {e}")

# Class to handle ticket cancellation
class Cancellation:
    def __init__(self, history):
        self.history = history

    def cancel_ticket(self, flight_number):
        ticket_info = next((ticket for ticket in self.history.history if ticket['flight_number'] == flight_number), None)
        if ticket_info:
            self.history.history.remove(ticket_info)
            self.history.save_history()
            self.history.delete_ticket_history(flight_number)  # Call method to delete ticket history file
            print("Ticket cancelled.")
        else:
            print("Ticket not found.")
