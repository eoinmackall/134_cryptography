"""
Some integer factorization algorithms.
"""

import primality as pr
import random

def TrialDivision(m):
    """
    Input: an integer n
    Output: Boolean-integer pair. If m is composite, returns (True, d)
    for a divisor d of m. Otherwise, returns (False,m).

    Works by dividing n by 1, 2, 3,...
    """

    n=abs(m)

    if n==0 or n==1 or n==2:
        return (False, m)

    for i in range(2,int((n**(1/2))//1)+1):
        if n % i ==0:
            return (True,i)
    
    return (False, n)


def PollardRho2(m, s=None):
    """
    Input: an integer m, a seed s (if no seed specified, then a random seed is used)
    Output: Boolean-integer pair. If m is composite, returns (True, d)
    for a divisor d of m. Otherwise, returns (False,m).

    Works by implementing Pollard's rho algorithm using polynomial x^2+1 for
    recursively defined sequence. 
    """
    n=abs(m)

    if n<=2:
        return (False, m)

    if s == None:
        s=random.randrange(1,n)

    def f(x):
        return (x**2 + 1) % n

    x = s
    y = s
    d = 1
    i = 0

    while d == 1 and i<=1:
        x = f(x)
        y = f(f(y))
        d = pr.EuclideanAlgorithm(x - y, n)
        if d == n:
            d=1
        if x == y:
            i+=1

    if d != 1:
        return (True, d)
    else:
        return (False, m)