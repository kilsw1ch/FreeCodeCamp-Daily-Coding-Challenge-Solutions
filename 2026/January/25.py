def scale_image(size, scale):
    s=size.replace('x',' ')
    s=s.split()
    return f"{int(int(s[0])*scale)}x{int(int(s[1])*scale)}"