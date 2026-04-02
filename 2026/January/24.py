def get_bingo_letter(n):
    if n>0 and n<16:
        return "B"
    if n>15 and n<31:
        return "I"
    if n>30 and n<46:
        return "N"
    if n>45 and n<61:
        return "G"
    if n>60:
        return "O"