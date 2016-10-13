# create a simple function that gets multiple input values from the user,
# it validates the data and returns the tuple

# Change the prompts in get_data() for the phone number to accept the data in the format: 999-999-9999
   # Create a function called validate_phone() that accepts a string called phone as input. The function should:

  #  Use the split() function to break the phone string into a list of tokens using "-" as a separator.
  #  Test each of the characters in each of the tokens to make sure they are digits. Hint: Use nested for loops.
  #  Return true if phone is in the correct format, false otherwise
  #  Change get_data() to call the validate_phone() function to determine whether the data is valid.
 # Submit your .py file.

def validate_phone(phone):
    phone = str("123-456-7890")
    pl = phone.split('-')

    #pl is ['123','456','7890']


def get_data():
    #get info, make sure it is NOT empty
    fn = raw_input("First name: ")
    while len(fn) < 1:
        fn = raw_input("First name is required. Please re-enter: ")
            #same thing for last name
    ln = raw_input("Last name: ")
    while len(ln) < 1:
        ln = raw_input("Last name is required. Please re-enter: ")
    #get a phone number, make sure it is at least 10 digits
    #use .strip() command to rid of white space
    ph = raw_input("Enter 10-digit phone number: ")
    while validate_phone(ph) == False:
        raw_input("Phone number in format 999-999-9999 required. Please re-enter: ")
    #now I should have all 3 values
    return (fn, ln, ph)              #returns the values as a tuple


####----MAIN PROGRAM----###
# create an empty customer list
customer_list = []

print("Welcome to the customer database!")
print ("\nPlease choose from the following menu items: ")

#display a menu and get a valid menu choice
menu_choice = 0                 #initialize my test value
while menu_choice != 3:
    print("    1. Enter a new customer")
    print("    2. Display customer list")
    print("    3. Quit")
    choice = raw_input("? ")
    #check for a valid menu choice
    # if i try to convert to an intege and they type something else
    # i will get an error
    #first, strip off white space before testing value
    if choice.strip() not in ['1', '2', '3']:
        print("Invalid Choice. Please enter 1, , or 3.")
    else:
        menu_choice = int(choice)               #now I can test menu_choice in loop
    #now that I have a valid menu choice, I need to respond
    if menu_choice == 1:
        # put the customer data in my customer list
        customer_list.append(get_data())                     #add data tuple to the list
        print ""
    elif menu_choice == 2:             #display customer list
        #the values in the tuple from the list
        #will be matched up with variable names
        for (First, Last, phone) in customer_list:
            print Last + ", " + First + ", " + phone
        print""

print("\nThanks for using the customer database.")
