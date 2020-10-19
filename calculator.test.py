import unittest
from calculator import *

class test_calculator(unittest.TestCase):
    def main(self):
        self.only_numbers()
        self.zero_division()
        self.zero_division_raiz()
        self.odd_number_raiz()
        self.other_menu_option()

    def only_numbers(self):
        self.assertEqual(switch(1, "j", 4), "Sólo se deben ingresar numeros")
        self.assertEqual(switch(1, 5, 4), 9)

    def zero_division(self):
        self.assertEqual(switch(4, 5, 0), "Error: Division entre cero...")
    
    def zero_division_raiz(self):
        self.assertEqual(switch(6, 2, 0), "Error matematico")

    def odd_number_raiz(self):
        self.assertEqual(switch(6, 8, 3), 2)
        self.assertEqual(switch(6, 27, 3), 3)
        self.assertEqual(switch(6, 81, 2), 9)

    def other_menu_option(self):
        self.assertEqual(switch(7, 1, 2), "Opcion Invalida")


test = test_calculator()
test.main()