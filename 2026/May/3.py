def get_greeting(s):
    s=int(s.replace(':',''))
    if s>=500 and s<1200:
        return "Good morning"
    if s>=1200 and s<1800:
        return "Good afternoon"
    if s>=1800 and s<2200:
        return "Good evening"
    return "Good night"