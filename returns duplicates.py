def find_duplicates(list1,list2,list3):
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)

    common_elements = set1 & set2 & set3
    duplicates=list(common_elements)
    return duplicates
list1=[1,2,3,4]
list2=[3,4,5,6]
list3=[4,5,6,7]

duplicates = find_duplicates(list1,list2,list3)
print("Duplicates:",duplicates)
