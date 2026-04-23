# This class has been sunsetted


# class Event:
#     def __init__(self,
#                  entity, date, cash_end, credit_card,
#                  turkey_returned, ham_returned, beef_returned,
#                  turkey_price, ham_price, beef_price,
#                  turkey_purchased, ham_purchased, beef_purchased,
#                  bread_purchased):
        
#         # user input
#         self.entity = entity
#         self.date = date

#         # amount of cash in the bank before and after the event
#         self.CASH_START = 600
#         self.cash_end = cash_end

#         # credit card sales
#         self.credit_card = credit_card
#         # credit card tax - we take three percent to cover CC fees
#         # self.credit_card_tax = (self.credit_card * 3) / 100
#         self.credit_card_tax = self.credit_card * 3
#         # credit card net
#         self.credit_card_net = self.credit_card - self.credit_card_tax
        
#         # total amount of money generated BEFORE all things considered
#         self.total_sales = (self.credit_card_net + self.cash_end) - self.CASH_START

#         # amount of meat RETURNED
#         self.turkey_returned = turkey_returned
#         self.ham_returned = ham_returned
#         self.beef_returned = beef_returned

#         # PRICE of meat purchased
#         self.turkey_price = turkey_price
#         self.ham_price = ham_price
#         self.beef_price = beef_price

#         # AMOUNT of meat purchased
#         self.turkey_purchased = turkey_purchased
#         self.ham_purchased = ham_purchased
#         self.beef_purchased = beef_purchased

#         # AMOUNT of bread purchased
#         self.bread_purchased = bread_purchased

#         # bread total cost ( bread purchased * 10 )
#         self.bread_total_cost = self.bread_purchased * 10
        
#         # total cost of meat RETURNED
#         # total returned ( returned * price per pound )
#         self.total_returned = ((self.turkey_returned * self.turkey_price) +
#                           (self.ham_returned * self.ham_price) +
#                           (self.beef_returned * self.beef_price))
        
#         # total cost of 
#         # gross ( total returned + total sales )
#         self.gross = self.total_returned + self.total_sales

#         # total expenses ( purchased meat * meat price ) + bread total cost
#         self.total_expenses = ((self.turkey_purchased * self.turkey_price) +
#                           (self.ham_purchased * self.ham_price) +
#                           (self.beef_purchased * self.beef_price) +
#                           self.bread_total_cost)
        
#         # profit ( gross - total expenses )
#         self.profit = self.gross - self.total_expenses

#         # shared profit ( profit / 2 )
#         self.shared: int = self.profit / 2




        # 
        # Code graveyard
        # 
        # test retrieval of class attributes
        # vars() with an instance variable is the solution
        # attributes_dict_vars = vars(myvar)
        # print(f"Using vars(): {attributes_dict_vars}")