def is_valid_hex(s):
    if s[0]!='#':
        return False
    s=s.replace('#','')
    l=len(s)
    if l!=3 and l!=6:
        return False
    c=list("abcdef")
    for i in s:
        if not i.isdigit():
            if i.lower() not in c:
                return False
    return True