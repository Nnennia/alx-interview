# Pascal's Triangle
Pascal’s triangle, in algebra, a triangular arrangement of numbers that gives the coefficients in the expansion of any binomial expression, such as (x + y)n. It is named for the 17th-century French mathematician Blaise Pascal.
The rows of Pascal's triangle are conventionally enumerated starting with row n = 0 n=0 at the top (the 0th row). The entries in each row are numbered from the left beginning with k = 0 k=0 and are usually staggered relative to the numbers in the adjacent rows. The triangle may be constructed in the following manner: In row 0 (the topmost row), there is a unique nonzero entry 1. Each entry of each subsequent row is constructed by adding the number above and to the left with the number above and to the right, treating blank entries as 0. For example, the initial number of row 1 (or any other row) is 1 (the sum of 0 and 1), whereas the numbers 1 and 3 in row 3 are added to produce the number 4 in row 4.
## Formula
In Pascal's triangle, each number is the sum of the two numbers directly above it.

The entry in the n nth row and k kth column of Pascal's triangle is denoted ( n k ) {n \choose k}. For example, the unique nonzero entry in the topmost row is ( 0 0 ) = 1 {\displaystyle {0 \choose 0}=1}. With this notation, the construction of the previous paragraph may be written as follows:

    ( n k ) = ( n − 1 k − 1 ) + ( n − 1 k ) {n \choose k}={n-1 \choose k-1}+{n-1 \choose k},

for any non-negative integer n n and any integer 0 ≤ k ≤ n 0\leq k\leq n.[4] This recurrence for the binomial coefficients is known as Pascal's rule. 
### source: https://en.wikipedia.org/wiki/Pascal%27s_triangle