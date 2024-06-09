listA =[10,501,22,37,100,999,87,351]
print(listA)
list_odd=[]
list_even=[]
for number in listA:
    if (number%2==0):
        list_even.append(number)
    else:
        list_odd.append(number)
print("list of even numbers ",list_even)
print("list of odd numbers ",list_odd)
