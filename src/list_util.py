

def swap_list_positions(list : list, pos1 : int, pos2 : int)-> list:
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list



def dict_to_vector(dictionary : dict) -> list:
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
def bring_to_front(list : list, index_in : int) -> list:
    list.insert(0, list.pop(index_in))
    return list


def int_to_binary_list(n : int) -> list[int]:
    """
        Converts a binary number into a list of 0s and 1s representing it.

        Args:
        - int_value: some value.

        Returns:
        - binary_list: a list of 0s and 1s representing int_value.

        Example usage:
        print(binary_list_to_int(11)) # Output: [1, 0, 1, 1]
        """
    # Convert the integer to a binary string and remove the '0b' prefix.
    binary_str = bin(n)[2:]
    
    # Convert each character in the binary string to an integer and store in a list.
    binary_list = [int(digit) for digit in binary_str]
    
    return binary_list

def binary_list_to_int(binary_list : list[int]) -> int:
        """
        Converts a list of 0s and 1s representing a binary number to an integer.

        Args:
        - binary_list: a list of 0s and 1s representing a binary number.

        Returns:
        - int_value: the integer value corresponding to the binary number.

        Example usage:
        binary_list = [1, 0, 1, 1]
        int_value = binary_list_to_int(binary_list)
        print(int_value) # Output: 11
        """
        # Convert the binary list to a string representation and then convert to an integer.
        binary_string = ''.join([str(bit) for bit in binary_list])
        int_value = int(binary_string, 2)
        return int_value

def permutation_digit_swap_helper(block_permutation : list[int], block_digits : list[int], x : int) -> int:
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
    while len(x) < total_digits: # Fills in 0s in the front to get to total_digits number of bits 
        x.insert(0,0)


    # Generate blocks (ex. [010 10 10])
    blocks = []
    block_offset = 0
    for digits_to_append in block_digits:
        block_start = block_offset
        block_end = block_offset + digits_to_append
        blocks.append(x[block_offset:block_end])
        block_offset += digits_to_append

    # Rearrange result by permutation
    permuted_x = []
    for block_index in block_permutation:
        permuted_x.extend(blocks[block_index])

    return binary_list_to_int(permuted_x)




 
def permutation_digit_swap(block_permutation : list[int], block_digits : list[int])-> list:
    """
    Permutes the binary digits of an input integer x according to a specified
    permutation of the blocks of digits.

    Args: TODO: Fix
    - block_digits: a list of integers indicating the number of binary digits
      in each block of the input integer x.
    - block_permutation: a list of integers representing a permutation of the
      blocks of the input integer x.
      
    Returns:
    - permutation_out: the output of the enumeration with variable x with the same number of binary digits as x, but
      with the blocks permuted according to block_permutation.

    (See helper function for examples)
    """
    permutation_out = []
    total_digits = sum(block_digits)
    for x in range(2**total_digits):
        permutation_out.append(permutation_digit_swap_helper(block_permutation, block_digits, x))
    

    return permutation_out

