
Accomplish in a language of your choice:

Input: Given an array of integers

Output: In whatever representation you wish, output each integer in the array and all the other integers in the array that are
factors of the first integer.  

Example:

  Given an array of [10, 5, 2, 20], the output would be:

{10: [5, 2], 5: [], 2: [], 20: [10,5,2]}

Additional Questions: 

1. What if you were to cache the calculation, for example in the file system.  What would an example implementation
of the cache look like?  By cache I mean, given an array input, skip the calculation of the output if you have already
calculated the output at least once already.

2. What is the performance of your caching implementation?  Is there any way to make it more performant.

3. What if you wanted to reverse the functionality.  What if you wanted to output each integer and all the other integers in the 
array that is the first integer is a factor of I.E:

Given an array of [10, 5, 2, 20], the output would be:
{10: [20], 5: [10,20], 2: [10, 20], 20: []}

Would this change your caching algorithim?

With caching, the output should be the same except the calculations are not performed.