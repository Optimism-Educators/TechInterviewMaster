def is_triplet(a, b, c):
    """
    Validate whether three integers form a Pythagorean triplet.

    A Pythagorean triplet satisfies the condition:
        a^2 + b^2 = c^2
    where c is the largest number.

    Parameters:
    a (int): First number
    b (int): Second number
    c (int): Third number

    Returns:
    bool: True if they form a triplet, else False
    """
    a, b, c = sorted([a, b, c])
    return a**2 + b**2 == c**2


# Example usage
if __name__ == "__main__":
    examples = [
        (3, 4, 5),
        (13, 5, 12),
        (1, 2, 3)
    ]

    for nums in examples:
        result = is_triplet(*nums)
        print(f"is_triplet{nums} ➞ {result}")
