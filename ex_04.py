def find_missing_number(liste):
    n = len(liste) + 1  
    sum_with_missing = (min(liste) + max(liste)) * n // 2 
    actual_sum = sum(liste)

    return sum_with_missing - actual_sum
