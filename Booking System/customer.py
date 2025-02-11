global user_tickets, all_bookings

'''Function to check if username exists'''
def username_exists(username):
  '''This return statement will return false if the username doesnt exist or it will return true if the username does exist. 
    This true or false can be used in the other functions for validations so this function is used for checking and validations 
    for both creating a new user or to log in'''
  
  with open("username.txt", "r") as file:
    return username in file.read().splitlines() 


def account_creation(user):
  '''Function for account creation, runs a recursive function where it loops until the user inputs a username which is not in the 
   text file, if user does not exist in the txt file it stores it in there.'''
  
  if username_exists(user): #runs the username_exist function to check whether the inputted username is already stored in the file or not
    new_user = input("Sorry, but this username has already been created and stored in our system.\n Enter a different username: ") #message when the username is already stored in the file
    account_creation(new_user) #returns to checking the file with the new user inputted by the user
  else:
    with open("username.txt", "a") as file: #opens the file as append and is labelled as file
      file.write(user + "\n")
      print(f"Congratulations {user}, your username has been saved!") #prints out showing the the username has been saved in the file/.


#function for users to login
def user_login(access):
  global login #allows specific username to be implemented across the whole system every time a user logs in
  if username_exists(access) == True: #first it checks whether the inputted username is found in the file, if it is found (==TRUE) then it print out message:
    print(f"Your username has been found in our system, Welcome back {access}!") #once account is successfully found the messafe is presented 
  else: 
    login = input("Your account has not been found. Please try again\nEnter your username: ") #when user is not found in the system this is printer out 
    user_login(login) #returns to asking user to input a username which is not stored already in the system until it finds a valid username

#function that generates the seating layout accordingly to the project specification
def seat_layout(data, userdata): 
     '''
     I had changed the parameters from just layout (mentioned in milestone) to data and userdata.
     This is because I didn't store the layout in a text file to worry about passing it into the function.
     Instead, I stored the bookings in a text file and stored the user's bookings in a list and printed the layout depending on the data.

     Parameters:
     data: list of lists containing all bookings
     userdata: list of lists containing all bookings of the user

     '''
     for row in range(7):
        print(f"Row {7-row}: ", end="")
        print(" "*row*2, end = "")
        for seat in range(20-row*2): 
            if [row,seat] in userdata:
                print("B", end=" ") #prints user data as B
            elif [row,seat] in data:
                print("X", end= " ") #prints other users as X
            else:
              print("_", end=" ") #prints the unbooked seats as _ with spaces in between which have no value
        print()


def book_ticket(username): 
    '''
    In milestone, my parameter was access which I have changed to username in order to make it easier for me to understand what value I am
    passing through the function.

    Parameter:
    username: the username of the user who is booking the ticket.
    '''
    prices = [20, 40, 60, 70, 70, 80, 100] #prices from each row in the theatre, e.g, 20 for row 7, 40 for row 6, 60 for row 5,...
    try:
        row = 7-int(input("Enter the row (1-7): ")) #asks user to input the row they would like to book
        seat = int(input("Enter seat: "))-1 #asks user to input seat that they would to book
    except ValueError:
        print("Invalid input, please enter numbers only.") #exception handling for values outside of integers
        book_ticket(username) #sends user back to the start of the function
    else:
        if row < 0 or row > 6 or seat < 0 or seat > 19 - row*2: #if the inputted range for row and seat is outside 
           print("You have chosen an invalid row or seat, please try again: ") #asks user to input again
           book_ticket(username) #sends user back to the start of the function
        else:
            if [row,seat] in all_bookings: #checks if the chosen seat is already booked. If the ticket is already booked
                print("Seat already booked") #alerts user that the seat is already booked
                book_ticket(username) #sends user back to the start of the function
            else:
                  price = prices[row] #prices based on the row from the prices list 
                  confirm = input(f"--------------\nRow: {7 - row}\nSeat: {seat + 1}\nPrice: {price}\n--------------\nWould you like to book this seat? (Y/N): ")
                  if confirm.upper() == "Y": #if the users confirms to book that seat
                        with open("bookings.txt", "a") as file: #opens booking file as append and labelled as file
                            file.write(username + "," + str(row) + "," + str(seat) + "\n") #how the booking information is stored
                        print(f"{username}, your ticket has been booked!") #informs user that their booking is confirmed
                        user_tickets.append([row, seat])
                        all_bookings.append([row, seat])
                  elif confirm.upper() == "N": #if user decides to not book the ticket 
                        print("Booking cancelled by user") #informs that the booking has been called off
                  else:
                        print("Invalid choice, please enter Y or N.") #when user has entered value outside of "Y" or "N"


