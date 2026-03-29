def is_valid_isbn10(s):
    v=0
    r=s.replace('-','')
    d=r[-1]
    if not d.isdigit():
        if d!='X':
            return False
    for i in range(0,len(r)-1):
        if not r[i].isdigit():
            return False
        v+=int(r[i])*(i+1)
    if d=='X':
        v+=100
    else:
        v+=int(d)*10
    return True if v%11==0 else False