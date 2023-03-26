number = int(input())
x = 0
x += 10000 * (number % 10)
x += 1000 * (number//10 % 10)
x += 100 * (number//100 % 10)
x += 10 * (number//1000 % 10)
x += (number//10000 % 10)
print(x)
