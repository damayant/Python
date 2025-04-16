def flatten(arr, depth):
    """
    Flatten a deeply nested array up to n levels.
    
    Parameters:
    arr (list): The nested array to flatten.
    depth (int): The number of levels to flatten.

    Returns:
    list: The flattened array.
    """
    if depth == 0:
        return arr
    result = []
    for item in arr:
        if isinstance(item, list):
            result.extend(flatten(item, depth - 1))
        else:
            result.append(item)
    return result

# Example usage 
nested_array = [1, [2, [3, [4]], 5], 6]
depth = 2
flattened_array = flatten(nested_array, depth)
print(flattened_array)  # Output: [1, 2, 3, [4], 5, 6]

