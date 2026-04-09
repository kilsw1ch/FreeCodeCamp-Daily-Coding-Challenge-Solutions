def palindrome_locator(s):
    if s!=s[::-1]:
        return "none"
    l=len(s)
    m=int(l/2)
    if l%2!=0:
        return s[m]
    else:
        return f"{s[m-1]}{s[m]}"