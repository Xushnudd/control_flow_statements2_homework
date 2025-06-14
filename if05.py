def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    a = n//10000
    b = (n//1000)%10
    d = (n//100)%10
    e = (n//10)%10
    f = n%10
    if a>=b and a>=d and a>=e and a>=f:
        return a
    elif b>=a and b>=d and b>=e and b>=f:
        return b
    elif d>=a and d>=b and d>=e and d>=f:
        return d
    elif e>=a and e>=b and e>=d and e>=f:
        return e
    else:
        return f
print(main(67485))