def generate_signature(name, title, company):
    n=name[0]
    if n.upper()<'I':
        n=">>"
    elif n.upper()<'R':
        n="--"
    elif n.upper()<'Z':
        n="::"
    return f"{n}{name}, {title} at {company}"