# Main function to run the program
from Classes import *
def main():
    carry_you = Carry_you()

    user_id = input("Enter user ID: ")
    password = input("Enter password: ")

    if carry_you.login(user_id, password):
         print("Login successful!")
    else:
        return False
    history = History(user_id)

    while True:
        print("Choose an option:\n 1. Buy a ticket\n 2. View history\n 3. Check out\n 4. Cancel a ticket\n 5. Exit\n")
        try:
            choice = int(input())

            if choice == 1:
                flight = Flight()
                flight.ask_departure_city()
                flight.ask_arrival_city()
                flight.ask_ticket_quantity()
                available_flights = flight.check_available_flights()

                if available_flights:
                    selected_tickets = []
                    for _ in range(flight.ticket_quantity):
                        print("Enter the flight number you want to book:")
                        flight_number = input().strip()
                        selected_flight = next((f for f in available_flights if f['flight_number'] == flight_number), None)
                        while not selected_flight:
                            print("Invalid flight number. Please choose from the available flights.")
                            flight_number = input().strip()
                            selected_flight = next((f for f in available_flights if f['flight_number'] == flight_number), None)

                        passenger_name= input("Enter passenger name: ")
                        passenger_phone= input("Enter passenger phone: ")
                        passenger_email= input("Enter passenger email: ")

                        passenger = Passenger(passenger_name,passenger_phone,passenger_email)
                        passenger.add_phone(passenger_phone)

                        selected_tickets.append({
                            "flight_number": selected_flight['flight_number'],
                            "airline_name": selected_flight['airline_name'],
                            "schedule": selected_flight['schedule'],
                            "date": selected_flight['date'],
                            "price": selected_flight['price'],
                            "passenger_name": passenger.name,
                            "passenger_email": passenger.email,
                            "passenger_phone": passenger.phone
                            })

                    for ticket_info in selected_tickets:
                        history.add_to_history(ticket_info)

            elif choice == 2:
                history.display_history()

            elif choice == 3:
                total_price = sum(ticket['price'] for ticket in history.history)
                print(f"Total Price: {total_price}")
                print("Confirmed! Check Your Email for Confirmation.\n Thank You!")
                history.save_history()
                print("Checked out and saved history.")

            elif choice == 4:
                print("Enter the flight number you want to cancel:")
                flight_number = input().strip()
                cancellation = Cancellation(history)
                cancellation.cancel_ticket(flight_number)

            elif choice == 5:
                show_Goodbye()
                break

            else:
                print("Invalid option. Please enter a number between 1 and 5.")

        except ValueError:
            print("Error: Please enter a valid option (1-5).")

if __name__ == "__main__":
    show_welcome_and_website()
    main()
