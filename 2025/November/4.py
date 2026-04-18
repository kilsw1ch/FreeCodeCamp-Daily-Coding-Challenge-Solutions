def image_search(images, term):
    term=term.lower()
    r=[]
    for i in images:
        if term in i.lower():
            r.append(i)
    return r