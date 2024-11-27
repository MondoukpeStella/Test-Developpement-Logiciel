def longest_unique_substring(s):
    if type(s)!=str :
        raise ValueError("Le paramère s doit être une chaine de charactères")
    unique_substring = [char for char in s if s.count(char)==1]
    return len(unique_substring)
