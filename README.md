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

###Instructions
1. Open a python shell in the credit directory with 'python'
2. Import the line of credit class with 'from credit import lineOfCredit'
3. Create a new instance with 'loc = lineOfCredit(apr, credit)' with the chosen values for apr and credit.

###Supported operations:
- 'loc.makeWithdrawl(100)' - Draws the chosen amount from the account.
- 'loc.makePayment(100)' - Pays the chosen amount into the account. Note that interest will be paid off before the balance.
- 'loc.progressDays(10)' - Progresses days by the chosen number. If the simulation reaches the end of a period, interest calculations are automatically calculated and the transactions of that period are pushed to the account history.
- 'loc.currentDay()' - Prints the current day of the simulation and the remaining days before the end of the period.
- 'loc.paymentDue()' - Prints the current payment due (balance and interest).

###Notes and assumptions