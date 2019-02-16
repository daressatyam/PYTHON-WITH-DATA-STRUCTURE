from math import sqrt
def square(n):
    if(sqrt(n) % 1 == 0):
        return True
    else:
        return False
def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def primesquare(l):
    s=l[0]
    if(isprime(s)):
        for i in range(0,len(l),2):
            if(isprime(l[i])==False):
                return False
        for i in range(1,len(l),2):
            if(square(l[i])==False):
                return False
        return True
    elif(square(s)):
        for i in range(0,len(l),2):
            if(square(l[i])==False):
                return False
        for i in range(1,len(l),2):
            if(isprime(l[i])==False):
                return False
        return True
    else:
        return False