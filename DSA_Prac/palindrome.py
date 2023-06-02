def binary_search_recursive(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target < data[mid]:
            return binary_search_recursive(data, target, low, mid-1)
        else:
            return binary_search_recursive(data, target, mid+1, high)
data = [2,2,2,7,8,9]
target = 2
print(binary_search_recursive(data, target, 0, 5))
