def squares_with_three(n):
    c=0
    for i in range(1,n):
        if '3' in str(i*i):
            c+=1
    return c