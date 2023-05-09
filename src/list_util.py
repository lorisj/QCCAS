

def swap_list_positions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list



def dict_to_vector(dictionary):
    """
    Converts a dictionary of the form {key: value} into a vector.

    Parameters:
        - dictionary (dict): A dictionary with keys as elements and values as counts.

    Returns:
        - list: A list representing a vector with key repeated value number of times.
    """
    vector = []
    for key, value in dictionary.items():
        vector.extend([key] * value)
    return vector


# Brings the value at index_in to the front, does not change anything else
def bring_to_front(list, index_in):
    list.insert(0, list.pop(index_in))
    return list



def int_to_binary_list(n):
    # Convert the integer to a binary string and remove the '0b' prefix.
    binary_str = bin(n)[2:]
    
    # Convert each character in the binary string to an integer and store in a list.
    binary_list = [int(digit) for digit in binary_str]
    
    return binary_list

def permutation_digit_swap_helper(block_permutation, block_digits,x):
    """
    Permutes the binary digits of an input integer x according to a specified
    permutation of the blocks of digits.

    Args:
    - block_digits: a list of integers indicating the number of binary digits
      in each block of the input integer x.
    - block_permutation: a list of integers representing a permutation of the
      blocks of the input integer x.
    - x: an integer between 0 and 2**sum(block_digits)-1 to be permuted.

    Returns:
    - permuted_x: an integer with the same number of binary digits as x, but
      with the blocks permuted according to block_permutation.

    Example usage:
    block_digits = [3, 2, 2]
    block_permutation = [2, 1, 0]
    x = 42  # (010 10 10 in binary)
    permuted_x = block_permutation_swap(block_digits, block_permutation, x)
    print(permuted_x) # Output: 82, which is (10 10 010 in binary)
    """
    x = int_to_binary_list(x)
    total_digits = sum(block_digits)
    assert not(len(x) > total_digits), "input to permutation_digit_swap_helper is larger than block_digits allows"
    while len(x) < total_digits # fill in 0s in the front to get to total_digits number of bits 
        x.insert(0,0)
        

 
def permutation_digit_swap(block_permutation, block_digits):
    """
    Permutes the binary digits of an input integer x according to a specified
    permutation of the blocks of digits.

    Args:
    - block_digits: a list of integers indicating the number of binary digits
      in each block of the input integer x.
    - block_permutation: a list of integers representing a permutation of the
      blocks of the input integer x.
    - x: an integer between 0 and 2**sum(block_digits)-1 to be permuted.

    Returns:
    - permuted_x: an integer with the same number of binary digits as x, but
      with the blocks permuted according to block_permutation.

    Example usage:
    block_digits = [3, 2, 2]
    block_permutation = [2, 1, 0]
    x = 42  # (010 10 10 in binary)
    permuted_x = block_permutation_swap(block_digits, block_permutation, x)
    print(permuted_x) # Output: 82, which is (10 10 010 in binary)
    """


# def test():
#     list = [0,1,2,3,4,5]
#     bring_to_front(list, 4)
#     print(list)


# test()