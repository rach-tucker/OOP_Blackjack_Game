import random

class Hand:
    hand = []

    def __init__(self, dealer):
        self.hand = []
        self.dealer = dealer

    def addToHand(self, card):
        self.hand.append(card)

    def totalValue(self):
        value = 0
        for card in self.hand:
            if card in ['J','Q','K']:
                value += 10
            elif card != 'A':
                value += card
            elif card == 'A':
                if (value + 11) > 20:
                    value += 1
                else:
                    value += 11
        return value

    def is_blackjack(self):
        for card in self.hand:
            if self.totalValue() == 21 and len(self.hand) == 2:
                return True

    def is_bust(self):
        if self.totalValue() > 21:
            return True

    def show_hand(self):
        if self.dealer:
            return "Dealer's hand: " + str(self.hand[0]) + ", HIDDEN"
        else:    
            return "Here is the Player's hand: " + str(self.hand)

class Dealer:
    def __init__(self):
        self.hand = Hand(True)

class Player:
    def __init__(self):
        self.hand = Hand(False)

class Game:
    def __init__(self):
        self.player = Player()
        self.dealer = Dealer()
        self.turn = "Player"
        self.deck = self.set_deck()
        self.playing = False
    
    def set_deck(self):
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10,
            2, 3, 4, 5, 6, 7, 8, 9, 10,
            2, 3, 4, 5, 6, 7, 8, 9, 10,
            2, 3, 4, 5, 6, 7, 8, 9, 10,
            'A', 'J', 'K', 'Q',
            'A', 'J', 'K', 'Q',
            'A', 'J', 'K', 'Q',
            'A', 'J', 'K', 'Q']
        random.shuffle(deck)
        return deck
    
    def start_game(self):
        self.deck = self.set_deck()
        for card in range(2):
            self.player.hand.addToHand(self.deal_single_card())
            self.dealer.hand.addToHand(self.deal_single_card())
        self.turn = "Player"

    def compare_cards(self):
        if self.player.hand.totalValue() > self.dealer.hand.totalValue():
            print(f"You have a total of {self.player.hand.totalValue()} which is higher than the dealer's total of {self.dealer.hand.totalValue()}. Congratulations, you won!")
            self.playing = False

        if self.dealer.hand.totalValue() > self.player.hand.totalValue():
            print(f"You have a total of {self.player.hand.totalValue()} which is less than the dealer's total of {self.dealer.hand.totalValue()}. Dealer won!")
            self.playing = False

        if self.player.hand.totalValue() == self.dealer.hand.totalValue():
            print(f"You have a total of {self.player.hand.totalValue()} which is the same as the dealer's total of {self.dealer.hand.totalValue()}. It's a draw!")
            self.playing = False


    def deal_single_card(self):
        single_card = self.deck.pop()
        return single_card

    def hit_or_stand(self):
        x = input("Would you like to hit or stand? enter 'h' or 's'")
        if x == 'h':
            self.player.hand.addToHand(self.deal_single_card())
            self.dealer.hand.addToHand(self.deal_single_card())
        elif x =='s':
            self.compare_cards()

    def run(self):
        self.playing = True
        while self.playing:
            ask = input("Welcome to the table. To play Blackjack, enter 'play' or 'quit' to leave.")
            if ask == 'play':
                self.start_game()
                if self.dealer.hand.is_blackjack():
                    print("Dealer has BLACKJACK! You lost this round.")
                    break
                if self.player.hand.is_blackjack():
                    print("Player has BLACKJACK! Congratulations, you won!")
                    break
                while self.playing:
                    print(self.dealer.hand.show_hand())
                    print(self.player.hand.show_hand())
                    self.hit_or_stand()

                    if self.player.hand.is_bust():
                        print("Bust! You lost.")
                        print(self.player.hand.show_hand())
                        print(self.dealer.hand.show_hand())
                        break
                    if self.dealer.hand.is_bust():
                        print("Dealer Busts! You won!")
                        print(self.player.hand.show_hand())
                        print(self.dealer.hand.show_hand())
                        break
            elif ask == 'quit':
                print("Hope to see you soon!")
                break
            else:
                print("Invalid repsonse. Try again.")


blackjack = Game()

blackjack.run()