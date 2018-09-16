import unittest

from checkStr import *


class Test_CheckStr(unittest.TestCase):

    # test method used to verify false inputs
    def test_false_checkStr(self):
        test_str_check = CheckStr()
        test_strings = ['abcdefghij',
                        '12324567',
                        '65432765234\n3454364',
                        'abcd',
                        '1234567890',
                        '1234567890$$$$%2%3%4',
                        '1234567890$$$$%2%3%4',
                        '',
                        'abcd efght ijklmnopqrstuvw 123##'
                        ]

        for each_str in test_strings:
            self.assertEqual(test_str_check.check_alpha(each_str), False)

    def test_true_checkStr(self):
        # test method used to verify true inputs
        test_str_check = CheckStr()
        test_strings = ['abcdefghijklmnopqrstuvwxyz',
                        'abcdefghijklmnopqrstuvwXYZZ',
                        '12345abcdefghijklmnopqrstuvwXYZZ%%%%',
                        '   abcdefghijklmnopqrstuvwXYZZ  ',
                        'xyzaaaabcdefghijklmnopqrstuvw'
                        ]
        for each_str in test_strings:
            self.assertEqual(test_str_check.check_alpha(each_str), True)


# runs the unit tests in the module
if __name__ == '__main__':
    unittest.main()