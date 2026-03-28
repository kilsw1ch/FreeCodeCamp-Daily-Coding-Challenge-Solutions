def is_unnatural_prime(n):
    if n==1 or n==-1 or n==0:
        return False
    an=abs(n)
    for i in range(2,an):
        if an%i==0:
            return False
    return True