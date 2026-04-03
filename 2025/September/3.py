def is_pangram(s,l):
    s=s.lower()
    for i in s:
        if i.isalpha() and i not in l:
            return False
    for i in l:
        if i not in s:
            return False
    return True