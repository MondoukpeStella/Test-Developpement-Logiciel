def are_anagrams(str1,str2):
    if sorted(str1.replace(" ","") == str2.replace(" ","")) :
        print("Ces deux mots sont des anagrammes")
    else :
        print("Ces deux mots ne sont pas des anagrammes")