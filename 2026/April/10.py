def rook_attack(rook1, rook2):
    if rook1[0]==rook2[0] or rook1[1]==rook2[1]:
        return True
    return False