def are_anagrams(str1, str2):
    s1=(str1.replace(" ","")).lower()
    s2=(str2.replace(" ","")).lower()
    for i in s1:
        if i not in s2:
            return False
    return True