def jbelmu(text):
    w=text.split()
    jw=""
    r=""
    for i in w:
        if len(i)>1:
            for j in sorted(i[1:-1]):
                jw+=j
            r+=i[0]
            r+=jw
            r+=f"{i[-1]} "
            jw=""
        else:
            r+=f"i "
    return r.strip()