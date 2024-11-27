def sum_of_digits(n):
    if n < 0:
        raise ValueError("Le n doit être un entier positif.")
    return sum(int(digit) for digit in str(n))
