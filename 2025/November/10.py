def get_extension(filename):
    if '.' not in filename or filename[-1]=='.':
        return "none"
    r=""
    i=-1
    while filename[i]!='.':
        r+=filename[i]
        i-=1
    return r[::-1]