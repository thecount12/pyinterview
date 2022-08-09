"""
factorial testing
"""

def factorial(n):
    """
    ;parms n: int(n)
    """
    # love this line
    assert n>=0 and int(n) == n, "The number must be positive only!"
    print(n)
    # if n in [0,1]: # Wow! easier than two lines
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
try:
    num = -1
    print(factorial(num))
except Exception as err:
    print(f"value: {str(num)}, {err}")
# another
try:
    num = 2.5
    print(factorial(num))
except Exception as err2:
    print(f"value: {str(num)}, {err2}")


