def is_sorted(arr):
    s=sorted(arr)
    if arr==s:
        return "Ascending"
    elif arr==s[::-1]:
        return "Descending"
    else:
        return "Not sorted"