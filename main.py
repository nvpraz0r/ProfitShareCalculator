import os # used to clear terminal screen

from Event import *

# 
# future plans:
#   - use tkinter to incorporate a GUI
# 
# to do:
#   - fix the prompts to reflect proper user prompts
#   - hook up inputs to Event
# 

# yay global variables bad practices start now :D
# responses array is where all the user input is stored
# which will EVETUALLY be sent to Event
responses = [] # this exists to be called from the main_method()

# main_method that calls all the other functions
def main_method():

    main_loop()

    Event.generate_array()

    # send the responses to Event.py
    # test messages

    # Testing input
    Event.test_responses(responses)
    Event.print_responses()


# unsure if this is how I want to handle the main loop 
def main_loop():
    """
    Docstring for main_loop
    """
    # placeholder for prompts
    # this currently exists as proof of concept
    # refactor prompts array to reflect proper prompts
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

    #
    running : bool = True
    # 
    while running:
        # display program title
        intro_to_application()

        # loop through prompts
        for prompt in prompts:
            # get_validation_method calls input_validation_float or input_validation_string
            # gvm calls ivf or ivs due to prompt[1]'s designation - which is a hardcoded happy path shot caller
            # ivf or ivs returns their respective data type which is stored in "value" - user input
            value = get_validation_method(prompt[0],prompt[1]) # refactor this please - too many nested functions
            # add value - user input - into responses array
            responses.append(value)

        # end while loop
        running = False


# helper method that directs the flow
# of which method should be used to
# validate user input
#
# switch case
# 1 = float
# 2 = string
def get_validation_method(prompt, prompt_data_type):    
    """
    Docstring for get_validation_method
    
    :param prompt: Description
    :param prompt_data_type: Description
    """    
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
    """
    Docstring for input_validation_float
    
    :param prompt: Description
    """
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
    """
    Docstring for input_validation_string
    
    :param prompt: Description
    """
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
    """
    Docstring for clear_screen
    """
    # For windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For mac and linux (bash systems)
    else:
        _ = os.system('clear')


# generate the file
def generate_excel_file():
    pass