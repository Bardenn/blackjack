class BlackjackPlayer():
    def __init__(self):
        self.hand = []
        self.dealerhand = []
        self.wins = 0
        self.losses = 0
        self.draws = 0

    def on_dealt_card(self, card):
        card.faceup = True
        self.hand.append(card)
        self.render_game()

    def on_dealer_dealt_card(self, card):
        self.dealerhand.append(card)
        self.render_game()

    def on_game_end(self, result):
        if result is None:
            self.draws += 1
        elif result is True:
            self.wins += 1
        else:
            self.losses += 1
        self.hand = []
        self.dealerhand = []
        self.render_game_end(result)

    def reveal_all_cards(self):
        for card in self.dealerhand:
            card.faceup = True
        self.render_game()

    def on_hit(self, result):
        raise NotImplementedError()

    def do_play(self):
        raise NotImplementedError()

    def render_game(self):
        raise NotImplementedError()

    def render_game_end(self):
        raise NotImplementedError()