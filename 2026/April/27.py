def get_word_score(word):
    l=list("abcdefghijklmnopqrstuvwxyz")
    d={}
    d.update({l[i]:i+1 for i in range(26)})
    s=0
    word=word.lower()
    for i in word:
        s+=d[i]
    return s