def compress_string(sentence):
    w=sentence.split()
    l=[]
    for i in w:
        if i not in l:
            l.append(i)
    print(l)
    r=""
    for i in w:
        c=sentence.count(i)
        if c>1 and i not in r:
            r+=f"{i}({c}) "
        elif i not in r:
            r+=i+" "
    return r.strip()