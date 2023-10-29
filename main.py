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

def main():
    balance = deposit()
    lines = get_number_of_lines()
    #  ici on voir si l'argent de pari est supérieur de son depôt
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You don't have enough money in your current account, which is it {deposit}!")
        
        else :
            break

    print(f"you are betting ${bet} on {lines} lines. Total bet is iqual to : ${total_bet}")
    # print(balance, lines)

main()


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
    
    columns = [[], [],[]]

    for _ in range(cols):
        column = []
        current_symbols = spin.copy()

        for _ in range(rows):

            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)

    return columns


