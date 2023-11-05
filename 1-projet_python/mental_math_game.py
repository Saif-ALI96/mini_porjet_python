# 3 TIMED MATH CHALLENGE

from random import randint , choice
import time
# Définition des opérateurs mathématiques disponibles
OPREATORS = ['+' , '-' , '*' ]

# Bornes minimale et maximale pour les opérandes
MIN_OPERAND = 3
MAX_OPERAND = 12

# Nombre total de problèmes à résoudre
TOTAL_PROBLEMS = 10

def generate_problem():

    # Génère aléatoirement un problème mathématique
    left = randint(MIN_OPERAND, MAX_OPERAND)
    right = randint(MIN_OPERAND, MAX_OPERAND)
    operator = choice(OPREATORS)

    # Crée l'expression mathématique sous forme de chaîne de caractères
    expr = str(left) + ' ' + operator + ' ' + str(right)

    # Évalue l'expression pour obtenir la réponse
    answer = eval(expr)
    # print(expr) 
    return expr , answer


# Initialisation du compteur d'erreurs
wrong = 0

# Attente de l'entrée de l'utilisateur pour démarrer le jeu
input("Press enter to start ! ")
print('-------------------')

# Mesure du temps au début du jeu
start_time = time.time()

# Boucle pour générer et résoudre les problèmes
for i in range(TOTAL_PROBLEMS):

    expr , answer = generate_problem()

    while True:

        # Invite l'utilisateur à entrer sa réponse
        user_answer = input(f'\n problem # {i+1} : {expr} = ')
        if user_answer == str(answer):
            break  # Sort de la boucle si la réponse est correcte

        wrong += 1  # Incrémente le compteur d'erreurs


# Mesure du temps à la fin du jeu
end_time = time.time()

total_time = round(end_time - start_time, 2)


# Affiche le score du joueur (nombre de problèmes correctement résolus)
if wrong != 0:
    print(f" \n You got {TOTAL_PROBLEMS - wrong} out of {TOTAL_PROBLEMS} correct")
else:
    print(f"You got all problems correct!")
    
print('-------------------')
print("Nice work!")
print(f"\nTime taken for the test is {total_time} seconds.")
