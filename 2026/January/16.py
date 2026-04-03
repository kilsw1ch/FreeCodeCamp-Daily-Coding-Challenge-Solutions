import math
def is_integer_hypotenuse(a, b):
    h=math.sqrt(a*a+b*b)
    print(h)
    s=str(h)
    if s[-1]=='0':
        if s[-2]=='.':
            return True
    return False