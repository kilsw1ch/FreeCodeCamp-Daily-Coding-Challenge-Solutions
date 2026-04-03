def complementary_dna(strand):
    r=""
    for i in strand:
        if i=='A':
            r+='T'
        elif i=='T':
            r+='A'
        elif i=='C':
            r+='G'
        elif i=='G':
            r+='C'
    return r