def count_characters(sentence):
    sentence=sentence.lower()
    sentence=sorted(sentence)
    c=""
    r=[]
    for i in sentence:
        if i.isalpha() and i not in c:
            r.append(f"{i} {sentence.count(i)}")
            c+=i
    return r