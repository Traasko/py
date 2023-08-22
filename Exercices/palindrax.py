def est_palindrome(mot):
    mot_inverse = mot[::-1]
    return mot == mot_inverse

mot = input("Entrez un mot : ")

if est_palindrome(mot):
    print("C'est un palindrome.")
else:
    print("Ce n'est pas un palindrome.")
