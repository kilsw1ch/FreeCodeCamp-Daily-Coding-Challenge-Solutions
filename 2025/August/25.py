def to_camel_case(s):
    r=""
    l=[' ','-','_']
    i=0
    while i<len(s):
        if s[i] in l:
            j=s[i+1]
            if j not in l:
                r+=s[i+1].upper()
                i+=1
        else:
            r+=s[i].lower()
        i+=1
    return r