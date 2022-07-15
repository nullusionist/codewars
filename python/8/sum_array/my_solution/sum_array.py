def sum_array(arr):
    if arr is None: return 0
    if len(arr) is 0 or len(arr) is 1 : return 0
    return (sum(arr) - (min(arr) + max(arr)))