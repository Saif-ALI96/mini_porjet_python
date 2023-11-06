# 2 MADLIBS GENERATOR 
# 1. Write a program that generates two Mad Libs stories, each with different characters and plot twists. The user should be able to specify the
# 
# This program generates two madlibs stories. Each story has a different number of words to fill in the blanks, and each word is randomly selected

with open("story.txt","r") as f :
   my_story = f.read()

# print(my_story)
words = []

start_of_word = -1
target_start = "<"
target_end = ">"

start_of_word = -1  # Initialisation d'une variable pour suivre le début d'un mot
words = []  # Initialisation d'une liste pour stocker les mots extraits

# Parcours chaque caractère de la chaîne "my_story" en gardant leur position avec "enumerate"
for i, char in enumerate(my_story):
    # Vérifie si le caractère actuel est égal à "target_start"
    if char == target_start:
        # Si c'est le cas, enregistre la position de début du mot
        start_of_word = i

    # Vérifie si le caractère actuel est égal à "target_end" et si le début du mot a été enregistré
    if char == target_end and start_of_word != -1:
        # Si c'est le cas, extrait le mot de la chaîne et l'ajoute à la liste "words"
        word = my_story[start_of_word: i + 1]
        words.append(word)
        start_of_word = -1  # Réinitialise la position de début du mot

# Une fois la boucle terminée, affiche la liste "words" contenant les mots extraits

unique_words = set(words)  # Obtenez les mots uniques en utilisant un ensemble

# print(unique_words_list)

#  Ce dictionnaire sera utilisé pour stocker les réponses de l'utilisateur pour chaque mot unique dans l'histoire.
answers = {}

for unique_wo in unique_words:
    answer_of_user = input(f"Enter a word for {unique_wo} :")
    answers[unique_wo] = answer_of_user

# print(answers)
# mainentant il faut mettre tous les mots dans le dict answers dnas l'histoire 

for word_to_replace in unique_words:
    my_story = my_story.replace(word_to_replace , answers[word_to_replace])

print(my_story)
