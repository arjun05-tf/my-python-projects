import random

playerIn = True
dealerIn = True

# deck of card / player dealer hand

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
user_hand = []
dealer_hand = []

# deal the cards

def deal_cards(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

# calculate the total of both user and dealer

def total(turn):
    score = 0
    face_card = ['J', 'K', 'Q']
    for card in turn:
        if card in face_card:
            score += 10
        elif card == 'A':
            if score + 11 > 21:
                score += 1
            else:
                score += 11
        else:
            score += card
    return score

# check for winner

def reveal_dealer_hand():
    if len(dealer_hand) == 2:
        return dealer_hand[0]

# game loops for asking user for hit and stand

for _ in range(2):
    deal_cards(dealer_hand)
    deal_cards(user_hand)

while playerIn or dealerIn:
    print(f"Dealer has {reveal_dealer_hand()} and X")
    print(f"You have {user_hand} for a total of {total(user_hand)}")
    if playerIn:
        action = int(input("1: Stay\n2: Hit\n"))
    
    if total(dealer_hand) > 16:
        dealerIn = False
    else:
        deal_cards(dealer_hand)

    if action == 1:
        playerIn = False
    else:
        deal_cards(user_hand)
    
    if total(user_hand) >= 21:
        break
    elif total(dealer_hand) >= 21:
        break


if total(user_hand) == 21:
    print(f"\n You have {user_hand} for a total of {total(user_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("BlackJack! You win")

elif total(dealer_hand) == 21:
    print(f"\n You have {user_hand} for a total of {total(user_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("BlackJack! Dealer wins")

elif total(user_hand) > 21:
    print(f"\n You have {user_hand} for a total of {total(user_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("You Bust! Dealer wins")
elif total(dealer_hand) > 21:
    print(f"\n You have {user_hand} for a total of {total(user_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("Dealer Bust! You win")
elif 21 - total(dealer_hand) < 21 - total(user_hand):
    print(f"\n You have {user_hand} for a total of {total(user_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("Dealer wins!")
elif 21 - total(dealer_hand) > 21 - total(user_hand):
    print(f"\n You have {user_hand} for a total of {total(user_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("You win!")