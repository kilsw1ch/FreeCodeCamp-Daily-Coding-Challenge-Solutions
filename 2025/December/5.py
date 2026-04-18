def difference(arr1, arr2):
    r=arr1+arr2
    for i in r:
        if i in arr1 and i in arr2:
            r.remove(i)
            r.remove(i)
    return r