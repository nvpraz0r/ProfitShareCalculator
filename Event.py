# eventually will use pandas to create excel file
# import pandas

class Event():

    #
    entity : str = "" # user input
    date : str = "" #user input

    # 
    CASH_START : float = 600.00
    cash_end : float = 0.00 # user input
    credit_card : float = 0.00 # user input
    # 
    credit_card_tax : float = credit_card * 0.03
    # 
    credit_card_net : float = credit_card - credit_card_tax
    # 
    total_sales : float = (credit_card_net + cash_end) - CASH_START

    # returned meat
    turkey_returned : float = 0 # user input
    ham_returned : float = 0 # user input
    beef_returned : float = 0 # user input
    # 
    turkey_price : float = 0 # user input
    ham_price : float = 0 # user input
    beef_price : float = 0 # user input
    # 
    total_returned : float = (turkey_returned * turkey_price) + (ham_returned * ham_price) + (beef_returned * beef_price)
    # 
    gross = total_returned + total_sales

    # expenses
    turkey_purchased : float = 0 # user input
    ham_purchased : float = 0 # user input
    beef_purchased : float = 0 # user input
    bread : int = 0 # user input
    bread_total : int = bread * 10
    # 
    total_expenses : float = (turkey_purchased * turkey_price) + (ham_purchased * ham_price) + (beef_purchased * beef_price) + bread_total
    # 
    profit : float = gross - total_expenses
    # 
    shared : float = profit / 2

    # file name
    file_name : str = date + "_" + entity

    # Every variable will go into this array
    class_var_list = {}

    event_responses = []

    def __init__(self,
                 entity, date, cash_end, credit_card,
                 turkey_returned, ham_returned, beef_returned,
                 turkey_price, ham_price, beef_price,
                 turkey_purchased, ham_purchased, beef_purchased,
                 bread_purchased):
        self.entity = entity
        self.date = date
        self.cash_end = cash_end
        self.credit_card = credit_card
        self.turkey_returned = turkey_returned
        self.ham_returned = ham_returned
        self.beef_returned = beef_returned
        self.turkey_price = turkey_price
        self.ham_price = ham_price
        self.beef_price = beef_price
        self.turkey_purchased = turkey_purchased
        self.ham_purchased = ham_purchased
        self.beef_purchased = beef_purchased
        self.bread_purchased = bread_purchased


    # Am I able to prevent calling this before the variables have been populated?
    # If not no big deal this is a personal project
    def generate_array():
        """
        This method populates the class_var_list with the class Event variables.
        """
        # I have no idea how this works
        # by the looks of it - it prints all the variables in the class
        class_var_list = [value for key, value in Event.__dict__.items() if not key.startswith('_') and not callable(value)]
        print(class_var_list)


    # This method generates the excel file with the help of generate_array() method
    def generate_file(everything):
        pass


    # in order to access global variables
    # use "global foo"
    def test_responses(responses):
        global event_responses
        event_responses = responses
    
    def print_responses():
        global event_responses
        print(event_responses)