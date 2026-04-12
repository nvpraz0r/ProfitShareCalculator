class Event:
    def __init__(self,
                 entity, date, cash_end, credit_card,
                 turkey_returned, ham_returned, beef_returned,
                 turkey_price, ham_price, beef_price,
                 turkey_purchased, ham_purchased, beef_purchased,
                 bread_purchased):
        """
        :param entity:
        :param date:

        :param cash_end:
        :param credit_card:

        :param turkey_returned:
        :param ham_returned:
        :param beef_returned:

        :param turkey_price:
        :param ham_price:
        :param beef_price:

        :param turkey_purchased:
        :param ham_purchased:
        :param beef_purchased:

        :param bread_purchased:
        """


        # user input
        self.entity = entity
        self.date = date

        # amount of cash in the bank before and after the event
        self.CASH_START : float = 600.00
        self.cash_end = cash_end

        # credit card sales
        self.credit_card = credit_card
        # credit card tax - we take three percent to cover CC fees
        self.credit_card_tax = self.credit_card * 0.03
        # credit card net
        self.credit_card_net = self.credit_card - self.credit_card_tax
        
        # total amount of money generated BEFORE all things considered
        self.total_sales = (self.credit_card_net + self.cash_end) - self.CASH_START

        # amount of meat RETURNED
        self.turkey_returned = turkey_returned
        self.ham_returned = ham_returned
        self.beef_returned = beef_returned

        # PRICE of meat purchased
        self.turkey_price = turkey_price
        self.ham_price = ham_price
        self.beef_price = beef_price

        # AMOUNT of meat purchased
        self.turkey_purchased = turkey_purchased
        self.ham_purchased = ham_purchased
        self.beef_purchased = beef_purchased

        # AMOUNT of bread purchased
        self.bread_purchased = bread_purchased

        # bread total cost ( bread purchased * 10 )
        self.bread_total_cost = self.bread_purchased * 10.00
        
        # total cost of meat RETURNED
        # total returned ( returned * price per pound )
        self.total_returned = ((self.turkey_returned * self.turkey_price) +
                          (self.ham_returned * self.ham_price) +
                          (self.beef_returned * self.beef_price))
        
        # total cost of 
        # gross ( total returned + total sales )
        self.gross = self.total_returned + self.total_sales

        # total expenses ( purchased meat * meat price ) + bread total cost
        self.total_expenses = ((self.turkey_purchased * self.turkey_price) +
                          (self.ham_purchased * self.ham_price) +
                          (self.beef_purchased * self.beef_price) +
                          self.bread_total_cost)
        
        # profit ( gross - total expenses )
        self.profit = self.gross - self.total_expenses

        # shared profit ( profit / 2 )
        self.shared = self.profit / 2






    # # CODE GRAVEYARD

    # REFACTOR TO STORE CALCULATED TOTALS IN THE GLOBAL VARIABLES
    # def calculate_totals(self):
    #     """
    #     this method aggregates all the relevant data used to generate the profit share document

    #     returns a dictionary of the local variables

    #     :return: locals()
    #     :rtype: dictionary
    #     """


    #     # variable order

    #     # entity name
    #     entity = self.entity
    #     # date
    #     date = self.date

    #     # sales
    #     # cash start
    #     CASH_START : float = 600.00
    #     # cash end
    #     cash_end = self.cash_end
    #     # credit card
    #     credit_card = self.credit_card
    #     # credit card tax
    #     credit_card_tax = self.credit_card * 0.03
    #     # credit card net
    #     credit_card_net = self.credit_card - credit_card_tax
    #     # total sales
    #     total_sales = (credit_card_net + self.cash_end) - CASH_START

    #     # returned
    #     # returned turkey
    #     turkey_returned = self.turkey_returned
    #     # returned ham
    #     ham_returned = self.ham_returned
    #     # returned beef
    #     beef_returned = self.beef_returned
    #     # turkey price
    #     turkey_price = self.turkey_price
    #     # ham price
    #     ham_price = self.ham_price
    #     # beef price
    #     beef_price = self.beef_price
    #     # total returned ( returned * price per pound )
    #     total_returned = ((self.turkey_returned * self.turkey_price) +
    #                       (self.ham_returned * self.ham_price) +
    #                       (self.beef_returned * self.beef_price))
    #     # gross ( total returned + total sales )
    #     gross = total_returned + total_sales

    #     # expenses
    #     # turkey purchased
    #     turkey_purchased = self.turkey_purchased
    #     # ham purchased
    #     ham_purchased = self.ham_purchased
    #     # beef purchased
    #     beef_purchased = self.beef_purchased
    #     # bread purchased
    #     bread_purchased = self.bread_purchased
    #     # bread total cost ( bread purchased * 10 )
    #     bread_total_cost = self.bread_purchased * 10
    #     # total expenses ( purchased meat * meat price ) + bread total cost
    #     total_expenses = ((self.turkey_purchased * self.turkey_price) +
    #                       (self.ham_purchased * self.ham_price) +
    #                       (self.beef_purchased * self.beef_price) +
    #                       bread_total_cost)
    #     # profit ( gross - total expenses )
    #     profit = gross - total_expenses
    #     # shared profit ( profit / 2 )
    #     shared = profit / 2


    #     # print(f"Cash start: {CASH_START}")
    #     # print(f"credit card tax: {credit_card_tax}")
    #     # print(f"credit card net: {credit_card_net}")
    #     # print(f"total sales: {total_sales}")
    #     # print(f"total returned: {total_returned}")
    #     # print(f"gross: {gross}")
    #     # print(f"bread total cost: {bread_total_cost}")
    #     # print(f"total expenses: {total_expenses}")
    #     # print(f"profit: {profit}")
    #     # print(f"shared: {shared}")


    #     return locals()