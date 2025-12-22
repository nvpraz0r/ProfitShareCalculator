# 
# ideas:
# - CLI interface doesn't need to be fancy
# - Prompt user for various data points
#   - cash close out, credit card close out, product costs; you get the idea
# - Once all the data has been confirmed generate a CSV file or excel spreadsheet
# 
# 
# CURRENT PROBLEM
#   - responses array not filling with user input
# 
# 
# 
# 
# code flow
# 
# 
# dict = [variable, data type]
# data type float or string
# 
# 
# intro
# enter entity
# enter date
# cash end
# credit card
# returned amount of turkey
# returned amount of ham
# returned amount of beef
# price of turkey per pound
# price of ham per pound
# price of beef per pound
# amount of turkey purchased
# amount of ham purchased
# amount of beef purchased
# amount of hamburger buns purchase
# 
# send the variables 
# 
# 

import os # used to clear terminal screen

from Event import *


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



    main_loop()

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
            return input_validation_float(prompt)
        case 2:
            # string
            return input_validation_string(prompt)
        case _:
            print("Error occurred somewhere during the validation process.")


# check if input is a valid float
def input_validation_float(prompt):

    while True:
        try:
            result : float = float(input(f"Please enter the {prompt}"))
            print(result)
            return result
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
            return result
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


    prompts = [
        ("one",1),
        ("two",1),
        ("three",1),
        ("four",1),
        ("five",1),
        ("six",1),
        ("seven",1),
        ("eight",1),
        ("nine",1),
        ("ten",1),
        ("eleven",1),
        ("twelve",1),
        ("thirteen",1),
        ("fourteen",1)
    ]

    # store user responses
    responses = []

    running : bool = True

    while running:
        # 
        intro_to_application()

        for prompt in prompts:
            value = get_validation_method(prompt[0],prompt[1])
            responses.append(value)
            
        running = False


    # send the responses to Event.py
    # test messages
    clear_screen()
    print("printing responses")
    for i in responses:
        print(i)

    # generate the file

    # continue?