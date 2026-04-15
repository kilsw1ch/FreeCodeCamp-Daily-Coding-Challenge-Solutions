def sort_and_swap(arr):
    a=sorted(arr)
    for i in range(3,len(a)):
        if i%3==0:
            t=a[i]
            a[i]=a[i-1]
            a[i-1]=t
    return a