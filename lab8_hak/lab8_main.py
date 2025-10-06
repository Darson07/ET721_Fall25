'''
Darson Hak
Lab #8: Unit Testing
09/29/2025
'''
import unittest
import calculations
from bankaccount import *

# Function to add and return the sum of two numbers
def addtwonumbers(a,b):
    return a+b

print("\n----- Example #1: Test for Equality -----")
# create a unit to test function "addtwonumbers"
class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(addtwonumbers(2,3),5)



print("\n----- Example #2: Unittest for Calculations -----")
class TestCalculation(unittest.TestCase):
    def test_multiplication(self):
        self.assertEqual(calculations.multiplythreenumbers(5),5)
        self.assertEqual(calculations.multiplythreenumbers(2,3),6)
        self.assertEqual(calculations.multiplythreenumbers(2,3,4),24)
        self.assertEqual(calculations.multiplythreenumbers(0),0)

    def test_division(self):
        self.assertEqual(calculations.dividetwonumbers(8,4),2)
        self.assertAlmostEqual(calculations.dividetwonumbers(9,2),4.5)
        self.assertEqual(calculations.dividetwonumbers(9,0),-1)
        self.assertIsNone(calculations.multiplythreenumbers("a",2))

print("\n----- Lab #8 Lab -----")
class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(owner = "Darson", balance = 100)

    def test_initial(self):
        self.assertEqual(self.account.get_balance(), 100)

    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.get_balance(), 150)

    def test_withdraw(self):
        self.account.withdraw(30)
        self.assertEqual(self.account.get_balance(), 70)

    def test_withdraw_more(self):
        self.assertRaises(ValueError, self.account.withdraw, 200)

    def test_sequence_of_transactions(self):
        self.account.deposit(100)
        self.account.withdraw(50)
        self.account.deposit(25)
        self.account.withdraw(75)
        self.assertEqual(self.account.get_balance(), 100)

if __name__ == "__main__":
    unittest.main()