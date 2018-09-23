import random
import unittest

# SI 507 Fall 2018
# Homework 2 - Code

##COMMENT YOUR CODE WITH: Benjamin Rego
# Section Day/Time: Wednesday 5:30 - 7pm
# People you worked with: Alone

######### DO NOT CHANGE PROVIDED CODE #########
### Scroll down for assignment instructions.
#########

class Card(object):
    suit_names =  ["Diamonds","Clubs","Hearts","Spades"]
    rank_levels = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    faces = {1:"Ace",11:"Jack",12:"Queen",13:"King"}

    def __init__(self, suit=0,rank=2):
        self.suit = self.suit_names[suit]
        if rank in self.faces: # self.rank handles printed representation
            self.rank = self.faces[rank]
        else:
            self.rank = rank
        self.rank_num = rank # To handle winning comparison

    def __str__(self):
        return "{} of {}".format(self.rank,self.suit)

class Deck(object):
    def __init__(self): # Don't need any input to create a deck of cards
        # This working depends on Card class existing above
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit,rank)
                self.cards.append(card) # appends in a sorted order

    def __str__(self):
        total = []
        for card in self.cards:
            total.append(card.__str__())
        # shows up in whatever order the cards are in
        return "\n".join(total) # returns a multi-line string listing each card

    def pop_card(self, i=-1):
        # removes and returns a card from the Deck
        # default is the last card in the Deck
        return self.cards.pop(i) # this card is no longer in the deck -- taken off

    def shuffle(self):
        random.shuffle(self.cards)

    def replace_card(self, card):
        card_strs = [] # forming an empty list
        for c in self.cards: # each card in self.cards (the initial list)
            card_strs.append(c.__str__()) # appends the string that represents that card to the empty list
        if card.__str__() not in card_strs: # if the string representing this card is not in the list already
            self.cards.append(card) # append it to the list

    def sort_cards(self):
        # Basically, remake the deck in a sorted way
        # This is assuming you cannot have more than the normal 52 cars in a deck
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit,rank)
                self.cards.append(card)

class Hand(object):
    def __init__(self,init_cards):
        if type(init_cards) == type([]):
            self.cards = init_cards

    def __str__(self):
        hand = []
        for card in self.cards:
            hand.append(card.__str__())
        # shows up in whatever order the cards are in
        return "\n".join(hand) # returns a multi-line string listing each card

    def add_card(self,card):
        if card.__str__() not in self.__str__():
            self.cards.append(card)
        return None

    def remove_card(self,card):
        for indv_card in self.cards:
            if card.__str__() == indv_card.__str__():
                self.cards.remove(indv_card)
                return indv_card
        return None

    def draw(self,deck):
        self.add_card(deck.pop_card())
        return None

    def remove_pairs(self):
        hand = []
        pair_dict = {}
        hand_dict = {}
        removed_cards = []
        for card in self.cards:
            hand.append(card.__str__())
            hand_dict[card.__str__()] = card
        for item in hand:
            item_list = item.split()
            if item_list[0] not in pair_dict.keys():
                pair_dict[item_list[0]] = 1
            else:
                pair_dict[item_list[0]] += 1
        for pair in pair_dict.items():
            if pair[1] >= 2:
                counter = 0
                for card_suit in hand_dict.keys():
                        if card_suit.split()[0] == pair[0]:
                            self.remove_card(hand_dict[card_suit])
                            removed_cards.append(card_suit)
                            counter += 1
                        if counter == 2:
                            return removed_cards
        return removed_cards




### Go Fish ###

players = input("Please list the names of the players separated by commas: ")
player_list = players.replace(' ', '').split(',')

hand_dictionary = {}
shuffled_deck = Deck()
shuffled_deck.shuffle()
popped_card = shuffled_deck.pop_card()

for player in player_list:
    player_hand = Hand([])
    for i in range(7):
        player_hand.draw(shuffled_deck)
    hand_dictionary[player] = player_hand
    print(player)
    print(player_hand)



# player whose turn it is, asks about a particular card. Alice: "Bob, do you have any threes?"
    #Alice must have a three to ask
    #Bob hands over the threes he has
    #if Bob has none, he says go fish, alice draws from the deck
    # if alice draws the card she needs, she reveals card and goes again
    #otherwise, next players turn
#
