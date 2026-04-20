import os # used to clear terminal screen
import time

class Utils:
    # clear the screen
    def clear_console():
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
    def input_validation_float(prompt):
        """
        Docstring for input_validation_float
        
        :param prompt: Description
        """
        while True:
            try:
                result = int(input(f"Please enter the {prompt}.\n"))
                return result
            except ValueError:
                print("Invalid input. Please enter the correct information.")
                # wait for 2 seconds
                time.sleep(2)
                # clear_console()


    # check if input is a valid string
    def input_validation_string(prompt):
        """
        Docstring for input_validation_string
        
        :param prompt: Description
        """
        while True:
            try:
                result = input(f"Please enter the {prompt}:\n")
                if not result.isalpha():
                    raise ValueError
                return result
            except ValueError:
                print("Invalid input. Please enter the correct information.")
                # wait for 2 seconds
                time.sleep(2)
                # clear_console()


    def get_validation_method(self, prompt, prompt_data_type):
        """
        Docstring for get_validation_method:
        helper method that directs the flow of which method should be used to get user input. 1 for int, 2 for string
        
        :param prompt: Description
        :param prompt_data_type: Description
        """    
        # switch case
        # 1 = int
        # 2 = string
        match prompt_data_type:
            case 1:
                # int
                return Utils.input_validation_float(prompt)
            case 2:
                # string
                return Utils.input_validation_string(prompt)
            case _:
                print("Error occurred somewhere during the validation process.")
                return None


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