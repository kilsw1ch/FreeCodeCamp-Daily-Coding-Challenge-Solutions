def get_initials(name):
    s=name.split()
    r=""
    for i in s:
        r+=f"{i[0]}."
    return r