for n in range(0, 1001):
   if (n == 1 or (n > 100 and n % 100 == 1) or (n > 20 and n % 10 == 1)) and n != 11:
       print(n, 'программист')
   elif (n == 0) or (4 < n < 21) or (100 < n % 100 < 21) or (24 < n % 100 < 99):
       print(n, 'программистов')
   elif (1 < n < 5) or (n > 21 and 1 < n % 10 < 5):
       print(n, 'программиста')