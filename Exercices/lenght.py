def count_vowels(word):
    vowels = "aeiouAEIOU"
    return sum(1 for char in word if char in vowels)

def filter_by_vowel(word_list, N):
    return [word for word in word_list if count_vowels(word) >= N]

mots = ["apple", "banana", "cherry", "date", "grape", "kiwi", "lemon"]
n = 2
resultat = filter_by_vowel(mots, n)
print(f"Les mots avec au moins {n} voyelles sont : {resultat}")
