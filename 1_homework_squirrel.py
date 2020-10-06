
def factorial(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return n*factorial(n-1)

def squirrel (n):
    return int(str(factorial(n=n))[0])
