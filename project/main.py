# Function to check if username exists
def username_exists(username):
  with open("username.txt", "r") as file:
    return username in file.read().splitlines(
    )  # This return statement will return false if the username doesnt exist or it will return true if the username does exist. This true or false can be used in the other functions for validations so this function is used for checking and validations for both creating a new user or to log in.


# Function for account creation
def account_creation(user):
  if username_exists(
      user
  ):  # Here I changed it so that if the username exists, it will output a message to the user saying it exists and then asks them to enter a different username which is ran through the function again called a recursive function to check if the new username they entered exists as well and if the new username they entered doesnt exist then it add it to the text file
    new_user = input(
        "Sorry, but this username has already been created and stored in our system.\n Enter a different username: "
    )
    username_exists(new_user)
  else:
    with open("username.txt", "a") as file:
      file.write(user + "\n")
      print(f"Congratulations {user}, your username has been saved!")


# Function for users to login
def user_login(access):
  if username_exists(
      access
  ) == True:  # I changed this so that u can use that function to check if the username exists or not
    print(
        f"Your username has been found in our system, Welcome back {access}!")
  else:  # I changed this as the user is trying to log in so it takes an input statment which then does something called a recursive function which is a function that calls itself
    login = input(
        "Your account has not been found :( Please try again!\nEnter your username: "
    )
    user_login(login)
    

#def seat_layout(layout):
 # for i in range(7):
  #  row = 


#def show_ticket(Access):

def user_menu(access):
  print(f"Welcome {access}!")
  while True:
    try:
      choice = int(input("1. Book ticket\n2. Cancel ticket\n3. Show ticket\n4. Quit\nChoice: "))
    except ValueError:
      print("Invalid input, please enter a number")
      continue
    else:
      if choice == "1":
        #book_ticket(access)
        print("Book ticket")

      elif choice == "2":
        #cancel_ticket(access)
        print("Cancel ticket")

      elif choice == "3":
        #show_ticket(access)
        print("Show ticket")

      elif choice == "4":
        print("Thank you for using our system!")
        break

      else:
        print("Invalid input, please enter a number from 1-4")




def admin_menu():
  print("Welcome Admin!")
  while True:
    try:
      choice = int(input("1. View Ticketing Status\n2. Cancel Ticket\n3. Reset\n4. Quit\nChoice: "))
    except ValueError:
      print("Invalid input, please enter a number")
      continue
    else:
      if choice == 1:
        #view_ticketing_status()
        print("View Ticketing Status")

      elif choice == 2:
        #cancel_ticket()
        print("Cancel Ticket")

      elif choice == 3:
        #reset()
        print("Reset")

      elif choice == 4:
        print("Quit")
        break

      else:
        print("Invalid input, please enter a number from 1-4")
 
  






'''Main Code'''  # I put this in a while loop so that the code will keep running until the user logs in so I recommend running the code with different inputs and stuff so u understand whats going on.

print("Welcome to the Cinema Booking System!")
while True:
  admin_input = input("Are you an admin? (Y/N):\n").upper()
  if admin_input == "Y":
    admin_menu()
    break

  elif admin_input == "N":
    begin = input("\nAre you a new user? (Y/N): \n").upper()

    if begin == "Y":
      new_user = input("Please enter your preferred username: \n")
      account_creation(new_user)

    elif begin == "N":
      login = input("Please enter your username to login: \n")
      user_login(login)
      user_menu(login)  # I added this break so that it will break out of the while loop once the user successfully logs in otherwise it will keep asking the user until they successfull log in even after making a new username, Try run the code so u understand the code.

    else:
      print("Invalid input, please try again")
  else:
    print("Invalid input, please try again")
