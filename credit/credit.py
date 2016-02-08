#!/usr/bin/python

class lineOfCredit(object):
    """ Line of credit class: Simulates a line of credit where you have an apr
    a line of credit and you can make payments and withdrawls. A history of your
    transactions are kept, interest is calculated at the end of each 30 day period
    Attributes:
        apr             Apr for this loc
        credit          Maximum credit available
        balance         Current balance for this loc
        interest        Current interest due
        carryover       The carryover balance between months
        day             Current day, starts at zero
        transactions    Payments and withdrawls this month. A list of tuples:
                        tuple[0] = day of transaction
                        tuple[1] = transaction amount
                        tuple[2] = balance after transaction
        history         History of transactions over all prior months
    """

    def __init__(self, apr, credit):
        self.apr = apr
        self.credit = credit
        self.balance = 0
        self.interest = 0
        self.carryover = 0
        self.day = 0
        self.transactions = []
        self.history = []

    def progressDays(self, days):
        if (days < 0):
            raise ValueError("You're days cannot be negative")
        for i in range(days):
            self.day += 1
            if (self.day % 30 == 0):
                self.periodEnd()

    def currentDay(self):
        print "Current day: " + str(self.day)
        print "Days remaining in billing period: " + str(30 - (self.day % 30))

    def makePayment(self, payment):
        """ Make payments towards on the balance and interest rate.
        Assumption: Any payments go to paying off interest before paying the balance
        """
        if (payment < 0):
            raise ValueError("You're payment cannot be negative")
        elif (payment > self.balance + self.interest):
            raise ValueError("You're payment is higher than your current balance and interest")
        elif (payment > self.interest):
            self.balance -= (payment - self.interest)
            self.interest = 0
        else:
            self.interest -= payment
        transaction = (self.day, payment*-1, self.balance)
        self.transactions.append(transaction)

    def makeWithdrawl(self, withdrawl):
        """ Draw money from the credit line.
        Assumption: That the current interest counts against the available credit
        """
        if (withdrawl < 0):
            raise ValueError("You're withdrwal cannot be negative")
        elif (withdrawl > self.credit - (self.balance + self.interest)):
            raise ValueError("You cannot withdraw that much. It would exceed your available credit")
        else:
            self.balance += withdrawl
        transaction = (self.day, withdrawl, self.balance)
        self.transactions.append(transaction)

    def creditRemaining(self):
        print "You remaining credit is: " + str(self.credit - (self.balance + self.interest))

    def truncate(self, number):
        return int(round(number, 2)*100) / 100.0

    def periodEnd(self):
        """ Calculates interest at the end of the 30 day period and
        pushes transactions to history. It also carries over any remaining
        balance to the next month through the carryover variable so that
        interest can be charged to it if a
        Assumption: Interest is not added to the balance since it is not compounded
        """
        period_interest = 0
        day_counter = 30
        for trans in reversed(self.transactions):
            trans_day = trans[0] % 30
            period_interest += (trans[2] * self.apr) / 365 * (day_counter - trans_day)
            day_counter = trans_day

        if (self.carryover > 0):
            period_interest += (self.carryover * self.apr) / 365 * (day_counter - 0)
            self.carryover = 0

        period_interest = self.truncate(period_interest)

        self.interest += period_interest
        self.history = self.history + self.transactions

        if (self.balance > 0):
            self.carryover = self.balance

        # print "Interest accrued this month: " + str(period_interest)
        # print "Current payment due: " + str(self.balance + self.interestinterest)

    def paymentDue(self):
        print "Current payment due: " + str(self.interest + self.balance)







