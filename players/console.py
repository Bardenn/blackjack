import cardprinter
import os
from players.generic import BlackjackPlayer
from os import system, name

def clear():
    """https://stackoverflow.com/a/61688844/12125728"""
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

HEADER = """
     _ _   _            _        _            _
    |  _ \| |          | |      | |          | |      
    | |_) | | __ _  ___| | __   | | __ _  ___| | __     
    |  _ <| |/ _` |/ __| |/ /   | |/ _` |/ __| |/ /      ,'`.   
    | |_) | | (_| | (__|   < |__| | (_| | (__|   <      (_,._)  
    |____/|_|\__,_|\___|_|\_\____/ \__,_|\___|_|\_\\      /\    
"""

class BlackjackConsolePlayer(BlackjackPlayer):
    def do_hit(self):
        self.render_game()
        return input("Hit / Stand? (h/s) ") == "h"

    def do_play(self):
        return input("Play again? (y/n)") == "y"

    def render_game_end(self, result):
        if result is None:
            print("Draw!")
        elif result is True:
            print("Won!")
        else:
            print("Lost!")

    def render_game(self):
        # clear the console
        clear()

        print(HEADER)
        # re-render 'board state'
        # render cards
        print("Your hand: ")
        print(cardprinter.ascii_version_of_cards(self.hand))
        print("Dealer: ")
        print(cardprinter.ascii_version_of_cards(self.dealerhand))