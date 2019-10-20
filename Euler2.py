def fib(n):
    print(n)
    if n == 1:
        return 0
    elif n == 2:
        return 1

    return fib(n-1) + fib(n-2)


def sum_of_numbers():
    total = 0
    n = 1
    while fib(n) < 4000000:
        if fib(n) % 2 == 0:
            print(fib(n))
            total = total + fib(n)
            print("Total = " + str(total))
        n = n + 1
    return total


print("Сумма четных чисел Фибоначчи, меньших 4000000 равна: " + str(sum_of_numbers()))
