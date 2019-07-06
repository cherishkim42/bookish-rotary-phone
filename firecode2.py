'''Write a recursive method that returns the nth Fibonacci number. Assume n is less than 15.'''

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)