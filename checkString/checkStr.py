
"""Simple Alphabet Checker"""


class CheckStr:
    """Check if the input has all the alphabets """
    def __init__(self):
        # predefine your alphabets
        self.match_string = 'abcdefghijklmnopqrstuvwxyz'
    
    def check_alpha(self, input_string):
        if str(input_string) == 'None':
            return False
        elif len(input_string) < 26:
            return False
        else:
            lowercase_input_list = list(str(input_string).lower())
            # run loop 26 times to make sure all the alphabets are present in the input string
            return all(each_alpha in lowercase_input_list for each_alpha in self.match_string)

