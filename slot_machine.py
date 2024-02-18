import random

MAX_LINES = 3   # maximum number of lines to bet
MIN_BET = 1     # min amount bet
MAX_BET = 100   # max amount bet
ROWS = 3        # Number of rows (lines) in slot
COLS = 3        # Number of cols in slot

# All symbols and number of duplication/recurrence
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

# Value for each symbol
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

# Check and calculate the winnings, check if the same symbol appears 3 times
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    # for every row in the rows (lines bet)
    for line in range(lines):
        symbol = columns[0][line]
        ###print(f"Vérifions si le symbole {symbol} apparait 3 fois...")
        # for column in the columns
        for i, column in enumerate(columns):
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                ###print("Non, pas de bol.")
                break
            elif i == 2:
                print(f"Le symbole {symbol} apparait 3 fois à la ligne {line + 1} !!!")
                winnings += values[symbol] * bet
                winnings_lines.append(line + 1)
    if winnings == 0:
        print("Pas de bol...")
    print(f"Vous gagnez {winnings} €")
    print("Ligne(s) gagnante(s) :", *winnings_lines)
    return winnings

# Generate the slot machine
def get_slot_machine_spin(rows, cols, symbols):
    # create a copy of symbol list
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    ###print("Liste qui servira au choix (au hasard) des symboles : ", *all_symbols)
    columns = []
    for _ in range(cols):
        column = []
        # Create a copy of symbols list (for manipulating/removing symbols)
        current_symbols = all_symbols[:]
        for _ in range(rows):
            # pick a random symbol from symbols list
            value = random.choice(current_symbols)
            # Delete symbol from list
            current_symbols.remove(value)
            # Add symbol in column
            column.append(value)
        # Add column in columns list
        columns.append(column)
    ###print(f"Voici les {cols} colonnes de la machine à sous : ", columns)
    return columns

# Print slot machine in grid
def print_slot_machine(columns):
    print("La machine est lancée... voici le résultat :")
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

# Get initial deposit (capital)
def deposit():
    while True:
        amount = input("Quel est votre capital de départ (en €) ? ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Erreur : veuillez entrer un montant supérieur à 0.")
        else:
            print("Saisie incorrecte. Veuillez saisir un nombre.")
    return amount

# Get number of lines to bet on (1, 2 or 3)
def get_number_of_lines():
    while True:
        lines = input(f"Sur combien de lignes voulez-vous miser (entre 1 et {MAX_LINES}) ? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Erreur : entrer un nombre entre entre 1 et {MAX_LINES}.")
        else:
            print("Saisie incorrecte. Veuillez saisir un nombre.")
    return lines

# Get amount bet
def get_bet():
    while True:
        amount = input(f"Combien voulez-vous miser sur chaque ligne (entre {MIN_BET} € et {MAX_BET} €) ? ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Erreur : veuillez entrer un montant entre {MIN_BET} et {MAX_BET}.")
        else:
            print("Saisie incorrecte. Veuillez saisir un nombre.")
    return amount

# Run the slot machine
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        # Check if deposit is sufficient (compared to amount bet)
        if total_bet < balance:
            break
        else:
            print(f"Votre capital ({balance} €) est insuffisant pour le total misé ({total_bet} €).")
    print(f"Vous avez misé {bet} € sur {lines} lignes, ce qui fait {total_bet} € misé au total.")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings = check_winnings(slots, lines, bet, symbol_value)
    return winnings - total_bet

# Main function
def main():
    print('Bienvenue à la machine à sous !')
    balance = deposit()
    while True:
        print(f"Capital actuel : {balance} €")
        user_input = input("Appuyer Entrer pour jouer (ou 'q' puis Entrer pour quitter) -> ")
        if user_input == "q":
            break
        balance += spin(balance)
    print(f"Vous partez avec {balance} €.")
    print(f"Fin de partie.")

main()