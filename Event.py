# eventually will use pandas to create excel file
# import pandas

class Event():
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


    def calculate_totals(self):
        """
        this method aggregates all the relevant data used to generate the profit share document

        returns a dictionary of the local variables

        :return: locals()
        :rtype: dictionary
        """


        # variable order

        # entity name
        entity = self.entity
        # date
        date = self.date

        # sales
        # cash start
        CASH_START : float = 600.00
        # cash end
        cash_end = self.cash_end
        # credit card
        credit_card = self.credit_card
        # credit card tax
        credit_card_tax = self.credit_card * 0.03
        # credit card net
        credit_card_net = self.credit_card - credit_card_tax
        # total sales
        total_sales = (credit_card_net + self.cash_end) - CASH_START

        # returned
        # returned turkey
        turkey_returned = self.turkey_returned
        # returned ham
        ham_returned = self.ham_returned
        # returned beef
        beef_returned = self.beef_returned
        # turkey price
        turkey_price = self.turkey_price
        # ham price
        ham_price = self.ham_price
        # beef price
        beef_price = self.beef_price
        # total returned ( returned * price per pound )
        total_returned = ((self.turkey_returned * self.turkey_price) +
                          (self.ham_returned * self.ham_price) +
                          (self.beef_returned * self.beef_price))
        # gross ( total returned + total sales )
        gross = total_returned + total_sales

        # expenses
        # turkey purchased
        turkey_purchased = self.turkey_purchased
        # ham purchased
        ham_purchased = self.ham_purchased
        # beef purchased
        beef_purchased = self.beef_purchased
        # bread purchased
        bread_purchased = self.bread_purchased
        # bread total cost ( bread purchased * 10 )
        bread_total_cost = self.bread_purchased * 10
        # total expenses ( purchased meat * meat price ) + bread total cost
        total_expenses = ((self.turkey_purchased * self.turkey_price) +
                          (self.ham_purchased * self.ham_price) +
                          (self.beef_purchased * self.beef_price) +
                          bread_total_cost)
        # profit ( gross - total expenses )
        profit = gross - total_expenses
        # shared profit ( profit / 2 )
        shared = profit / 2


        print(f"Cash start: {CASH_START}")
        print(f"credit card tax: {credit_card_tax}")
        print(f"credit card net: {credit_card_net}")
        print(f"total sales: {total_sales}")
        print(f"total returned: {total_returned}")
        print(f"gross: {gross}")
        print(f"bread total cost: {bread_total_cost}")
        print(f"total expenses: {total_expenses}")
        print(f"profit: {profit}")
        print(f"shared: {shared}")


        return locals()


    def generate_excel_file(self, everything):
        """
        this method creates an excel file based off the variables in calculate_totals()
        :param everything:
        :type everything:
        :return:
        :rtype:
        """
        # file name
        file_name : str = self.date + "_" + self.entity
        pass


    # # CODE GRAVEYARD

    # #
    # entity : str = "" # user input
    # date : str = "" #user input

    # # 
    # CASH_START : float = 600.00
    # cash_end : float = 0.00 # user input
    # credit_card : float = 0.00 # user input
    # # 
    # credit_card_tax : float = credit_card * 0.03
    # # 
    # credit_card_net : float = credit_card - credit_card_tax
    # # 
    # total_sales : float = (credit_card_net + cash_end) - CASH_START

    # # returned meat
    # turkey_returned : float = 0 # user input
    # ham_returned : float = 0 # user input
    # beef_returned : float = 0 # user input
    # # 
    # turkey_price : float = 0 # user input
    # ham_price : float = 0 # user input
    # beef_price : float = 0 # user input
    # # 
    # total_returned : float = (turkey_returned * turkey_price) + (ham_returned * ham_price) + (beef_returned * beef_price)
    # # 
    # gross = total_returned + total_sales

    # # expenses
    # turkey_purchased : float = 0 # user input
    # ham_purchased : float = 0 # user input
    # beef_purchased : float = 0 # user input
    # bread_purchased : int = 0 # user input
    # bread_total_cost : int = bread_purchased * 10
    # # 
    # total_expenses : float = (turkey_purchased * turkey_price) + (ham_purchased * ham_price) + (beef_purchased * beef_price) + bread_total
    # # 
    # profit : float = gross - total_expenses
    # # 
    # shared : float = profit / 2