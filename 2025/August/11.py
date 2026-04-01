def is_balanced(s):
    s=s.lower()
    l=len(s)
    m=int(l/2)
    if l%2!=0:
        m+=1
    a=s[:m]
    b=s[m:l]
    va=0
    vb=0
    v=list("aeiou")
    for i,j in zip(a,b):
        if i in v:
            va+=1
        if j in v:
            vb+=1
    return True if va==vb else False