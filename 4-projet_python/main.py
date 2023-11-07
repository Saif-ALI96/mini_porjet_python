'''#  nous allons creer mini projet pour pratiquer python
#  on va construire  a text based slot mahcine'''
# pour generer la machine il faut importer la bibloteque random
import random


MAX_LINES = 3
MAX_BET = 100  # رهان
MIN_BET = 1
#  creer une faction qui demande l'utilisateur de entrer un nombre 
#  إيداع


def deposit():
    while True:
        amount = input("what would you like to depoist ? $ \n")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0 :
                break
            else:
                print("Amount must be greater than 0.")
        
        else:
            print("Please enter a number .")
        
    return amount 

#  creer une fonctions pour les lignes de la machine
def get_number_of_lines():
    while True:
        lines = input("Enter the nomber of lines to bet on (1-" + str(MAX_LINES) + ") ? ")
        if lines.isdigit():
                lines = int(lines)
                if 1 <= lines <= MAX_LINES:
                     break
                else:
                    print("Enter a valid number of lines")
        else:
            print("Please enter a nomber .")
                
    return lines
        
#  creer une fonctions pour les paris
#  رهان
def get_bet():
    while True:
        bet = input(f"How much do you want to bet? (${MIN_BET} -- ${MAX_BET} ? ) " )
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break

            else:
                print(f'Amount must be bettween ${MIN_BET} - ${MAX_BET} .')

        else :
            print('Please enter a number .')

    return bet

# maintenant la partie qui va faire fonctionner la machine
ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2 , 
    "B" : 4 ,
    "C" : 6 ,
    "D" : 8
}
def generate_slot_machine_spin(rows, cols,symbols):
#  rows : le nombre de rangées dans la machine
#  cols : le nombre de colonnes dans la machine
#  symbols : le dictionnaire contenant les symboles et leur nombre d'apparitions (par exemple des lettres ou des chiffres)
    spin = []
    for symbol , symbol_count in symbols.items():

        for _ in range(symbol_count):

            spin.append(symbol)
    
    columns = []

    for _ in range(cols):
        column = []
        current_symbols = spin.copy()

        for _ in range(rows):

            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)

    return columns


#  on voudrait voir ou printer ce qu'il y a dans columns pour 
#  pouvoir les tester apres 

def print_slot_machine(columns):
                
    for row in range(len(columns[0])):
        
        for i , column in enumerate(columns):
            if i != len(columns) - 1 :
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

#  nous devons savoir quel est leur meilleur, sur quoi ils parient
#  et combien d'argent ont-ils gagné en total ?
symbol_value = {
    "A" : 5 , 
    "B" : 4 ,
    "C" : 3 ,
    "D" : 2
}

def check_winnings(columns,lines,bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]

        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1 )

        
    return winnings, winnings_lines




#  ici c'est l'affiche de notre jeu 
def game(balance):

    lines = get_number_of_lines()

        #  ici on voir si l'argent de pari est supérieur de son depôt
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You don't have enough money in your current account, which is it {balance}!")
        else :
            break

    print(f"you are betting ${bet} on {lines} lines. Total bet is iqual to : ${total_bet}")
    # print(balance, lines)

    slots = generate_slot_machine_spin(ROWS, COLS ,symbol_count)

    print_slot_machine(slots)
    winnings, winnings_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"you won ${winnings}.")
    print(f"You won on lines :", *winnings_lines)

    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"current blance is ${balance}")

        spin = input("Press enter to play (q to quit).")

        if spin == "q":
            break

        balance += game(balance)

    print(f"You left with ${balance}")

main()

