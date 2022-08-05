#!/usr/bin/env python3

import random
import os
import time

suites = ["Hearts","Diamonds","Clubs","Spades"]
numbers = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10","Jack","Queen","King"]

values = {
    "Ace": 11,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
}

deck = []
drawn = []
player_hand = []
dealer_hand = []


def init():
    print("\nWelcome!\n")
    build_new_deck()
    
    
def menu():
    inp = ""
    while inp.lower() != "q":
        clearscreen()
        print("\nCards.py\nMain Menu\n")
        inp = input(" (Q)uit\n\n (P)lay Blackjack\n\n (B)uild new deck\n (S)how cards\n (R)andom card\n\n > ")
        if inp.lower() == "b":
            build_new_deck()
        elif inp.lower() == "s":
            show_deck()
            time.sleep(2)
        elif inp.lower() == "r":
            print(random_card())
            time.sleep(1)
        elif inp.lower() == "p":
            play_blackjack()
            
            
def farewell():
    print("\nFarewell!\n")
    time.sleep(2)
    temp = os.system('clear')

    
def clearscreen():
    temp = os.system('clear')
    

def build_new_deck():
    global deck
    deck = []
    for suite in suites:
        for number in numbers:
            card = str(number+" of "+suite)
            deck.append(card)

            
def show_deck():
    print("\n")
    for card in deck:
        print(card)
    print("\n")
    print(str(len(deck))+" cards in the deck")
    
    
def random_card():
    #print("def random_card()")
    print("\n")
    card = random.choice(deck)
    return(card)


def draw_card():
    card = random_card()
    drawn.append(card)
    deck.remove(card)


def draw_card_player():
    card = random_card()
    player_hand.append(card)
    deck.remove(card)


def draw_card_dealer():
    card = random_card()
    dealer_hand.append(card)
    deck.remove(card)
    
    
def reset_deck():
    build_new_deck()
    drawn.clear()
    player_hand.clear()
    dealer_hand.clear()


def play_blackjack():
    #print("def play_blackjack()")
    reset_deck()
    draw_card_player()
    draw_card_player()
    player_done = False
    dealer_done = False
    value = 0
    dealer = 0
    
    while not player_done:
        clearscreen()
        value = 0
        value = hand_value("player")
        #for card in player_hand:
        #    value += card_value(card,value)
        print(player_hand)
        print("Total:"+str(value))
        if value == 21:
            print("You win!  What luck!")
            time.sleep(2)
            player_done = True
        elif value > 21:
            print("Oops!  You went over 21!")
            time.sleep(2)
            player_done = True
        else:
            inp = input("\n(H)it or (s)tay?\n > ")
            if inp.lower() == "h":
                draw_card_player()
            else:
                player_done = True
                
    draw_card_dealer()
    while not dealer_done:
        clearscreen()
        dealer = 0
        draw_card_dealer()
        dealer = hand_value("dealer")
        #for card in dealer_hand:
        #    dealer += card_value(card,dealer)
        print(dealer_hand)
        print("Total:"+str(dealer)+"\n")
        if dealer == 21:
            print("Dealer wins!  What luck!")
            dealer_done = True
        elif dealer > 21:
            print("Oops!  Dealer went over 21!")
            dealer_done = True
        else:
            if dealer >= 17:
                print("Dealer to stay at "+str(dealer))
                dealer_done = True
            else:
                print("Dealer to hit")
        time.sleep(1)
                
                
    clearscreen()
    print("\nPlayer got "+str(value))
    print(str(player_hand))
    print("\nDealer got "+str(dealer))
    print(str(dealer_hand))
    
    print("\n\n")
    if dealer == 21:
        print("BLACKJACK! Dealer wins!")
    elif value == 21:
        print("BLACKJACK! You win!!")
    elif dealer > 21 and value > 21:
        print("No one wins :(")
    elif ((dealer > value) and (dealer <= 21)) or (value > 21):
        print("Dealer wins!")
    elif dealer == value:
        print("Dealer and player split the pot.")
    else:
        print("You win!!")
    print("\n")
    time.sleep(2)
    inp = input("Play again? (y/n)\n > ")
    if inp.lower() == "y":
        play_blackjack()
    
        
        
def hand_value(who):
    total = 0
    if who == "player":
        for card in player_hand:
            total += card_value(card,total)
        return(total)
    elif who == "dealer":
        for card in dealer_hand:
            total += card_value(card,total)
        return(total)
            

    
def card_value(card,total):
    card_parts = card.split(" ")
    card_no = card_parts[0]
    if card_no.isdigit():
        value = int(card_no)
    elif card_no == "Ace":
        if total >= 11:
            value = 1
        else:
            value = 11
    else:
        value = 10
    return(value)
        
    
    
############
############

init()

menu()

farewell()
