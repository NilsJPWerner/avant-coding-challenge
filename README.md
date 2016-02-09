# Coding Challenge for Avant

## Factors

This is the first time I've written ruby, so I apologize if I missed some style errors.

### Question 1

I currently have a caching system in my implementation that skips finding factors for values already computed. If it finds a factor it also checks to see if that factor is in the cache and if so adds the (non-duplicate) factors of that factor to the values array of factors so that it can leverage the precomputed factors of factors (since they will all be factors of the original value as well). 

Filesystem?


### Question 2

- The simplest and least efficient implementation of this problem would be just to loop through all the values and test each value pairwise resulting in o(n^2) time complexity. My implementation while still effectively looping through all the values, skips values already in the cache and include the factors of factors already calculated.
- If we know the average maximum value of inputs, we could precompute factors up to this number (if space is not a huge issue) and put them in a lookup table and then pick out the factors that appear in the array and the table. This would eliminate the need to do any factorization in real time, as the only computation would be lookups in the table and the array. However if this table is too large to load into memory, the time spent fetching the values from disk would outweigh the benefits of not having to factorize.


## Line of Credit

This challenge is written in python 2.7

###Instructions
1. Open a python shell in the credit directory with `python`
2. Import the line of credit class with `from credit import lineOfCredit`
3. Create a new instance with `loc = lineOfCredit(apr, credit)` with the chosen values for apr and credit.

To run the tests type python credit_test -v in terminal

###Supported operations:
- `loc.makeWithdrawal(100)` - Draws the chosen amount from the account.
- `loc.makePayment(100)` - Pays the chosen amount into the account. Note that interest will be paid off before the balance.
- `loc.makeFullPayment()` - Pays the balance and interest in full.
- `loc.progressDays(10)` - Progresses days by the chosen number. If the simulation reaches the end of a period, interest calculations are automatically calculated and the transactions of that period are pushed to the account history.
- `loc.currentDay()` - Prints the current day of the simulation and the remaining days before the end of the period.
- `loc.paymentDue()` - Prints the current payment due (balance and interest).
- `loc.creditRemaining()` - Prints the remaining available credit. Note that a negative available credit is possible if interest accumulates to the point where the balance and interest are higher than the credit.
- `getPastTransaction(10)` - Prints the transactions that happened on the selected day.

###Notes and assumptions
- I assume that interest is calculated and payment is due on the first day of the next billing period.
- I also assume that if two or more transactions are made on the same day, that interest only accumulates on the last principal balance that passes over into the next day.
- I made my first day be 0 in order for the example scenarios to work (since there needs to be 15 days from the first day to day 15 for the interest calculation to be correct). Thus the next period starts on day 30 which is also when interest is calculated.
- Since compound interest is not calculated I keep all accrued interest in a seperate variable from the balance.
- Any remaining balance at the end of a period is carried over to the next period in a variable so that the transactions of the period ending can be flushed to the transaction history.
- I stored transaction history in tuples rather than seperate objects because I wanted to keep the whole simulation in one class and there are only three fields for each transaction. It might have been more pythonic to do it with an object however. Might reduce overhead though.
