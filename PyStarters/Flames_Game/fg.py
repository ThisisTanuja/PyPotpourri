# function to remove common characters with their respective occurrences
def remove_same_char(l1, l2):
    i = 0
    while i < len(l1):
        j = 0
        while j < len(l2):

            # if common character found, then remove that character from both the lists
            if l1[i] == l2[j]:
                l1.pop(i)
                l2.pop(j)
                i -= 1
            else:
                j += 1
        i += 1

    # return count of remaining letters
    return len(l1 + l2) 


if __name__ == "__main__":
    
    # taking two inputs
    name1 = input("Player 1 name: ").lower().replace(" ", "")
    name2 = input("Player 2 name: ").lower().replace(" ", "")

    # converting to lists
    name1_list = list(name1)
    name2_list = list(name2)

    # calling method
    remaining_count = remove_same_char(name1_list, name2_list)
    
    # list of flames acronym
    result_list = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

    # looping until only one item is left in the result list
    while len(result_list) > 1:

        # storing the index value from where we need to perform slicing
        split_at = remaining_count % len(result_list) - 1

        # anti-clockwise circular fashion counting
        if split_at >= 0:
            right = result_list[split_at + 1 : ]
            left = result_list[ : split_at]
            #list concatenation
            result_list = right + left
        else:
            result_list = result_list[ : len(result_list) - 1]
      
    print("Relationship Status: ", result_list[0])
