from players.generic import BlackjackPlayer
import tkinter as tk

class BlackjackGUIPlayer(BlackjackPlayer):
    def __init__(self, *args):
        super().__init__(*args)
        self.root = tk.Tk()
        self.app = tk.Frame(self.root)
        self.app.pack()
        self.create_widgets()

    def create_widgets(self):
        self.app.hi_there = tk.Button(self.app)
        self.app.hi_there["text"] = "Hello World\n(Click me)"
        self.app.hi_there["command"] = self.do_sth
        self.app.hi_there.pack(side="top")

        self.app.quit = tk.Button(self.app, text="QUIT", fg="red", command=self.root.destroy)
        self.app.quit.pack(side="bottom")

    def do_sth(self):
        print("Clicked!")

    def do_hit(self):
        pass

    def do_play(self):
        pass

    def render_game_end(self, result):
        pass

    def render_game(self):
        self.root.update()