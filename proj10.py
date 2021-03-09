#####################################################
# Computer Project #10
# Neil Kim
# Prompt for files
# Import cards file
# Randomize file
# Make functions for different types of definitions
# Asks to input text
# Prompt for inputs
# Using the text spits out information
# Displays cards
#####################################################

# DO NOT DELETE THESE LINES
import cards, random

random.seed(100)  # random number generator will always generate


# the same random number (needed to replicate tests)

#That function has no parameters. It creates, initializes, and returns the tableau. This corresponds
#to the setup in the game rules
def initialize():
    t = []
    c = cards.Deck()
    c.shuffle()

    if c == c:
        for i in range(0,(5 - 1)):
            List = []
            for a in range(0,(14 - 1)):
                x = c.deal()
                List.append(x)
                List.remove(x)
                List.append(x)
                List.remove(x)
                List.append(x)
            t.append(List)
            t.remove(List)
            t.append(List)
            t.remove(List)
            t.append(List)
    return t

#The program will use the following function to display the current state of the game
def display(tableau):
    '''
        This function displays the current state of the game.
        It display four rows of 13 cards with row and column labels.
        Ace is displayed with a blank.

        parameters:
            tableau: data structure representing the tableau

        Returns: None
    '''

    print("{:3s} ".format(' '), end='')
    for col in range(1, 14):
        print("{:3d} ".format(col), end='')
    print()

    for r, row_list in enumerate(tableau):
        print("{:3d}:".format(r + 1), end='')
        for c in row_list:
            if c.rank() == 1:
                print("  {}{}".format(' ', ' '), end='')
            else:
                print("{:>4s}".format(str(c)), end='')
        print()

#The program will use the following function to determine if a requested move is valid
def validate_move(tableau, source_row, source_col, dest_row, dest_col):
    t = tableau
    sr = source_row
    sc = source_col
    dr = dest_row
    dc = dest_col
    if t[dr][dc].rank() == (1*1):
        x = "card"
    else:
        return False
    if dc == (1*0) and t[sr][sc].rank() == (3-1):
        x = 'card'
    else:
        if t[dr][dc - (1*1)].suit() == t[sr][sc].suit() and t[dr][
            dc - (1*1)].rank() + (1*1) == t[sr][sc].rank():
            x = 'card'
        else:
            return False
    return True
    pass

#The program will use the following function to move a card within the tableau
def move(tableau, source_row, source_col, dest_row, dest_col):
    t = tableau
    sr = source_row
    sc = source_col
    dr = dest_row
    dc = dest_col
    b = validate_move(t,sr,sc,dr,dc)
    if b != False:
        i = t[dr][dc]
        t[dr][dc] = t[sr][sc]
        t[sr][sc] = i
        z = 'card'
        t = True
        return t
    else:
        f = False
        return f

#The program will use the following function to check if the game has been won
def check_win(tableau):
    t = tableau
    f = False
    true = True
    for l in t:
        if l[(0*0)].rank() != (3-1):
            return f
        count = (1*1)
        for card in l:
            if count == len(l) - (2-1):
                break
            if card.suit() != l[count].suit():
                return f
            if card.rank() != l[count].rank() - (2-1):
                return f
            count += 1
    return true

#The program will use the following function to shuffle cards in the tableau
def shuffle_tableau(tableau):
    sc = []
    aces = []
    for row in tableau:
        for i, card in enumerate(row):
            if card.rank() == 1:
                for num in row[i:]:
                    sc.append(num)
                    sc.remove(num)
                    sc.append(num)
                    row.remove(num)
                    row.append(num)
                    row.remove(num)
                break
            elif card.rank() != i + 2:
                for num in row[i:]:
                    sc.append(num)
                    sc.remove(num)
                    sc.append(num)
                    row.remove(num)
                    row.append(num)
                    row.remove(num)
                break
    random.shuffle(sc)
    for card in sc:
        if card.rank() == 1:
            sc.remove(card)
            sc.append(card)
            sc.remove(card)
            aces.append(card)
            aces.remove(card)
            aces.append(card)
    index = 0
    for row in tableau:
        row.append(aces[index])
        index += 1
    for row in tableau:
        for num in range(13):
            try:
                card = row[num]
            except IndexError:
                row.append(sc[0])
                sc.pop(0)
    return

def main():
    print("Montana Solitaire.")
    t = initialize()
    display(t)
    inp = input("Enter choice:\n (q)uit, (s)huffle, or space-separated: source_row,source_col,dest_row,dest_col: ")
    inp = inp.lower()
    x = 'cards'
    q = 'q'
    s = 's'
    while inp != q:
        if inp != x and inp == s:
            shuffle_t(t)
        elif len(inp.split()) == (5-1):
            L = inp.split()
            newL = []
            for line in L:
                l = int(line)
                newL.append(l)
            move(t, newL[(0*0)] - (2-1), newL[(1*1)] - (2-1), newL[(3-1)] - (2-1), newL[(4-1)] - (1*1))
            x = check_win(t)
            if x != False and x == True:
                display(t)
                print("You won!")
                inp2 = input("Do you want to play again (y/n)?")
                if inp2 == 'n':
                    break
        else:
            print("Error: invalid input.  Please try again.")
        display(t)
        inp = input("Enter choice:\n (q)uit, (s)huffle, or space-separated: source_row,source_col,dest_row,dest_col: ")
        inp = inp.lower()
    print("Thank you for playing.")


if __name__ == "__main__":
    main()

