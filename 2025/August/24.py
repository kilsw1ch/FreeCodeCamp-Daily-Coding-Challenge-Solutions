def battle(my_army, opposing_army):

    if len(my_army)>len(opposing_army):
        return "Opponent retreated"

    elif len(my_army)<len(opposing_army):
        return "We retreated"
        
    d = {i: i for i in range(10)}

    letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    d.update({letters[i]: i+1 for i in range(52)})

    wa=0
    wb=0

    for i, j in zip(my_army,opposing_army):

        if not i.isalnum():
            if j.isalnum():
                if j!='0':
                    wb+=1

        elif not j.isalnum():
            if i.isalnum():
                if i!='0':
                    wa+=1

        elif d[i]>d[j]:
            wa+=1

        elif d[i]<d[j]:
            wb+=1
            
    if wa>wb:
        return "We won"

    elif wb>wa:
        return "We lost"

    else:
        return "It was a tie"