def get_element_size(window_size, element_vw, element_vh):
    w=element_vw.replace("vw",'')
    h=element_vh.replace("vh",'')
    s=window_size.replace(" x ",' ')
    s=s.split()
    w=int(int(w)*int(s[0])/100)
    h=int(int(h)*int(s[1])/100)
    return f"{w} x {h}"