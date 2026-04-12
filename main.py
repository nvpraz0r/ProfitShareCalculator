import pandas as pd
from Event import *
from Utils import *

# 
# future plans:
#   - use tkinter to incorporate a GUI
# 
# to do:
#   - fix the prompts to reflect proper user prompts ✅
#   - hook up inputs to Event ✅
#   - dummy up responses so I don't have to manually enter 14 variables when testing ✅
#   - finish up calculate_totals() ✅
#   - figure out how to print all the variables independently ✅
#   - refactor Event class: use globals or don't, pick one ✅
#       - the problem right now is globals are available but not used ✅
#       - the infrastructure is there ✅
#   - import pandas ✅
#   - print all the data into an excel spreadsheet ✅
# 
# 
#   - Rearrange the variable order to reflect format of previous profit share reports ✅
# 
#   - TEST WITH REAL DATA TO CONFIRM ACCURACY OF LOGIC
# 
# 
#   TESTING GIT SYNC

# spoofed data
responses = [
             "Scouts",
             "09/09/26",
             1166.54,
             213.46,
             0,
             0,
             0,
             5.59,
             1.99,
             4.25,
             8,
             12,
             36,
             4
]
# entity, date, cash_end, credit_card,turkey_returned,
# ham_returned, beef_returned,turkey_price, ham_price,
# beef_price,turkey_purchased, ham_purchased, beef_purchased,bread_purchased

# main_method that calls all the other functions
def main_method():
    # reactivate this to resume user input
    # spoofing input to make testing easier
    # main_loop()

    # send the responses to MyEvent.py
    myvar = Event(*responses)

    # test retrieval of class attributes
    # vars() with an instance variable is the solution
    attributes_dict_vars = vars(myvar)
    print(f"Using vars(): {attributes_dict_vars}")

    # test printing all values
    # items()
    for k,v in attributes_dict_vars.items():
        print(f"*{k}: {v}")


    try:
        TEST_PANDAS(attributes_dict_vars)
    except Exception as e:
        print(f"An error occurred while creating the excel file: '{e}'")


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


# WORKING ON THIS FUNCTION
def TEST_PANDAS(attributes_dict_vars):
    # data = {
    #     "test123" : 123,
    #     "test456" : 456
    # }
    # df = pd.DataFrame([data]).transpose()
    # df.index.name = 'asdf'
    # df.to_excel("TestFile.xlsx")

    file_path = "TestFile.xlsx"

    # change variable column before packaging the program for use
    df = pd.DataFrame.from_dict(attributes_dict_vars, orient='index', columns=['AML'])
    df.index.name = 'Profit Share Report'
    df.to_excel(file_path)