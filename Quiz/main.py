
for n in range(1, 101):

    if n % 3==0 and n % 5==0:
        print(n,"Fizzbuzz")
    elif n % 3==0:
        print(n,"fizz")
    elif n % 5==0:
        print(n,"Buzz")
    else:
         print(n)