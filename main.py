from MyEvent import *
from Utils import *

# 
# future plans:
#   - use tkinter to incorporate a GUI
# 
# to do:
#   - fix the prompts to reflect proper user prompts ✅
#   - hook up inputs to Event ✅
# 
#   - dummy up responses so I don't have to manually enter 14 variables when testing ✅
#   - finish up calculate_totals() ✅
#   - figure out how to print all the variables independently ✅
# 
# 
# 
#   - refactor Event class: use globals or don't, pick one ✅
#       - the problem right now is globals are available but not used ✅
#       - the infrastructure is there ✅
#   - Event class needs to be able to print the class variables
#
#
#   - TEST WITH REAL DATA TO CONFIRM ACCURACY OF LOGIC
#
#  
#   - import pandas
#   - print all the data into an excel spreadsheet
# 
# 
# 

# spoofed data
# responses = ["asdf","09/09/26",1234,300,2,3,4,5,6,7,8,9,10,11]
# 
responses = []

# main_method that calls all the other functions
def main_method():
    # reactivate this to resume user input
    # spoofing input to make testing easier
    main_loop()

    # send the responses to MyEvent.py
    myvar = MyEvent(*responses)

    # test retrieval of class attributes
    # vars() with an instance variable is the solution
    attributes_dict_vars = vars(myvar)
    print(f"Using vars(): {attributes_dict_vars}")

    # test printing all values
    # items()
    for k,v in attributes_dict_vars.items():
        print(f"*{k}: {v}")



#
def main_loop():
    """
    Docstring for main_loop
    """

    utils = Utils()

    # placeholder for prompts
    # this currently exists as proof of concept
    # refactor prompts array to reflect proper prompts
    prompts = [
        ("entities' name",2),
        ("date of the event",2),
        ("closing cash amount",1),
        ("credit card amount",1),
        ("amount of Turkey returned (in pounds)",1),
        ("amount of Ham returned (in pounds)",1),
        ("amount of Beef returned (in pounds)",1),
        ("price per pound of Turkey",1),
        ("price per pound of Ham",1),
        ("price per pound of Beef",1),
        ("amount of Turkey purchase (in pounds)",1),
        ("amount of Ham purchased (in pounds)",1),
        ("amount of Beef purchased (in pounds)",1),
        ("amount of Bread purchased",1)
    ]
    # "Please enter the {prompt}"
    # switch case
    # 1 = float
    # 2 = string

    #
    running : bool = True
    # 
    while running:
        # display program title
        utils.intro_to_application

        # loop through prompts
        for prompt in prompts:
            # get_validation_method calls input_validation_float or input_validation_string
            # gvm calls ivf or ivs due to prompt[1]'s designation - which is a hardcoded happy path shot caller
            # ivf or ivs returns their respective data type which is stored in "value" - user input
            value = utils.get_validation_method(prompt[0],prompt[1]) # refactor this please - too many nested functions
            # add value - user input - into responses array
            responses.append(value)

        # end while loop
        running = False


# 
def generate_excel_file():
    pass