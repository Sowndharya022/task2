listA=[10,501,22,37,100,999,87,351]
print(listA)
list_prime=[]
for i in listA:
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        list_prime.append(i)

print("prime numbers",list_prime)