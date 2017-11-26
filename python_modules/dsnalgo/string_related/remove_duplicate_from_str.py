"""


input : geeksforgeeks
output :geksfor


and also maintain the order of charcters
"""

def remove_duplicate1(input_str):
    occ_map_dict={}
    output=""
    for char in input_str:
        if char not in occ_map_dict:
            occ_map_dict[char] = True
            output = output + char
    return output




print remove_duplicate1("geeksforgeeks")
