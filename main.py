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

    profit : float = total_sales - total_expenses

    shared : float = profit / 2

    # stuff here