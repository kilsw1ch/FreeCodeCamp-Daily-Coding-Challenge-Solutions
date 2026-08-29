def sort_numbers(s):
    s=s.replace(',',' ')
    l=s.split()
    r=[]
    for i in l:
        r.append(int(i))
print(sort_numbers("3,1,2"))