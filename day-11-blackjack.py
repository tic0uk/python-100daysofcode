# A game of blackjack (also known as 21)
# The solution I came up with wasn't the same as the teachers recommended way but it works so 
# I'll put it up here and learn for future lessons.

from replit import clear
from art import logo
import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
def play_game():
    user_response = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if user_response == "y":
        return True
    elif user_response == "n":
        return False
def new_player_card():
    player_card = cards[random.randint(0,len(cards)-1)]
    player_hand.append(player_card)
    return player_card
def new_computer_card():
    computer_card = cards[random.randint(0,len(cards)-1)]
    return computer_card
def check_player_score(score_player_hand):
    for i in range(0,len(player_hand)):
        if player_hand[i] == 11 and score_player_hand > 21:
            player_hand[i] = 1    
            score_player_hand = sum(player_hand)   
    print(f"    Your Cards: {player_hand}, current score: {score_player_hand}")
    print(f"    Computers first card: {computer_first_card}")
    if score_player_hand > 21:
        return False
    else:  
        return True
def check_computer_score(score_computer_hand):
    for i in range(0,len(computer_hand)):
        if computer_hand[i] == 11 and score_computer_hand > 21:
            computer_hand[i] = 1 
            score_computer_hand = sum(computer_hand)
    return score_computer_hand
def blackjack(score_player_hand,score_computer_hand):
    blackjack = False
    if score_player_hand == 21 or score_computer_hand == 21:
        return True
        print (blackjack)
    elif blackjack == False:
        return False
def deal_first_cards():
    computer_hand.append(computer_first_card)
    computer_hand.append(new_computer_card())
    new_player_card()
    new_player_card()
def offer_card():
    want_card = True
    while want_card:        
        deal_another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if deal_another_card == "y":
            print("dealing another card")
            new_player_card()
            want_card = check_player_score(sum(player_hand))
        elif deal_another_card == "n":
            want_card = False
            
def computer_turn():
    while sum(computer_hand) < 17:
            computer_hand.append(new_computer_card())
def who_won(player_final_score,computer_final_score):
    if blackjack_flag:
        if player_final_score > computer_final_score:
            return "Win with a Blackjack"
        elif computer_final_score > player_final_score:
            return "Lose, oppenent has Blackjack" 
    elif player_final_score > 21:
        return "You went over. You lose"
    elif computer_final_score > 21:
        return "Opponent went over. You win" 
    elif player_final_score > computer_final_score:
        return "You win"
    elif computer_final_score > player_final_score:
        return "You Lose"
    elif player_final_score == computer_final_score:
        return "It's a draw!"
new_game = play_game()
while new_game:
    clear()
    print(logo)
    computer_hand = []
    player_hand = []
    
    computer_first_card = new_computer_card()
    deal_first_cards()
    sum_player_hand = sum(player_hand)
    sum_computer_hand = sum(computer_hand)
    check_player_score(sum(player_hand))
    blackjack_flag = blackjack(sum_player_hand,sum_computer_hand)
    if blackjack_flag == False:
        offer_card()
        sum_player_hand = sum(player_hand)
        computer_turn()
        sum_computer_hand = check_computer_score(sum(computer_hand))
    print(f"    Your final hand: {player_hand}, final score: {sum_player_hand}")
    print(f"    Computer's final hand: {computer_hand}, final score: {sum_computer_hand}")
    print (who_won(sum_player_hand,sum_computer_hand))
        
    new_game = play_game()
