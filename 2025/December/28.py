def to_screaming_snake_case(variable_name):
    r=""
    for i in variable_name:
        if i.isupper():
            r+=f"_{i}"
        elif i=='_' or i=='-':
            r+='_'
        else:
            r+=i
    c=r[0]
    if c=='_':
        r=r[1:]
    return r.upper()