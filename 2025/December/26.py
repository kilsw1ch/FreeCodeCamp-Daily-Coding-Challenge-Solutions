def sum_divisors(n):
    s=1
    for i in range(2,n+1):
        if n%i==0:
            s+=i
    return s