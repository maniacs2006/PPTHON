name = input("Enter your name: ")
num1 = int(input("Enter your first favorite number: "))
num2 = int(input("Enter your second favorite number: "))
num3 = int(input("Enter your third favorite number: "))
print(f"Hello,{name}! Let's explore your favorite numbers: ")
numbers = [num1,num2,num3]
for number in numbers:
    if number % 2 == 0:
        print(f"The number {number} is even.")
    else:
        print(f"The number {number} is odd.")
    print(f"The number {number} and its square: ({number}, {number ** 2})")
sum_of_num =sum(numbers)
print(f"Amazing! The sum of your favorite numbers is: {sum_of_num}")
prime = True
if sum_of_num > 1:
    for i in range(2,int(sum_of_num ** 0.5)+ 1):
        if sum_of_num % i == 0:
            prime = False
            break
else:
    prime = False

if prime:
    print(f"Wow, {sum_of_num} is a prime number!")
else:
    print(f"{sum_of_num} is not a prime number.")
