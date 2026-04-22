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
#   - Rearrange the variable order to reflect format of previous profit share reports ✅
#   - TEST WITH REAL DATA TO CONFIRM ACCURACY OF LOGIC ❌❌❌
#       - test with real data was incorrect possibly due to use of float
#
#   - Refactor data types from float to int:
#       - divide data by 100 to achieve dollar and cent amount without floating point errors
#
#   - Refactor::
#       - clean up code base:
#           - cull unnecessary comments
#           - clean up functions and methods
#           - clean up files
#           - Add how to use in README doc and in comments

from Event import *
from Utils import *


# entity, date, cash_end, credit_card,turkey_returned,
# ham_returned, beef_returned,turkey_price, ham_price,
# beef_price,turkey_purchased, ham_purchased, beef_purchased,bread_purchased
# responses = [
#              "Scouts",
#              "09/09/26",
#              1166.54,
#              213.46,
#              0,
#              0,
#              0,
#              5.59,
#              1.99,
#              4.25,
#              8,
#              12,
#              36,
#              4
# ]


responses = []

def main():
    """ Main method that calls all other functions """
    # 
    get_user_responses()

    # send the responses to MyEvent.py
    myvar = Event(*responses)

    # test retrieval of class attributes
    # vars() with an instance variable is the solution
    attributes_dict_vars = vars(myvar)
    print(f"Using vars(): {attributes_dict_vars}")

    # test printing all values
    # items()
    for key, value in attributes_dict_vars.items():
        print(f"*{key}: {value}")

    # works, just don't need it to work right now
    # try:
    #     TEST_PANDAS(attributes_dict_vars)
    # except Exception as e:
    #     print(f"An error occurred while creating the excel file: '{e}'")


#
def get_user_responses():
    """ This function gets all the relevant data from the user """

    # Utils class reference
    utils = Utils()


    # "Please enter the {prompt}"
    # switch case
    # 1 = int
    # 2 = string
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


    #
    running : bool = True
    # 
    while running:
        # display program title
        utils.intro_to_application()

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


    def event_replacement(prompts):
        """ replacing event class due to it's limitations """

        # 14 user input values
        # entity = prompts[0]
        # date = prompts[1]
        # cash_end = prompts[2]
        # credit_card = prompts[3]
        # turkey_returned = prompts[4]
        # ham_returned = prompts[5]
        # beef_returned = prompts[6]
        # turkey_price = prompts[7]
        # ham_price = prompts[8]
        # beef_price = prompts[9]
        # turkey_purchased = prompts[10]
        # ham_purchased = prompts[11]
        # beef_purchased = prompts[12]
        # bread_purchased = prompts[13]
        user_input_values = {
            "entity": "",
            "date": "",
            "cash_end" : 0,
            "credit_card" : 0,
            "turkey_returned" : 0,
            "ham_returned" : 0,
            "beef_returned" : 0,
            "turkey_price" : 0,
            "ham_price" : 0,
            "beef_price" : 0,
            "turkey_purchased" : 0,
            "ham_purchased" : 0,
            "beef_purchased" : 0,
            "bread_purchased" : 0
        }

        # needs to be tested
        for prompt in prompts:
            user_input_values[prompt] = prompt
        

