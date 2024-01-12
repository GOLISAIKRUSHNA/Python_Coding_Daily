# def move_zeros_to_end(arr):
#     # Filter out non-zero elements and create a new array
#     non_zeros = [num for num in arr if num != 0]
    
#     # Count the number of zeros in the original array
#     num_zeros = len(arr) - len(non_zeros)
    
#     # Append zeros to the end of the new array
#     result = non_zeros + [0] * num_zeros
    
#     return result

# # Example usage:
# input_array = [0, 2, 0, 4, 3, 0, 5, 0]
# output_array = move_zeros_to_end(input_array)

# print("Input array:", input_array)
# print("Output array:", output_array)    



print("****** Move all zero's to end of array ****")











# def sai(input):
#     # print(input)
#     no_zero=[x for x in input if x!=0]

#     num_zero=len(input) -len(no_zero)
#     # print(num_zero)
#     print([1]*num_zero)


#     # val=
#     # print(val)



#     return None
#     # return no_zero+[0]*num_zero 
# input=list(map(int,input().split()))
# res=sai(input)
# print(res)






def sai(arr):
    non_zero=[x for x in arr if x!=0]
    zero=len(arr)-len(non_zero)
    print(non_zero + [0]*zero)

    return None 

input=list(map(int,input().split()))
res=sai(input)