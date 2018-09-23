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

#game initialize function


    # print(player)
    # print(player_hand)


#select start
def select_start(player_list):
    starting_position = random.randint(0,len(player_list)-1)
    print(player_list[starting_position],"will start.")
    return starting_position

def whose_turn(player):
    command_player = player_list[player]
    print(player_list[player],"'S TURN")
    print("Your Hand:")
    print(hand_dictionary[player_list[player]])
    card_rank = 0
    while card_rank not in range(1,14):
        card_rank = input('Please choose a card rank you would like to ask the other player if they have (between 1-13):')
        try:
            card_rank = int(card_rank)
        except:
            card_rank = input('Please choose a card rank you would like to ask the other player if they have (between 1-13):')
    player_asked = ''
    while player_asked not in player_list:
        player_asked = input('Please name the player you are asking:').upper()
    return (command_player,player_asked,card_rank)

def hand_check(inquiry):
    hand = []
    hand_types = []
    player_asking = inquiry[0]
    player_asked = inquiry[1]
    for card in hand_dictionary[player_asked].cards:
        hand.append(card.__str__())
    #print(player_asked)
    #print(hand)
    for indv_card in hand:
        card_type = indv_card.split()[0]
        if card_type == "Ace":
            card_type = 1
        elif card_type == "King":
            card_type = 13
        elif card_type == "Queen":
            card_type = 12
        elif card_type == "Jack":
            card_type = 11
        card_type = int(card_type)
        hand_types.append(card_type)
    #print(hand_types)
    #print(inquiry[0])
    #print(inquiry[1])
    if inquiry[2] in hand_types:


        #card swap between players
        for cards in hand_dictionary[player_asked].cards:
            if inquiry[2] == 1 and cards.__str__().split()[0] == "Ace":
                hand_dictionary[player_asking].add_card(cards)
                hand_dictionary[player_asked].remove_card(cards)
                print(player_asked,"handed an Ace to", player_asking)
                #print(hand_dictionary[player_asked])
                #print(hand_dictionary[player_asking])
            elif inquiry[2] == 11 and cards.__str__().split()[0] == "Jack":
                hand_dictionary[player_asking].add_card(cards)
                hand_dictionary[player_asked].remove_card(cards)
                print(player_asked,"handed a Jack to", player_asking)
                #print(hand_dictionary[player_asked])
                #print(hand_dictionary[player_asking])
            elif inquiry[2] == 12 and cards.__str__().split()[0] == "Queen":
                hand_dictionary[player_asking].add_card(cards)
                hand_dictionary[player_asked].remove_card(cards)
                print(player_asked,"handed a Queen to", player_asking)
                #print(hand_dictionary[player_asked])
                #print(hand_dictionary[player_asking])
            elif inquiry[2] == 13 and cards.__str__().split()[0] == "King":
                hand_dictionary[player_asking].add_card(cards)
                hand_dictionary[player_asked].remove_card(cards)
                print(player_asked,"handed an King to", player_asking)
                #print(hand_dictionary[player_asked])
                #print(hand_dictionary[player_asking])
            elif str(inquiry[2]) in cards.__str__():
                hand_dictionary[player_asking].add_card(cards)
                hand_dictionary[player_asked].remove_card(cards)
                print(player_asked,"handed a", str(inquiry[2]),"to", player_asking)
                #print(hand_dictionary[player_asked])
                #print(hand_dictionary[player_asking])
    else:
        print(player_asked,"doesn't have a", str(inquiry[2]),"- Go fish", player_asking)
        print(player_asking,'draws a card...')
        pop_a_card = shuffled_deck.pop_card()
        hand_dictionary[player_asking].add_card(pop_a_card)
        if pop_a_card.__str__().split()[0] == str(inquiry[2]):
            print(player_asking,"drew the card he/she asked for, they get to go again!")



def book_add(book):
    for player in hand_dictionary.keys():
        player_hand_quantity = {}
        for cards in hand_dictionary[player].cards:
            if cards.__str__().split()[0] not in player_hand_quantity:
                player_hand_quantity[cards.__str__().split()[0]] = 1
            else:
                player_hand_quantity[cards.__str__().split()[0]] += 1
        # print(player)
        # print(player_hand_quantity)


        # check to see if a player has a set of 4
        for types in player_hand_quantity.keys():
            if player_hand_quantity[types] >=4:
                # print("Before")
                # print(hand_dictionary[player])
                if player in book.keys():
                    book[player].append(types)
                else:
                    book[player] = [types]
                print(player,"has completed the set for",types)


                #now, remove the 4 cards from their hand
                for set_card in hand_dictionary[player].cards:
                    if set_card.__str__().split()[0] == types:
                        hand_dictionary[player].remove_card(set_card)
                    else:
                        continue
                # print("after")
                # print(hand_dictionary[player])
                print(book)
                return True


        #this should cause the person inquiring to draw a card and if it is the card they needed, they go again

#this can be activated after any hand check to drop the quad pairs



players = input("Please list the names of the players separated by commas: ")
player_list = players.replace(' ', '').upper().split(',')

hand_dictionary = {}
shuffled_deck = Deck()
shuffled_deck.shuffle()
popped_card = shuffled_deck.pop_card()

for player in player_list:
    player_hand = Hand([])
    for i in range(7):
        player_hand.draw(shuffled_deck)
    hand_dictionary[player] = player_hand

book = {}
# startgame = select_start(player_list)
# first_turn_result = whose_turn(startgame)
# first_inquiry = hand_check(first_turn_result,book)
while len(book.keys())<1:
    for player in range(len(player_list)):
        print('\n')
        players_turn = whose_turn(player)
        inquiry = hand_check(players_turn)
        add_to_book = book_add(book)

leader = ''
leader_score = 0
for person in book.keys():
    if len(book[person])>leader_score:
        leader_score = len(book[person])
        leader = person

print('*' *25)
print('*' *25)
print("The winner is", leader, "with", leader_score, 'points')
print('*' *25)
print('*' *25)

    #break




# player whose turn it is, asks about a particular card. Alice: "Bob, do you have any threes?"
    #Alice must have a three to ask
    #Bob hands over the threes he has
    #if Bob has none, he says go fish, alice draws from the deck
    # if alice draws the card she needs, she reveals card and goes again
    #otherwise, next players turn
#
