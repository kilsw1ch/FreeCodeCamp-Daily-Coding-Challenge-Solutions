def get_lowercase_words(s):
    r=""
    l=s.split()
    for i in l:
        b=0
        for j in i:
            if j.isupper():
                b=1
                break
        if b==0:
            r+=f" {i}"
    return r[1:]