def pow2(n):
    if n==0:
        return 1
    return pow2(n-1) + pow2(n-1)

def pow2_mult(n):
    if n==0:
        return 1
    return 2*pow2_mult(n-1)

def pow2_normal(n):
    if n==1:
        return 2
    if n%2==0:
        p=pow2_normal(n/2)
        return p*p
    p=pow2_normal(n-1/2)
    return 2*p*p

def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)

def primo(n):
    if n<=1:
        return False
    for i in range(2,n-1):
        if n%1==0:
            return False
    return True
