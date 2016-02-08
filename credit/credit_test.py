#!/usr/bin/python
import unittest
from credit import lineOfCredit


class lineOfCreditTest(unittest.TestCase):

    # Scenario one from instructions
    def test_scenario_one(self):
        loc = lineOfCredit(0.35, 1000)
        loc.makeWithdrawl(500)
        loc.progressDays(30)
        assert loc.interest == 14.38
        assert loc.balance == 500

    # Scenario two from instructions
    def test_scenario_two(self):
        loc = lineOfCredit(0.35, 1000)
        loc.makeWithdrawl(500)
        loc.progressDays(15)
        loc.makePayment(200)
        loc.progressDays(10)
        loc.makeWithdrawl(100)
        loc.progressDays(5)
        assert loc.interest == 11.99
        assert loc.balance == 400

    # def test3():
    #     loc = lineOfCredit(0.35, 500)
    #     loc.makeWithdrawl(500)


if __name__ == '__main__':
    unittest.main()