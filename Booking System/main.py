global user_tickets, all_bookings, book_ticket

#import the modules for customer and admin functionalities into the main program
import customer #imports customer module
import admin #imports admin module 

'''Main Code'''  

customer.all_bookings = [] 
customer.all_ticket()
print("Welcome to the Theatre Booking System!")
while True: #loop that functions the system
  customer.user_tickets = []
  admin_input = input("Are you an admin? (Y/N):\n").upper()
  if admin_input == "Y": #if the user is an admin and they choose "Y":
    admin.admin_menu() #admin options will pop up from the admin module

  elif admin_input == "N": #if the user is not and admin and they choose "N"
    begin = input("\nAre you a new user? (Y/N): \n").upper() #questions if they are new to the system, which if "Y"" will create a new account, if "N" will log in

    if begin == "Y": #if the user chooses "Y" to being a new customer
      new_user = input("Please enter your preferred username: \n") #asks for a username 
      #account_creation from the customer module
      customer.account_creation(new_user) #function with the variable new_user as parameter to store the username within the file linked in the function
      

    elif begin == "N": #if the customer is not a new user
      login = input("Please enter your username to login: \n") #asks for the username they have entered when they created an account which is saved in txt file
      #function from the customer module imported, related to login, specific user ticket and also user menu with all the user options related to the theatre
      customer.user_login(login) #function from customer module which checks if the user data is stored in the file, if it is it logs user otherwise it suggests user to create a user
      customer.user_ticket(login) #function from customer module which retreats all the booked tickets by the specific customer who is logged in 
      customer.user_menu(login, customer.user_tickets) #function from customer module which opens the user menu once successfuly logged in with all the functionailities as options

    else:
      print("Invalid input, please try again") #if user inputs something other than "Y" or "N" for customer user login/creation
  else:
    print("Invalid input, please try again") #if user inputs something other than "Y" or "N" for admin user login
  
  #purpose of this is for user quitting the system (4th options in the user menu) 
  halt = True
  end = False
  while halt:
    quiting = input("Would you like to quit the system? (Y/N): ").upper() #asks user if they wish to quit out of the system
    if quiting == 'Y': #if their option is "Y", meaning they want to quit
      print("Thank you for using our system!") #print message will be displayed 
      halt = False
      end = True
      break #the program will stop running 
    elif quiting == 'N': #if the user does not wish to quit
      halt = False #the program will not stop running, it will go back to the very start of the program
    elif quiting != 'Y' and quiting != 'N': #if user input is outside of "Y" and "N":
      print("Invalid input, please try again") #user will require to input their option again

  if end == True:
    break
