global user_tickets, all_bookings

import customer #imports the customer module

def cancel_ticket_admin():
    prices = [20, 40, 60, 70, 70, 80, 100] #prices from each row in the theatre, e.g, 20 for row 7, 40 for row 6, 60 for row 5,...
    customer.seat_layout(customer.all_bookings, customer.user_tickets) #calls seat layout function from customer to display the layout of the theatre
    try:
        row = 7 - int(input("Enter the row of the ticket you would like to cancel (1-7): ")) #asks admin which row they want to choose
        seat = int(input("Enter the seat of the ticket you would like to cancel: "))-1 #asks admin which seat from the row they would like to choose to cancel
    except ValueError:
        print("Invalid input, please enter a number") #when admin has entered a value other than integer
        cancel_ticket_admin() #returns to the beginning of the function
    else:
        if row < 0 or row > 6 or seat < 0 or seat > 19 - row*2: #if the inputted range for row and seat is outside 
           print("You have chosen an invalid row or seat, please try again: ") #asks admin to input again
           cancel_ticket_admin() #returns to the beginning of the function
        else:
            price = prices[row]
            confirm = input(f"Are you sure you would like to cancel ticket?\nRow:{7-row}\nSeat: {seat+1}\nPrice: {price}\n(Y/N): ")
            if confirm.upper() == "Y": #if admin chooses to cancel the ticket
              for i in customer.user_tickets: 
                if i == [row, seat]: #if the entered row and seat value matches to the row and seat in user tickets list
                  user_tickets.remove(i) #the booking is removed from the list

              for i in customer.all_bookings:
                if i == [row, seat]:
                  customer.all_bookings.remove(i) #removes the booking from all_bookings list

              with open("bookings.txt", "r") as file: #opens booking file as file and reads
                  lines = file.readlines() #reads through all the lines in the file 
              with open("bookings.txt", "w") as file: #opens the booking file as file
                  for line in lines:
                      user_name, user_row, user_seat = line.strip().split(",") #splits lines of data into variable
                      if user_row == str(row) and user_seat == str(seat):
                          continue
                      else:
                          file.write(line)
                  file.close()
              print(f"Ticket has been cancelled") #informs admin that the ticket has been cancelled
            elif confirm.upper() == "N": #if admin chooses not to cancel ticket 
                print("Ticket cancellation cancelled by admin") #informs admin that the booked ticket has not been cancelled
            else:
                print("Invalid choice, please enter Y or N.") #informs admin that they have entered value outside of "Y" and "N"
                cancel_ticket_admin() #returns admin to the start of the function if they do not enter an appropriate value

def reset_booking():
    confirm = input("Are you sure you would like to reset the system? (Y/N): ") #asks admin if they wish to reset the booking system entirely
    if confirm.upper() == "Y": #if admin chooses to reset
        with open("bookings.txt", "w") as file: #opens booking file as write and labelled as file
            file.write("")
        customer.user_tickets.clear()
        customer.all_bookings.clear()
        print("System has been reset") #informs admin that the booking system has been reset and there is no previous bookings stored
    elif confirm.upper() == "N": #if admin chooses not to reset
        print("System reset cancelled by admin") #informs admin that it has been cancelled
    else:
        print("Invalid choice, please enter Y or N.") #informs admin that they have entered value outside of "Y" and "N"
        reset_booking() #returns admin to the start of the function if they do not enter an appropriate value

def admin_menu():
  print("Welcome Admin!")
  while True:
    try:
      choice = int(input("1. View Ticketing Status\n2. Cancel Ticket\n3. Reset\n4. Quit\nChoice: ")) #admin options printed out
    except ValueError:
      print("Invalid input, please enter a number") #when admin inputs a value outside of  integer
      continue
    else:
      if choice == 1: #if admin chooses option 1 
        print("View Ticketing Status") #option 1 represents viewing the ticketing status of the theatre
        customer.seat_layout(customer.all_bookings, customer.user_tickets) #imports the seat layout function from customer module displaying all user bookings stored within the two lists

      elif choice == 2: #if admin chooses option 2
        cancel_ticket_admin() #cancel ticket function for admin is imported as option 2 represents the ability for admin to cancel any specific ticket

      elif choice == 3: #if admin chooses option 3
        reset_booking() #reset booking function for admin is imported as option 3 represents the ability for admin to reset all of the bookings

      elif choice == 4: #if admin chooses option 4 
        print("Quit")
        break #breaks once the admin chooses to quit (after they halt the program)

      else:
        print("Invalid input, please enter a number from 1-4") #ensures that the user inputs a value from 1-4, anything outside of this will repeatedly ask user for valid input

