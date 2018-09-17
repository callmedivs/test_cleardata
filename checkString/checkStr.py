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
            lowercase_input = str(input_string).lower()
            # using sets
            return set(lowercase_input) >= set(self.match_string)
