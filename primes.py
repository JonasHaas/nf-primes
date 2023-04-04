numbers = range(2, 251)
count = 0
filename = 'result.txt'

with open(filename, 'w') as file:
    # Open the file in "write" mode to clear its contents
    pass

with open(filename, 'a') as file:
    for num in numbers:
        for i in range(2, num):
            if num % i == 0:
                # num is not prime
                break
        else:

            # num is prime, write it to the file
            count += 1
            file.write(str(num) + '\n')

print(str(count) + " prime numbers found.")