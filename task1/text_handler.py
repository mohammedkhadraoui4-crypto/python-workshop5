import string

def is_palindrome(text):
    """
    Vérifie si la chaîne est un palindrome, ignorant la casse et les espaces.
    """
    # Convertir en minuscules et retirer les espaces
    processed_text = "".join(char.lower() for char in text if char.isalnum())
    # Comparer la chaîne traitée avec son inverse
    return processed_text == processed_text[::-1]

def count_vowels(text):
    """
    Compte et retourne le nombre de voyelles (a, e, i, o, u) dans la chaîne.
    """
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

def reverse_text(text):
    """
    Retourne la version inversée de la chaîne d'entrée.
    """
    return text[::-1]

def remove_punctuation(text):
    """
    Retourne la chaîne avec toute la ponctuation retirée.
    """
    # Utilise string.punctuation pour obtenir tous les caractères de ponctuation
    translator = str.maketrans("", "", string.punctuation)
    return text.translate(translator)

def capitalize_words(text):
    """
    Retourne la chaîne avec la première lettre de chaque mot en majuscule.
    """
    # Utilise la méthode title() des chaînes de caractères
    return text.title()

def count_words(text):
    """
    Retourne le nombre total de mots dans la chaîne.
    Un mot est défini par un élément séparé par un espace.
    """
    # Utilise split() pour diviser la chaîne en une liste de mots
    words = text.split()
    return len(words)

def unique_words(text):
    """
    Retourne un ensemble (set) de mots uniques trouvés dans le texte.
    Ignore la casse et la ponctuation pour l'unicité.
    """
    # 1. Retirer la ponctuation
    no_punct_text = remove_punctuation(text)
    
    # 2. Convertir en minuscules et diviser en mots
    words = no_punct_text.lower().split()
    
    # 3. Créer et retourner un ensemble de mots uniques
    return set(words)
