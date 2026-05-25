# TODO:
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
# 
#   - Integrate GUI
# 
# 

from Event import *
from Utils import *


# entity, date, cash_end, credit_card,turkey_returned,
# ham_returned, beef_returned,turkey_price, ham_price,
# beef_price,turkey_purchased, ham_purchased, beef_purchased,bread_purchased
# responses = []
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


def main():
    """ Main method that calls all other functions """

    # uncomment for data gathering
    # get_user_responses()

    print("PRINTING RESPONSES")
    print(responses)
    print("DONE PRINTING RESPONSES")


    print("PRINTING EVENT CLASS REPLACEMENT")
    event_class_replacement(responses)
    print("DONE PRINTING EVENT CLASS REPLACEMENT")


    # 
    event_data_dict = event_class_replacement(responses)


    # test printing all values
    # items()
    print("Using items()")
    for key, value in event_data_dict.items():
        print(f"*{key}: {value}")

    # works, just don't need it to work right now
    # try:
    #     TEST_PANDAS(attributes_dict_vars)
    # except Exception as e:
    #     print(f"An error occurred while creating the excel file: '{e}'")


# TODO: calculate the totals✅
def event_class_replacement(user_input_values) -> dict:
    """
    Calculates the raw input data into 

    :param user_input_values The raw input data from the user

    :type user_input_values list

    :return The converted event data

    :rtype dictionary
    """

    # user_input_values DS contains all of the user input values
    # follow the indicated values below for their place in the array
    # 
    # 14 user input values
    # entity = user_input_values[0]
    # date = user_input_values[1]
    # cash_end = user_input_values[2]
    # credit_card = user_input_values[3]
    # turkey_returned = user_input_values[4]
    # ham_returned = user_input_values[5]
    # beef_returned = user_input_values[6]
    # turkey_price = user_input_values[7]
    # ham_price = user_input_values[8]
    # beef_price = user_input_values[9]
    # turkey_purchased = user_input_values[10]
    # ham_purchased = user_input_values[11]
    # beef_purchased = user_input_values[12]
    # bread_purchased = user_input_values[13]


    # Calculating the totals 

    # RAW indicated variables are used for calculations
    # CONVERTED indicated variables are used for printing

    # 
    CASH_START = 600

    # 
    cash_end_raw = user_input_values[2]
    cash_end_converted = user_input_values[2] / 100

    # 
    credit_card_raw = user_input_values[3]
    credit_card_converted = credit_card_raw / 100

    # 
    credit_card_tax_raw = 0
    credit_card_tax_converted = (credit_card_tax_raw * 3) / 100

    # 
    credit_card_net_raw = credit_card_raw - credit_card_tax_raw
    credit_card_net_converted = (credit_card_raw - credit_card_tax_raw) / 100

    # 
    total_sales_raw = (credit_card_net_raw + cash_end_raw) - CASH_START
    total_sales_converted = ((credit_card_net_raw + cash_end_raw) - CASH_START) / 100

    # 
    turkey_returned_lbs = 0
    ham_returned_lbs = 0
    beef_returned_lbs = 0

    # 
    turkey_price = 0
    ham_price = 0
    beef_price = 0

    # 
    turkey_purchased_lbs = 0
    ham_purchased_lbs = 0
    beef_purchased_lbs = 0

    # 
    bread_purchased = 0

    # 
    total_returned_raw = (turkey_returned_lbs * turkey_price) + (ham_returned_lbs * ham_price) + (beef_returned_lbs * beef_price)
    total_returned_converted = ((turkey_returned_lbs * turkey_price) + (ham_returned_lbs * ham_price) + (beef_returned_lbs * beef_price)) / 100

    # 
    gross_raw = total_returned_raw + total_sales_raw
    gross_converted = (total_returned_raw + total_sales_raw) / 100

    # 
    total_expenses_raw = (turkey_purchased_lbs * turkey_price) + (ham_purchased_lbs * ham_price) + (beef_purchased_lbs * beef_price) + bread_purchased
    total_expenses_converted = ((turkey_purchased_lbs * turkey_price) + (ham_purchased_lbs * ham_price) + (beef_purchased_lbs * beef_price) + bread_purchased) / 100

    # 
    profit_raw = gross_raw - total_expenses_raw
    profit_converted = (gross_raw - total_expenses_raw) / 100

    # 
    shared_profit_raw = profit_raw / 2
    shared_profit_converted = (profit_raw / 2) / 100
    





    # 

    # TODO: manually enter converted data values ✅
    converted_user_data = {
        "entity" : user_input_values[0],
        "date" : user_input_values[1],
        "cash_start" : 600,
        "cash_end" : cash_end_converted,
        "credit card": credit_card_converted,
        "credit card tax": credit_card_tax_converted,
        "credit card net": credit_card_net_converted,
        "total sales": total_sales_converted,
        "turkey returned (pounds)": turkey_returned_lbs,
        "ham returned (pounds)": ham_returned_lbs,
        "beef returned (pounds)": beef_returned_lbs,
        "turkey price": turkey_price,
        "ham price": ham_price,
        "beef price": beef_price,
        "bread purchased": bread_purchased,
        "total returned": total_returned_converted,
        "gross": gross_converted,
        "total expenses": total_expenses_converted,
        "profit": profit_converted,
        "shared": shared_profit_converted
    }


    return converted_user_data


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