def get_laptop_cost(laptops, budget):
    laptops=sorted(laptops,reverse=True)
    m=laptops[0]
    laptops.remove(m)
    for i in laptops:
        if i<=budget:
            return i
    return m if m<=budget else 0