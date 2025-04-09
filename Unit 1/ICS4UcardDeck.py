inputPath = "dataFileIN.txt"
outputPath = "dataFileOUT.txt"

file = open(inputPath, "r")
suits = file.readline().strip().split(',')
values = file.readline().strip().split(',')
file.close()

deck = [[f"{value}{suit}" for value in values] for suit in suits]

def print_deck(deck):
    for row in deck:
        print(" ".join(row))

def remove_card(deck, card):
    for i in range(len(deck)):
        for j in range(len(deck[i])):
            if deck[i][j] == card:
                deck[i][j] = "--"
                return True
    return False

def save_deck_to_file(deck, outputPath):
    with open(outputPath, "w") as file:
        for row in deck:
            file.write(" ".join(row) + "\n")

print("Initial Deck:")
print_deck(deck)


while True:
    card_to_remove = input("Enter a card to remove (or type 'exit' to quit): ").strip()
    

    if card_to_remove.lower() == 'exit':
        break

    if remove_card(deck, card_to_remove):
        print("Card removed!")
    else:
        print("Card not found in deck.")
    

    print_deck(deck)

save_deck_to_file(deck, outputPath)
print("Deck saved to output file.")
