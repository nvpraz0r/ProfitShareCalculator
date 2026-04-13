import os # used to clear terminal screen

class Utils:
    # clear the screen
    def clear_screen():
        """
        Docstring for clear_screen
        """
        # For windows
        if os.name == 'nt':
            _ = os.system('cls')
        # For mac and linux (bash systems)
        else:
            _ = os.system('clear')


    # check if input is a valid float
    # @staticmethod
    def input_validation_float(prompt):
        """
        Docstring for input_validation_float
        
        :param prompt: Description
        """
        while True:
            try:
                result : float = float(input(f"Please enter the {prompt}.\n"))
                print(result)
                return result
            except ValueError:
                print("Invalid input. Please enter the correct information.")
                # wait for 2 seconds
                # clear screen
                # print menu


    # check if input is a valid string
    # @staticmethod
    def input_validation_string(prompt):
        """
        Docstring for input_validation_string
        
        :param prompt: Description
        """
        while True:
            try:
                result : str = str(input(f"Please enter the {prompt}.\n"))
                print(result)
                return result
            except ValueError:
                print("Invalid input. Please enter the correct information.")
                # wait for 2 seconds
                # clear screen
                # print menu


    # helper method that directs the flow
    # of which method should be used to
    # validate user input
    #
    # switch case
    # 1 = float
    # 2 = string
    def get_validation_method(self, prompt, prompt_data_type):
        """
        Docstring for get_validation_method
        
        :param prompt: Description
        :param prompt_data_type: Description
        """    
        # switch case
        # 1 = float
        # 2 = string
        match prompt_data_type:
            case 1:
                # float
                return Utils.input_validation_float(prompt)
            case 2:
                # string
                return Utils.input_validation_string(prompt)
            case _:
                print("Error occurred somewhere during the validation process.")


    # display intro header
    def intro_to_application(self):
        print("         Profit Share Calculator")
        print("+-----------------------------------------+")
        print("|                                         |")
        print("| This Program is designed to generate    |")
        print("| an excel spreadsheet.                   |")
        print("|                                         |")
        print("+-----------------------------------------+")
        print()