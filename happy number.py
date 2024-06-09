def is_happy(n):
    seen=set()
    while n!=1 and n not in seen:
        seen.add(n)
        n=sum(int(digit)**2 for digit in str(n))
        return n==1
def find_happy_numbers(numbers):
    happy_numbers=[]
    for number in numbers:
        if is_happy(number):
            happy_numbers.append(number)
    return happy_numbers

numbers=[10,501,22,37,100,999,87,351]
happy_numbers=find_happy_numbers(numbers)
happy_count=len(happy_numbers)

print("happy numbers:",happy_numbers)
print("count of happy numbers",happy_count)
