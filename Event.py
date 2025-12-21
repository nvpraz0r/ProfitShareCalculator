
class Event():

    #
    entity : str = ""
    date : str = ""

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

    def generate_file():
        pass