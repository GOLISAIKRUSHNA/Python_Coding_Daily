def move_zeros_to_end(arr):
    # Filter out non-zero elements and create a new array
    non_zeros = [num for num in arr if num != 0]
    
    # Count the number of zeros in the original array
    num_zeros = len(arr) - len(non_zeros)
    
    # Append zeros to the end of the new array
    result = non_zeros + [0] * num_zeros
    
    return result

# Example usage:
input_array = [0, 2, 0, 4, 3, 0, 5, 0]
output_array = move_zeros_to_end(input_array)

print("Input array:", input_array)
print("Output array:", output_array)    
