def check_perfect_numbers(n):
    sum = 0
    for i in range(1, n):
        if (n % i) == 0:
            sum += i
    if sum == n:
        return True
    else:
        return False
num = input(int("Enter a positive integer: "))
if check_perfect_numbers(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")   
