def is_valid_ipv4(ipv4):
    s=ipv4.replace('.',' ')
    s=s.split()
    if len(s)<4:
        return False
    for i in s:
        n=int(i)
        if n<0 or n>255:
            return False
        if len(i)>1 and i[0]=='0':
            return False
        for j in i:
            if not j.isdigit():
                return False
    return True