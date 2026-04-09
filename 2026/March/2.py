def sum_letters(s):
    l=list("abcdefghijklmnopqrstuvwxyz")
    d={}
    d.update({l[i]:i+1 for i in range(26)})
    r=0
    s=s.lower()
    for i in s:
        if i.isalpha():
            r+=d[i]
    return r