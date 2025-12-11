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



    get_user_input("entity", 2)









# helper method that directs the flow
# of which method should be used to
# validate user input
#
# should I even bother..?
def get_validation_method(prompt, prompt_data_type):    
    
    # switch case
    # 1 = float
    # 2 = string
    # 3 = date
    match prompt_data_type:
        case 1:
            # float
            input_validation_float(prompt)
            pass
        case 2:
            # string
            input_validation_string(prompt)
            pass
        case 3:
            # date year/month/day
            input_validation_date(prompt)
            pass
        case _:
            print("Unknown error. Good luck!")


def input_validation_float(input):

    while True:
        try:
            number = float(input(f"Please enter the {input}"))
            print(number)
            break
        except ValueError:
            print("Invalid input. Please enter the correct information.")
            # wait for 2 seconds
            # clear screen
            # print menu


def input_validation_string(input):

    while True:
        try:
            number = float(input(f"Please enter the {input}"))
            print(number)
            break
        except ValueError:
            print("Invalid input. Please enter the correct information.")
            # wait for 2 seconds
            # clear screen
            # print menu


def input_validation_date(input):

    while True:
        try:
            number = float(input(f"Please enter the {input}"))
            print(number)
            break
        except ValueError:
            print("Invalid input. Please enter the correct information.")
            # wait for 2 seconds
            # clear screen
            # print menu