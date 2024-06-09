def first_non_repeating(list):
    occurences={}
    for iteam in list:
        if iteam in occurences:
            occurences[iteam]+=1
        else:
            occurences[iteam] = 1
    for iteam in list:
        if occurences[iteam] == 1:
            return iteam

    return None
numbers=[1,5,1,4,3,4,3]
print(first_non_repeating(numbers))

