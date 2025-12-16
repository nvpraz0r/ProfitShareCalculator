# 
# ideas:
# - CLI interface doesn't need to be fancy
# - Prompt user for various data points
#   - cash close out, credit card close out, product costs; you get the idea
# - Once all the data has been confirmed generate a CSV file or excel spreadsheet
# 

# 
# REFER TO example.txt
# 
# data structure planning - ditionary should work just fine
#
# 
# data = [
# ("entity name", "xyz group"),
# ("cash close out", 1234),
# ("credit card close out", 4321),
# ("total product costs", 1234),
# ("returned meat", 12),
# ("profit shared", 200)
# ]
# 
# 
# 
# LAST LEFT OFF:
#   - working on string input validation
# 
# IDEAS:
#   - object to dictionary???
# 
# 
# 


import os # used to clear terminal screen



def calculator():

    # 
    entity : str = ""
    date = 0

    # 
    CASH_START : float = 600.00
    cash_end : float = 0.00 # user input
    credit_card : float = 0.00 # user input
    credit_card_tax : float = credit_card * 0.03
    credit_card_net : float = credit_card - credit_card_tax
    total_sales : float = (credit_card_net + cash_end) - CASH_START

    # returned meat
    turkey_returned : float = 0 # user input
    ham_returned : float = 0 # user input
    beef_returned : float = 0 # user input

    turkey_price : float = 0 # user input
    ham_price : float = 0 # user input
    beef_price : float = 0 # user input

    total_returned : float = (turkey_returned * turkey_price) + (ham_returned * ham_price) + (beef_returned * beef_price)

    gross = total_returned + total_sales

    # expenses
    turkey_purchased : float = 0 # user input
    ham_purchased : float = 0 # user input
    beef_purchased : float = 0 # user input
    bread : int = 0 # user input
    bread_total : int = bread * 10

    total_expenses : float = (turkey_purchased * turkey_price) + (ham_purchased * ham_price) + (beef_purchased * beef_price) + bread_total

    profit : float = gross - total_expenses

    shared : float = profit / 2



    intro_to_application()


    # first param: is the prompt message
    # second param: is the DEMANDED data type
    # get_validation_method("ending amount of cash.", 2)









# helper method that directs the flow
# of which method should be used to
# validate user input
#
# switch case
# 1 = float
# 2 = string
def get_validation_method(prompt, prompt_data_type):    
    
    # switch case
    # 1 = float
    # 2 = string
    match prompt_data_type:
        case 1:
            # float
            input_validation_float(prompt)
            pass
        case 2:
            # string
            input_validation_string(prompt)
            pass
        case _:
            print("Error occurred somewhere during the validation process.")


# check if input is a valid float
def input_validation_float(prompt):

    while True:
        try:
            result : float = float(input(f"Please enter the {prompt}"))
            print(result)
            break
        except ValueError:
            print("Invalid input. Please enter the correct information.")
            # wait for 2 seconds
            # clear screen
            # print menu


# check if input is a valid string
def input_validation_string(prompt):

    while True:
        try:
            result : str = str(input(f"Please enter the {prompt}"))
            print(result)
            break
        except ValueError:
            print("Invalid input. Please enter the correct information.")
            # wait for 2 seconds
            # clear screen
            # print menu


# display intro header
def intro_to_application():
    print("         Profit Share Calculator")
    print("+-----------------------------------------+")
    print("|                                         |")
    print("| This Program is designed to generate    |")
    print("| an excel spreadsheet.                   |")
    print("|                                         |")
    print("+-----------------------------------------+")
    print()


# clear the screen
def clear_screen():
    # For windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For mac and linux (bash systems)
    else:
        _ = os.system('clear')

# unsure if this is how I want to handle the main loop 
def main_loop():
    # loop through a list of prompts that are needed
    # 
    #   dict [
    #   ("entity name", 1),
    #   ("date", 2),
    #   ("XZY", ),
    #   ()
    #   ]
    # 
    #   for prompt in prompts
    #       get_validation_method(prompt[0], prompt[1])
    #
    #       HOPEFULLY this will loop through all the prompts
    #    
    pass