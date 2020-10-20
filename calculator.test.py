import unittest
from calculator import *

class test_calculator(unittest.TestCase):
    def main(self):
        self.ideal_cases()
        self.only_numbers()
        self.zero_division()
        self.zero_division_root()
        self.number_root()
        self.other_menu_option()
        self.square_root_negative()

    def ideal_cases(self):
        """
            Check the ideal cases
        """
        self.assertEqual(switch(1, 1, 4), 5)
        self.assertEqual(switch(2, 5, 4), 1)
        self.assertEqual(switch(3, 5, 4), 20)
        self.assertEqual(switch(4, 8, 4), 2)
        self.assertEqual(switch(5, 2, 4), 16)
        self.assertEqual(switch(6, 8, 3), 2)
        

    def only_numbers(self):
        """
            Verifies if the numbers are not a string
        """
        self.assertEqual(switch(1, "j", 4), "Sólo se deben ingresar numeros")
        self.assertEqual(switch(1, 5, 4), 9)

    def zero_division(self):
        """
            Test if the division by zero is verified
        """
        self.assertEqual(switch(4, 5, 0), "Error: Division entre cero...")
    
    def zero_division_root(self):
        """
            Test if the root is valid
        """
        self.assertEqual(switch(6, 2, 0), "Error matematico")

    def number_root(self):
        """
            Test if the root returns a valid result
        """
        self.assertEqual(switch(6, 8, 3), 2)
        self.assertEqual(switch(6, 27, 3), 3)
        self.assertEqual(switch(6, 81, 2), 9)

    def other_menu_option(self):
        """
            Test if the options doest not match with the valid ones.
        """
        self.assertEqual(switch(7, 1, 2), "Opcion Invalida")

    def square_root_negative(self):
        """
            Test if the square root of a negative number throws an error.
        """
        self.assertEqual(switch(6, -2, 2), "Error matematico")

test = test_calculator()
test.main()