"""

⮞Assignment Problem: String is given as input that contains only lowercase letters, remove
duplicate letters so that every letter appears once In O(n) Time Complexity and O(1) Space
Complexity

"""


def Remove_Duplicates(array):
    ascii = [0] * 256
    
    res = []
    
    for char in array:
        if ascii[ord(char)] == 0: # If character is encountered for the first time
            ascii[ord(char)] = -1 
            res.append(char) # Add it to the list
    
    return ''.join(res)


array = "abbacaca"

print(Remove_Duplicates(array))