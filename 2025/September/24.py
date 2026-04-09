import math
def is_perfect_square(n):
    if n<0:
        return False
    x=math.sqrt(n)
    print(x)
    s=str(x)
    if s[-1]=='0':
        if s[-2]=='.':
            return True
    return False