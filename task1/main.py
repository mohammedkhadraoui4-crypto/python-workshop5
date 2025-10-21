# Importe toutes les fonctions du module text_handler
from text_handler import (
    is_palindrome,
    count_vowels,
    reverse_text,
    remove_punctuation,
    capitalize_words,
    count_words,
    unique_words
)

# Chaîne de test
test_string = "Madam, I'm Adam. This is the Python Workshop 4 task."

print("--- Test du module text_handler.py ---")
print(f"Chaîne de test: \"{test_string}\"")
print("-" * 35)

# 1. Tester is_palindrome()
palindrome_test1 = "Radar"
palindrome_test2 = "Hello World"
print(f"1. is_palindrome('{palindrome_test1}'): {is_palindrome(palindrome_test1)}")
print(f"   is_palindrome('{palindrome_test2}'): {is_palindrome(palindrome_test2)}")
print("-" * 35)

# 2. Tester count_vowels()
print(f"2. count_vowels(): {count_vowels(test_string)}")
print("-" * 35)

# 3. Tester reverse_text()
reversed_text = reverse_text(test_string)
print(f"3. reverse_text(): \"{reversed_text}\"")
print("-" * 35)

# 4. Tester remove_punctuation()
no_punct_text = remove_punctuation(test_string)
print(f"4. remove_punctuation(): \"{no_punct_text}\"")
print("-" * 35)

# 5. Tester capitalize_words()
capitalized_text = capitalize_words(test_string)
print(f"5. capitalize_words(): \"{capitalized_text}\"")
print("-" * 35)

# 6. Tester count_words()
# Remarque : Les mots sont séparés par des espaces, la ponctuation est ignorée lors du comptage si elle est attachée aux mots (utilisant split())
word_count = count_words(no_punct_text) # Utilise la chaîne sans ponctuation pour un comptage plus précis des "mots"
print(f"6. count_words() (sur texte sans ponctuation): {word_count}")
print("-" * 35)

# 7. Tester unique_words()
unique_word_set = unique_words(test_string)
print(f"7. unique_words(): {unique_word_set}")
print(f"   Nombre de mots uniques: {len(unique_word_set)}")
print("-" * 35)
