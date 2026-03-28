def get_captured_value(pieces):
    if 'K' not in pieces:
        return "Checkmate"
    value={'P':1,'R':5,'N':3,'B':3,'Q':9,'K':1}
    quantity={'P':8,'R':2,'N':2,'B':2,'Q':1,'K':1}
    s=0
    for i in pieces:
        quantity[i]-=1
    for k,v in quantity.items():
        s+=v*value[k]
    return s