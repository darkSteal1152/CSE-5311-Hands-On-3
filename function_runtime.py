def f(n):
    x = 1                      #
    for i in range(1, n):      # for loop runs through n iterations
        for j in range(1, n):  # for loop runs through n iterations
            x = x + 1          # constant time

    return x                   # returns summation of 1 for n times n times

# Runtime Summation can be written as
#             SUM(i = 1, n, SUM(j = 1, n, 1))
#                                                  SUM(j = 1, n, 1) = n
# Simplify to SUM(i = 1, n, n)
# Simplify to n * n = n^2
# Runtime = O(n^2)
