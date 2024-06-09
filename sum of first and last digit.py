num = int(input("enter a digit"))
first = num
last = num % 10
while first > 9:
    first = first // 10
print("first number",first)
print("last number",last)
sum=first+last
print("sum of first and last digit is",sum)
