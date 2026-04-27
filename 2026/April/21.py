def get_odd_words(s):
    s=s.split()
    r=""
    for i in s:
        if len(i)%2!=0:
            r+=f"{i} "
    return r.strip()