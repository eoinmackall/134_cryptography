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

def PollardRho_rec(m, s=None):
    """
    Input: an integer m, a seed s (if no seed specified, then a random seed is used)
    Output: Boolean-integer pair. If m is composite, returns (True, d)
    for a divisor d of m. Otherwise, returns (False,m).

    Works by implementing Pollard's rho algorithm using polynomial x^2+1 for
    recursively defined sequence. Uses recursion.
    """
    
    n=abs(m)

    if n==0 or n==1 or n==2:
        return (False, m)

    if s == None:
        s=random.randrange(1,n)
    
    #The function below satisfies rho_seq(i)=x_i
    rho_seq = lambda x : s if x==0 else (rho_seq(x-1)**2+1) % n

    #The main algorithm for finding a divisor of n
    for i in range(n):
        j=pr.EuclideanAlgorithm(rho_seq(2*i)-rho_seq(i),n)
        if j != 1:
            if j!=n:
                return (True, j)
         
    return (False, m)

def PollardRho(m, s=None):
    """
    Input: an integer m, a seed s (if no seed specified, then a random seed is used)
    Output: Boolean-integer pair. If m is composite, returns (True, d)
    for a divisor d of m. Otherwise, returns (False,m).

    Works by implementing Pollard's rho algorithm using polynomial x^2+1 for
    recursively defined sequence. Uses explicit computation of terms in sequence.
    """
    
    n=abs(m)

    if n==0 or n==1 or n==2:
        return (False, m)

    if s == None:
        s=random.randrange(1,n)
    
    #The function below is used to compute the ith value in
    #the Pollard-Rho sequence starting with seed s
    def rho_sequence(i,s):
        for j in range(1,i):
            s=(s**2+1) % n
        return s

    #This is the main implementation of Pollard's Rho algorithm
    #For each i, the following will compute x_{2i}-x_i.
    #To speed up future computations, the value of x_{2i} is stored
    #in a dictionary, and used in available.
    seen={}
    for i in range(1,n//2+1):

        q=rho_sequence(2*i,s)

        if q in seen.values(): #This indicates we have entered the loop of the rho
            
            seen[0]=q
            seen[2*i]=q
            
            #Used to determine length of loop period
            inverted_seen={u:v for v,u in seen.items()}
            l=inverted_seen[q]
            
            #The main algorithm for finding divisors, restricted to the loop
            for k in range(i,i+(2*i-l)):
                if k%2==0:
                    j=pr.EuclideanAlgorithm(seen[(2*k) % (2*i-l)]-seen[k], n)
                    if j != 1:
                        if j!= n:
                            return (True, j)
                else:
                    j=pr.EuclideanAlgorithm(seen[(2*k) % (2*i-l)]-rho_sequence(k,s), n)
                    if j != 1:
                        if j!= n:
                            return (True, j)
            break

        else: #If we haven't entered the loop, store q and proceed with algorithm
            seen[2*i]=q

        #The main algorithm for finding divisors
        if i%2==0:
            j=pr.EuclideanAlgorithm(q-seen[i], n)
            if j != 1:
                if j!= n:
                    return (True, j)
        else:
            j=pr.EuclideanAlgorithm(q-rho_sequence(i,s), n)
            if j != 1:
                if j!= n:
                    return (True, j)

    return (False, m)
