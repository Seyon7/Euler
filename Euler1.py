number_sum = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        number_sum += i
print(number_sum)
