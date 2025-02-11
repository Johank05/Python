'''User Access '''
def username_exists(username):
    '''
    This username will go over the user txt file searching whether the inputted username by new user is already 
    stored within the file already. This function will open the txt file to read only, as it will read all of the 
    lines within the txt file. 
    If there is a match, it will return True, if not, it will return False and output a message to the user to indicate a username 
    does not exist.

    Parameter : username (str) = represents the username that the function username_exists 
    checks for existence within the "username.txt" file.
    '''

def account_creation(user):
    '''
    This function will create a user if the username does not already exist within the "username.txt" file which is discovered through 
    the username_exists(username) function returning false.
    If it returns true, it will output a message to the user indicating that the username already exists and they will be prompted to
    try again.
    This function will allow user to store their username in the user.txt file.

    Parameters: user (str) = represents the inputted username from username_exists(username) function, which will be used to create a 
    new user.
    '''

def user_login(access):
    '''
    This functions relies on the username_exists(username) function to check if the username exists within the "username.txt" file.
    If the username is found in the txt file, it will log the user in to their account. If the account is not found 
    in the txt file, it will ask the user to enter a new username until a new user is not found in the txt 
    file validated by the username_exist(username).

    Parameter: access(str) =  represents the username inputted by the user for logging back into their account.
    '''

def seat_layout(layout):
    '''
    This function will display the current layout of the theatre seating.

    Parameter: layout = represents the theatre seating layout from which users will be able to choose bookings
    from, display the layout and also cancel ticket from.
    '''

def show_ticket_user(access):
    '''
    This function allows users to check the tickets which they have booked. This will display their specific tickes
    purchased by the user consisting information about their ticket number, row and seat number for the ticket and 
    how much the ticket was.
  
    Parameter: access (str) = represents the username inputted by the user to output their booked tickets.
    '''

def book_ticket(access, layout):
    '''
    This function will allow user to input a row number and seat number from which they can book from. Their booked
    seats will be stored in a txt file with their username, so that when they log back in their bookings are saved
    within the layout. If a user tries to book seats which are currently not available, it will not allow the user
    to book that seat.
  
    Parameters: access (str) = represents the username inputted by the user to book their seats.
                layout (str) = represents the theatre seating layout from which users will be able to choose bookings.
    '''

def cancel_ticket_user(access, layout):
    '''
    This function will allow the user to cancel their ticket only. Firstly, they will be presented their booked seats
    as "B" and other seats as "_" and will give users the option to choose which of their booked seats they will
    like to cancel, once the user chooses which seat they want to cancel, they will get a confirmation on the booking
    details, which consist of the row, seat, price and whether they will like to cancel this specific ticket.
    Once the ticket is cancelled, it will be removed from the seating layout and user's account.
  
    Parameters: access (str) = represents the username inputted by the user to cancel their specific seats.
                layout (str) = represents the theatre seating layout from which users will be able to choose bookings to cancel.
    '''

def user_menu(access):
    '''
    This function will show the menu for the users once they are logged into their account.
  
    Parameter: access (str) = represents the username inputted by the user to access their account.
    '''

''' Admin Access '''    

def admin_menu():
    '''
    This functions will show the menu for the admin if the user is an "admin".
    '''

def show_ticket_admin():
    '''
    This function will allow the admin to view all of the current booked tickets which have been booked out by all
    of the user. All of the tickets which have been booked by the users will be displayed as "x" in order for the 
    admin to know which seats are currently unavailable to be booked.
    '''

def reset_booking():
    '''
    This fucntion will allow the admin to reset all of the booking within the layout, which means that the whole 
    theatre layout is reset, and none of the booked seats are there anymore as they have been deleted.
    '''

def cancel_ticket_admin():
    '''
    This function will allow the admin to cancel specific tickets within the theatre layout, as they will be able 
    to select specific seats booked and cancel them if they want to. This is different from reset booking as instead
    of deleting all of the they can choose specific seating which they would like to be gone. 
    '''