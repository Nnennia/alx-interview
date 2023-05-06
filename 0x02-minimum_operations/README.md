# Minimum Operators
In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

    Prototype: def minOperations(n)
    Returns an integer
    If n is impossible to achieve, return 0

The function first initializes three variables: pasted, count, and copied. It then checks if n is less than or equal to 1, in which case it returns 0. Otherwise, it enters a while loop that continues until pasted is greater than or equal to n. Within the loop, it checks three conditions: if copied is 0, it sets copied to pasted and adds pasted to itself, incrementing count by 2. If n - pasted is divisible by pasted, it sets copied to pasted and adds pasted to itself, incrementing count by 2. Otherwise, it simply adds copied to pasted and increments count by 1. The loop continues until pasted is greater than or equal to n, at which point it returns count.

