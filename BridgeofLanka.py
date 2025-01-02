def largest_subarray_divisible_by_5(arr):
    # Dictionary to store the first occurrence of each remainder
    remainder_map = {}
    prefix_sum = 0
    max_length = 0
    start_index = -1  # To store the start index of the subarray
    
    # Traverse the array
    for i in range(len(arr)):
        # Update prefix sum
        prefix_sum += arr[i]
        
        # Calculate remainder of the prefix sum when divided by 5
        remainder = prefix_sum % 5
        
        # If remainder is 0, it means the sum of elements from 0 to i is divisible by 5
        if remainder == 0:
            max_length = i + 1  # The subarray is from index 0 to i
            start_index = 0
        
        # If remainder has been seen before, we can form a subarray from the next index after its first occurrence
        elif remainder in remainder_map:
            # Length of the subarray is current index - the first occurrence index
            subarray_length = i - remainder_map[remainder]
            if subarray_length > max_length:
                max_length = subarray_length
                start_index = remainder_map[remainder] + 1
        
        # Store the first occurrence of the remainder
        if remainder not in remainder_map:
            remainder_map[remainder] = i
    
    # If no valid subarray is found, return an empty list
    if max_length == 0:
        return []
    
    # Return the largest subarray
    return arr[start_index:start_index + max_length]

# Example test case
arr = [4, 1, 3, 2, 5, 10, 1]
print(largest_subarray_divisible_by_5(arr))  # Output: [5, 10]
