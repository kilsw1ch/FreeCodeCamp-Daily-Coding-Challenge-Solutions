def find_target(arr, target):
    l=len(arr)
    for i in range(0,l-1):
        for j in range(1,l):
            if arr[i]+arr[j]==target:
                return [i,j]
    return "Target not found"