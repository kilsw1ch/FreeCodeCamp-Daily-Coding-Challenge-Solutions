def space_jam(s):
    r=""
    c=0
    w=s.replace(" ","")
    print(w)
    for i in w:
        r+=i.upper()
        c+=1
        if c!=len(w):
            r+="  "
    return r