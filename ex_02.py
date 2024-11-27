def are_anagrams(str1,str2):
    if type(str1)!=str or type(str2)!=str :
         raise ValueError("Les paramères doivent être des chaine de charactères")
    if sorted(str1.replace(" ","")) == sorted(str2.replace(" ","")) :
        print("Ces deux mots sont des anagrammes")
    else :
        print("Ces deux mots ne sont pas des anagrammes")
