def duplicate_character_count(str1, str2):
    c=0
    for i in str2:
        if i in str1:
            c=c+1
    return c