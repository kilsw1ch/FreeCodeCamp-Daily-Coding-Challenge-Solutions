def nth_fibonacci(n):
    a=0
    b=1
    f=[a,b]
    for i in range(1,n):
        c=a+b
        f.append(c)
        a=b
        b=c
    return f[n-1]