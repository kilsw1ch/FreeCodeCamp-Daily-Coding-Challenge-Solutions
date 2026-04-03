import math
def goldilocks_zone(mass):
    l=pow(mass,3.5)
    s=math.sqrt(l)
    return [round(s*0.95,2),round(s*1.37,2)]