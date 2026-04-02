def capitalize_fibonacci(s):
    r=""
    f=[]
    l=len(s)
    a=0
    b=1
    c=0
    for i in range(1,l):
        f.append(c)
        c=a+b
        a=b
        b=c
    print(f)
    for i in range(0,l):
        if i in f and s[i].isalpha():
            r+=s[i].upper()
        else:
            r+=s[i].lower()
    return r