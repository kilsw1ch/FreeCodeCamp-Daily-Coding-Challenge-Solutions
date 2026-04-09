def get_next_bingo_number(n):
    b=n[0]
    a=int(n.replace(b,''))
    if a<15:
        a+=1
    elif a==15:
        return "I16"
    elif a<30:
        a+=1
    elif a==30:
        return "N31"
    elif a<45:
        a+=1
    elif a==45:
        return "G46"
    elif a<60:
        a+=1
    elif a==60:
        return "O61"
    elif a<75:
        a+=1
    else:
        return "B1"
    return f"{b}{a}"