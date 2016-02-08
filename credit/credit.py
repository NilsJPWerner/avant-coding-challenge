#!/usr/bin/python


class lineOfCredit(object):
    """
    Line of credit class: Simulates a line of credit where you have an apr
    a line of credit and you can make payments and withdrawls. A history of your
    transactions are kept, interest is calculated at the end of each thirty
    day period
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
        """
        Progresses days of the loc simulation. If the function reaches or passes a
        period end, it will run periodEnd
        """
        if (days <= 0):
            raise ValueError("You're days cannot be negative or zero")
        for i in range(days):
            self.day += 1
            if (self.day % 30 == 0):
                self.periodEnd()

    def currentDay(self):
        """
        Prints the current day and the remaining days in the period
        Note:   The remaining days are from the current day to the start of
                the next period
        """
        print "Current day: " + str(self.day)
        print "Days remaining in billing period: " + str(30 - (self.day % 30))

    def makePayment(self, payment):
        """
        Make payments on the line of credit.
        Assumptions:    Any payments go to paying off interest before paying
                        the balance
                        You can't pay more than your total outstanding dues
        """
        if (payment < 0):
            raise ValueError("You're payment cannot be negative")
        elif (payment > self.balance + self.interest):
            raise ValueError("You're payment is higher than your current\
             balance and interest")
        elif (payment > self.interest):
            self.balance -= (payment - self.interest)
            self.interest = 0
        else:
            self.interest -= payment
        transaction = (self.day, payment*-1, self.balance)
        self.transactions.append(transaction)

    def makeWithdrawl(self, withdrawl):
        """
        Draws money from the credit line. Will throw a ValueError if the
        withdrawl is more than the available credit
        Assumption: That the current interest counts against the available
                    credit
        """
        if (withdrawl < 0):
            raise ValueError("You're withdrwal cannot be negative")
        elif (withdrawl > self.credit - (self.balance + self.interest)):
            raise ValueError("You cannot withdraw that much. It would exceed\
                your available credit")
        else:
            self.balance += withdrawl
        transaction = (self.day, withdrawl, self.balance)
        self.transactions.append(transaction)

    def creditRemaining(self):
        """
        Prints the remaining credit on the loc
        Note:   Negative remaining credit is possible if interest accumulates
                too much
        """
        print "You remaining credit is: " + str(self.credit - (self.balance +
            self.interest))

    def truncate(self, number):
        """
        Rounds the input number to the nearest cent and then truncates it to
        two decimal places.
        Note:   It might be better to ceiling it rather than round so that the
                bank never loses money, but I'm not sure if thats appropriate
        """
        return int(round(number, 2)*100) / 100.0

    def periodEnd(self):
        """
        Calculates interest at the end of the 30 day period and pushes
        transactions to history. It also carries over any remaining balance
        to the next month through the carryover variable so that interest can be
        charged for then next month
        Assumption: Interest is not added to the balance since it is not
                    compounded
        """
        period_interest = 0
        day_counter = 30
        for trans in reversed(self.transactions):
            trans_day = trans[0] % 30
            period_interest += (trans[2] * self.apr) / 365 * (day_counter -
                trans_day)
            day_counter = trans_day

        # If there was carryover from the period preceding this one
        if (self.carryover > 0):
            period_interest += ((self.carryover * self.apr) / 365 *
                (day_counter - 0))
            self.carryover = 0

        period_interest = self.truncate(period_interest)

        self.interest += period_interest
        self.history = self.history + self.transactions

        if (self.balance > 0):
            self.carryover = self.balance

        # print "Interest accrued this month: " + str(period_interest)
        # print "Current payment due: " + str(self.balance +
        #    self.interestinterest)

    def paymentDue(self):
        """
        Prints the current payment due (interest and balance)
        """
        print "Current payment due: " + str(self.interest + self.balance)
