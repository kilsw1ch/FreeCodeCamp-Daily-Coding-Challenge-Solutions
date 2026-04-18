def find_pawn_moves(position):
    c,r=position[0],position[1]
    return [f"{c}{int(r)+1}", f"{c}{int(r)+2}"] if r=='2' else [f"{c}{int(r)+1}"]