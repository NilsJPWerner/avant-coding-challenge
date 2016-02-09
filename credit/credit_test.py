#!/usr/bin/python
import unittest
from credit import lineOfCredit


class lineOfCreditTest(unittest.TestCase):

    # Scenario one from instructions
    def test_scenario_1(self):
        loc = lineOfCredit(0.35, 1000)
        loc.makeWithdrawal(500)
        loc.progressDays(30)
        assert loc.interest == 14.38
        assert loc.balance == 500

    # Scenario two from instructions
    def test_scenario_2(self):
        loc = lineOfCredit(0.35, 1000)
        loc.makeWithdrawal(500)
        loc.progressDays(15)
        loc.makePayment(200)
        loc.progressDays(10)
        loc.makeWithdrawal(100)
        loc.progressDays(5)
        assert loc.interest == 11.99
        assert loc.balance == 400

    def test_scenario_3(self):
        loc = lineOfCredit(0.1, 1000)
        loc.makeWithdrawal(500)
        loc.progressDays(60)
        assert loc.interest == 8.22

    def test_withdraw(self):
        loc = lineOfCredit(0.35, 1000)
        loc.makeWithdrawal(100)
        assert loc.balance == 100
        loc.makeWithdrawal(100)
        assert loc.balance == 200

    def test_withdraw_too_much(self):
        loc = lineOfCredit(0.35, 1000)
        self.assertRaises(ValueError, loc.makeWithdrawal, 1001)

    def test_withdraw_negative(self):
        loc = lineOfCredit(0.35, 1000)
        self.assertRaises(ValueError, loc.makeWithdrawal, -1)

    def test_withdraw_invalid_value(self):
        loc = lineOfCredit(0.35, 1000)
        self.assertRaises(ValueError, loc.makeWithdrawal, 0.1111)

    def test_progress_days(self):
        loc = lineOfCredit(0.35, 1000)
        loc.progressDays(15)
        assert loc.day == 15

    def test_progress_days_negative(self):
        loc = lineOfCredit(0.35, 1000)
        self.assertRaises(ValueError, loc.progressDays, -1)

    def test_progress_days_float(self):
        loc = lineOfCredit(0.35, 1000)
        self.assertRaises(ValueError, loc.progressDays, 0.1)

    def test_full_payment(self):
        loc = lineOfCredit(0.35, 1000)
        loc.makeWithdrawal(500)
        loc.progressDays(30)
        loc.makeFullPayment()
        assert loc.interest == 0
        assert loc.balance == 0

    def test_payment(self):
        loc = lineOfCredit(0.35, 1000)
        loc.makeWithdrawal(500)
        loc.progressDays(30)
        loc.makePayment(500)
        loc.makePayment(14.38)
        assert loc.balance == 0.0
        assert loc.interest == 0.0

    def test_payment_negative(self):
        loc = lineOfCredit(0.35, 1000)
        loc.makeWithdrawal(500)
        self.assertRaises(ValueError, loc.makePayment, -1)

    def test_payment_invalid_value(self):
        loc = lineOfCredit(0.35, 1000)
        loc.makeWithdrawal(500)
        self.assertRaises(ValueError, loc.makePayment, 0.111)

    def test_payment_too_much(self):
        loc = lineOfCredit(0.35, 1000)
        loc.makeWithdrawal(500)
        loc.progressDays(30)
        self.assertRaises(ValueError, loc.makePayment, 514.39)

    def truncate(self):
        loc = lineOfCredit(0.35, 1000)
        assert loc.truncate(1.111) == 1.11
        assert loc.truncate(1.1) == 1.1
        assert loc.truncate(1.115) == 1.12


if __name__ == '__main__':
    unittest.main()
