Carry You - Flight Ticket Booking System
Carry You is a Python-based flight ticket booking system developed as an Object-Oriented Programming (OOP) project. It allows users to book flights, manage bookings,cancel and view booking history through a command-line interface.
Features
-User Authentication: Login or sign up with a user ID and password stored in `users.txt`.
-Flight Booking: Search and book flights based on departure and arrival cities from 'flights2.txt'.
-Booking History: View past bookings including flight details and passenger information.
-Ticket Cancellation: Cancel booked tickets and update booking history accordingly.
-Checkout: Calculate and display the total price of booked tickets.
Usage
1.Requirements:
   - pip install pillow
   -tkinter
   -python 3.5
1. Setup:
   - Ensure `users.txt` contains user IDs and passwords.
   - Populate `flights2.txt` with flight details.
2. Running the Program:
   - Execute `main_code.py` to start the booking system.
Structure
The project is structured into several classes:
- Carry_you: Manages user authentication and signup.
- List_of_flights: Abstract class for handling flight data.
- Flight: Subclass of `List_of_flights` for flight operations.
- Passenger: Manages passenger details.
- History: Stores and displays booking history.
- Cancellation: Handles ticket cancellation.
Files
- users.txt: Stores user credentials (`user_id,password`).
- flights2.txt: Contains flight details (`departure_city,arrival_city,airline_name,schedule,date,duration,class_type,price,flight_number`).
- main_code.py: Main program to run
- GUIintro.py:Graphical user interface for intro.
- GUIending.py:Graphical user interface for ending.
- Classes.py: all classes of program store in it.
Future Enhancements
- Implement GUI for better user interaction.
- Integrate database for scalable data management.
- Add seat selection and multi-city flight booking options.
License
This project is licensed under the MIT License.