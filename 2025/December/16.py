def has_consonant_count(text, target):
    c=0
    l=["a", "e", "i", "o", "u"]
    for i in text:
        if i.isalpha() and i not in l:
            c+=1
    return True if c==target else False