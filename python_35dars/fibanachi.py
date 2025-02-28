
def is_fibonacci(n):
    if n < 0:
        return False

    # Fibonacci sonlari to'g'risidagi matematik tekshiruv
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n
