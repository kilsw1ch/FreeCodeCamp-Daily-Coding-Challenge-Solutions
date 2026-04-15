def get_last_letter(s):
    r=""
    for i in s:
        if i.isalpha():
            r+=i
    m=max(r)
    for i in r:
        if i.isupper() and i.lower()>=m:
            return i
    return m