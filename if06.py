def main(n):
    """
    Find the index of the largest digit of the five-digit number.
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
        return 5
    elif b>=a and b>=d and b>=e and b>=f:
        return 4
    elif d>=a and d>=b and d>=e and d>=f:
        return 3
    elif e>=a and e>=b and e>=d and e>=f:
        return 2
    else:
        return 1
print(main(12765))