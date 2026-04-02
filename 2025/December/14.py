def title_case(title):
    w=title.split()
    r=""
    for i in w:
        r+=f"{i[0].upper()}{i[1:].lower()} "
    return r.strip()