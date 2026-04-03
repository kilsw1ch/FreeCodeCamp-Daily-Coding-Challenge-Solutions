def count(text, parameter):
    l=len(parameter)
    c=0
    for i in range(0,len(text)):
        if text[i:i+l]==parameter:
            c+=1
    return c