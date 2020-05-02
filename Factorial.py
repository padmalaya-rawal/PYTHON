#to calculate the factorial of the number

num = int(input("Enter the number: "))
fact = 1
temp =num
for rep in range(1, num+1):
    fact =fact * temp
    temp -=1
print(f"Factorial of {num} is {fact}")