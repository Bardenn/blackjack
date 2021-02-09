import random
import cardprinter
import os
from enum import Enum
from dataclasses import dataclass
from players.console import BlackjackConsolePlayer
# from players.gui import BlackjackGUIPlayer


class CardSuite(Enum):
    SPADES = '♠'
    DIAMONDS = '♦'
    CLUBS = '♥'
    HEARTS = '♣'

class CardRank(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

@dataclass
class Card:
    suite: CardSuite
    rank: CardRank
    value: int
    faceup: bool

class CardDeck():

    def __init__(self):
        self.cards = []
        for suite in list(CardSuite):
            for rank in list(CardRank):
                val = min(rank.value, 10)
                if rank == CardRank.ACE:
                    val = 11
                self.cards.append(Card(suite, rank, val, False))

    def draw_card(self):
        if len(self.cards) == 0:
            raise RuntimeError("The deck was empty! Buy $gme")

        chosen_card = random.choice(self.cards)
        self.cards.remove(chosen_card)
        return chosen_card

class BlackjackGame():

    def __init__(self, player):
        self.hand = []
        self.player = player
        self.deck = CardDeck()
        # 1. 1 card given to the player
        self.player.on_dealt_card(self.deck.draw_card())

        # 2. 1 card face up given to dealer
        card = self.deck.draw_card()
        card.faceup = True
        self.hand.append(card)
        self.player.on_dealer_dealt_card(card)

        # 3. 1 card face down given to the dealer
        card = self.deck.draw_card()
        self.hand.append(card)
        self.player.on_dealer_dealt_card(card)

        # 4. 1 card given to the player
        self.player.on_dealt_card(self.deck.draw_card())

    def is_blackjack(self, hand):
        return sum([card.value for card in hand]) == 21

    def is_bust(self, hand):
        return sum([card.value for card in hand]) > 21

    def check_hand_for_aces(self, hand):
        all_values = [card.value for card in hand]
        while sum(all_values) > 21 and 11 in all_values:
            first_11 = all_values.index(11)
            all_values[first_11] = 1
            hand[first_11].value = 1

    def play(self):
        """Returns True if the player won"""
        # check for blackjack, check for bust, check for player choice
        while not self.is_blackjack(self.player.hand) and not self.is_bust(self.player.hand):
            if self.player.do_hit():
                card = self.deck.draw_card()
                self.player.on_dealt_card(card)
                self.check_hand_for_aces(self.player.hand)
            else:
                break
        #blackjack, bust, or standing
        if self.is_blackjack(self.player.hand):
            return True
        if self.is_bust(self.player.hand):
            return False
        
        #7. dealer turns around his face down card
        self.player.reveal_all_cards()

        while sum([card.value for card in self.hand]) < 17:
            card = self.deck.draw_card()
            card.faceup = True
            self.hand.append(card)
            self.check_hand_for_aces(self.hand)
            self.player.on_dealer_dealt_card(card)

        if self.is_blackjack(self.hand):
            return False
        if self.is_bust(self.hand):
            return True

        dealer_sum = sum([card.value for card in self.hand])
        player_sum = sum([card.value for card in self.player.hand])

        if player_sum == dealer_sum:
            return None

        return player_sum > dealer_sum

def main():
    player = BlackjackConsolePlayer()
    play = True
    while play:
        seed = random.randint(1, 100000)
        random.seed(seed)
        game = BlackjackGame(player)
        won = game.play()
        player.on_game_end(won)
        print("Seed:", seed)
        print("W: {} / L: {} / D: {}".format(player.wins, player.losses, player.draws))
        play = player.do_play()


if __name__ == "__main__":
    main()