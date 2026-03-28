def get_captured_value(pieces):
    if 'K' not in pieces:
        return "Checkmate"
    dv={'P':1,'R':5,'N':3,'B':3,'Q':9,'K':1}
    dq={'P':8,'R':2,'N':2,'B':2,'Q':1,'K':1}
    s=0
    for i in pieces:
        dq[i]-=1
    for k,v in dq.items():
        s+=v*dv[k]
    return s

def convert_words(s):
    ws=s.split()
    r=""
    for w in ws:
        r+=str(len(w))+" "
    return r

def to_snake(camel):
    r=""
    for i in camel:
        if i.islower():
            r+=i
        else:
            r+="_"
            r+=i.lower()
    return r

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

def are_anagrams(str1, str2):
    s1=(str1.replace(" ","")).lower()
    s2=(str2.replace(" ","")).lower()
    for i in s1:
        if i not in s2:
            return False
    return True

def is_unnatural_prime(n):
    if n==1 or n==-1 or n==0:
        return False
    for i in range(2,abs(n)):
        if abs(n)%i==0:
            return False
    return True

def battle(my_army, opposing_army):

    if len(my_army)>len(opposing_army):
        return "Opponent retreated"

    elif len(my_army)<len(opposing_army):
        return "We retreated"
        
    d = {i: i for i in range(10)}

    letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    d.update({letters[i]: i+1 for i in range(52)})

    wa=0
    wb=0

    for i, j in zip(my_army,opposing_army):

        if not i.isalnum():
            if j.isalnum():
                if j!='0':
                    wb+=1

        elif not j.isalnum():
            if i.isalnum():
                if i!='0':
                    wa+=1

        elif d[i]>d[j]:
            wa+=1

        elif d[i]<d[j]:
            wb+=1
            
    if wa>wb:
        return "We won"

    elif wb>wa:
        return "We lost"

    else:
        return "It was a tie"