def user_ticket(username):
   '''
   I did not have this function in my milestone, however I implemented this. This function retreats all of the tickets booked by that
   specific user under their username and adds it to a list called user_tickets.

   Parameter:
   username: The username of the user who is logged in to cross-reference with all bookings. 
   '''
   with open("bookings.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            user_name, user_row, user_seat = line.strip().split(",")
            if user_name == username:
               user_tickets.append([int(user_row), int(user_seat)])

def all_ticket():
   '''
   I did not have this function in my milestone, however I implemented this. This function retreats all of the tickets booked by all 
   of the users which appends to a list called all_bookings.
   '''
   with open("bookings.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            user_name, user_row, user_seat = line.strip().split(",")
            all_bookings.append([int(user_row), int(user_seat)])


def show_ticket_user(username):
    '''
    In milestone, my parameter was access which I have changed to username in order to make it easier for me to understand what value I am
    passing through the function.

    Parameter:
    username: the username of the user who is trying to see their tickets.
    '''
    print("-------------------")
    print(f"Tickets for {username}:")
    print("-------------------")
    for ticket in user_tickets:
       count = user_tickets.index(ticket)+1
       print(f"Ticket {count}:\nRow: {7-int(ticket[0])}\nSeat: {int(ticket[1])+1}\n-------------")
       

def cancel_ticket_user(username):
    '''
    In milestone, my parameter was access which I have changed to username in order to make it easier for me to understand what value I am
    passing through the function.

    Parameter:
    username: the username of the user who is cancelling the ticket.
    '''
    prices = [20, 40, 60, 70, 70, 80, 100] #prices from each row in the theatre, e.g, 20 for row 7, 40 for row 6, 60 for row 5,...
    seat_layout([], user_tickets) #seat layout is printed out with the specific user's ticket 
    try:
        row = 7-int(input("Enter the row (1-7): ")) #asks user for the row for the ticket they wish to cancel 
        seat = int(input("Enter seat: "))-1 #asks user for the seat for the ticket they wish to cancel
    except ValueError:
        print("Invalid input, please enter numbers only.") #handles any inputted values which are outside of integers
        cancel_ticket_user(username) #returns to the beginning of the function
    else:
        price=prices[row] #price based on the row inputted
        confirm = input(f"--------------\nRow: {7 - row}\nSeat: {seat + 1}\nPrice: {price}\n--------------\nDo you want to cancel? (Y/N)\n ")
        validation = False 
        if confirm.upper() == "Y": #if they wish to cancel the ticket
            with open("bookings.txt", "r") as file: #opens booking file as file and reads
                    lines = file.readlines() #reads through all the lines in the file 
            with open("bookings.txt", "w") as file: #opens the booking file as file
                for line in lines: 
                    user_name, user_row, user_seat = line.strip().split(",") #splits lines of data into variable
                    if user_name == username and user_row == str([row,seat][0]) and user_seat == str([row,seat][1]): 
                      '''
                      goes over the file to look through the lines and checks the row (0) and seat (1) whether the row and 
                      seat chosen by the user matches with the user's information according to the file.
                      '''
                      user_tickets.remove([row,seat]) 
                      all_bookings.remove([row,seat])
                      validation = True
                    else:
                        file.write(line)
                file.close()
            if validation == True: #if user is successfully able to cancel their ticket
                print("Ticket cancelled successfully!") #this print statement shows up
            else:
                print("Ticket not found") #this print statement shows up if the chosen seat and row to cancel is not found

        elif confirm.upper() == "N": #if user does not want to cancel the ticket and chooses "N"
            print("Ticket cancellation cancelled by user") #informs the user that ticket cancellation has been called off
        else:
            print("Invalid choice, please enter Y or N.") #print out shown when user inputs value other than "Y" or "N"
            cancel_ticket_user(username) #takes user back to the start of the function

#functionality the displays all of the user menu options 
def user_menu(access,user_tickets):
    '''
    In my milestone, for user_menu function I had acces and not user_tickets. 

    Parameter: 
    access: represents the username inputted by the user to access their account.
    user_tickets: list of lists containing all tickets booked by that user which is passed over when displaying tickets.
    '''
    print(f"Welcome {access}!") #print out welcoming the user
    while True:
      try:
        choice = int(input("1. Book ticket\n2. Cancel ticket\n3. Show ticket\n4. Quit\nChoice: ")) #user options printed out
      except ValueError: #exception handling
        print("Invalid input, please enter a number") #value error is handle is it ensures that only integers are being inputted
        continue
  
      else:
        if choice == 1: #if user chooses option 1 
          seat_layout(all_bookings, user_tickets) #seat_layout function is printed out 
          book_ticket(access) #booked tickets function is imported as option 1 represents booking tickets and stored under that specific user
  
        elif choice == 2: #if user chooses option 2
          cancel_ticket_user(access) #cancel ticket function for user is imported as option 2 represents cancelling the ticket booked by that user only
  
        elif choice == 3: #if user chooses option 3
          print("Show ticket") 
          show_ticket_user(access) #show ticket function is imported as option 3 represents showing the tickets booked by that user only
  
        elif choice == 4: #if user chooses option 4
          print("Quit")
          break #breaks once the user chooses to quit (after they halt the program)
  
        else:
          print("Invalid input, please enter a number from 1-4") #ensures that the user inputs a value from 1-4, anything outside of this will repeatedly ask user for valid input
