def to_snake(camel):
    r=""
    for i in camel:
        if i.islower():
            r+=i
        else:
            r+="_"
            r+=i.lower()
    return r