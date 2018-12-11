"""Tic Tac Toe game using Min-Max algorithm"""
from copy import deepcopy
from tkinter import Button, Tk
from tkinter.font import Font


class Board:
    """Tic Tac Toe Game Board"""

    def __init__(self, other=None):
        self.player = "X"
        self.opponent = "O"
        self.empty = "-"
        self.size = 3
        self.fields = {}
        for y in range(self.size):
            for x in range(self.size):
                self.fields[x, y] = self.empty
        # copy constructor
        if other:
            self.__dict__ = deepcopy(other.__dict__)

    def move(self, x, y):
        """Move one step"""
        board = Board(self)
        board.fields[x, y] = board.player
        (board.player, board.opponent) = (board.opponent, board.player)
        return board

    def __minimax(self, player):
        """Min Max algorithm"""
        if self.won():
            if player:
                return (-1, None)
            else:
                return (+1, None)
        elif self.tied():
            return (0, None)
        elif player:
            best = (-2, None)
            for x, y in self.fields:
                if self.fields[x, y] == self.empty:
                    value = self.move(x, y).__minimax(not player)[0]
                    if value > best[0]:
                        best = (value, (x, y))
            return best
        else:
            best = (+2, None)
            for x, y in self.fields:
                if self.fields[x, y] == self.empty:
                    value = self.move(x, y).__minimax(not player)[0]
                    if value < best[0]:
                        best = (value, (x, y))
            return best

    def best(self):
        """Return best move available"""
        return self.__minimax(True)[1]

    def tied(self):
        """Game Tie State"""
        for (x, y) in self.fields:
            if self.fields[x, y] == self.empty:
                return False
        return True

    def won(self):
        """Game Win State"""
        # horizontal
        for y in range(self.size):
            winning = []
            for x in range(self.size):
                if self.fields[x, y] == self.opponent:
                    winning.append((x, y))
            if len(winning) == self.size:
                return winning
        # vertical
        for x in range(self.size):
            winning = []
            for y in range(self.size):
                if self.fields[x, y] == self.opponent:
                    winning.append((x, y))
            if len(winning) == self.size:
                return winning
        # diagonal
        winning = []
        for y in range(self.size):
            x = y
            if self.fields[x, y] == self.opponent:
                winning.append((x, y))
        if len(winning) == self.size:
            return winning
        # other diagonal
        winning = []
        for y in range(self.size):
            x = self.size - 1 - y
            if self.fields[x, y] == self.opponent:
                winning.append((x, y))
        if len(winning) == self.size:
            return winning
        # default
        return None

    def __str__(self):
        string = ""
        for y in range(self.size):
            for x in range(self.size):
                string += self.fields[x, y]
            string += "\n"
        return string


class GUI:
    """TkInter GUI App"""

    def __init__(self):
        self.app = Tk()
        self.app.title("Tic-Tac-Toe")
        self.app.resizable(width=True, height=True)
        self.board = Board()
        self.font = Font(family="Ubuntu Mono", size=32)
        self.buttons = {}
        self.reset_btn = None
        for x, y in self.board.fields:
            handler = lambda x=x, y=y: self.move(x, y)  # noqa
            button = Button(self.app, command=handler, font=self.font, width=2, height=1)
            button.grid(row=y, column=x)
            self.buttons[x, y] = button
        handler = lambda: self.reset()  # noqa
        button = Button(self.app, text="Reset", command=handler)
        button.grid(row=self.board.size + 1, column=0, columnspan=self.board.size, sticky="WE")
        self.reset_btn = button
        self.update()

    def reset(self):
        self.board = Board()
        self.update()

    def move(self, x, y):
        self.app.config(cursor="watch")
        self.app.update()
        self.board = self.board.move(x, y)
        self.update()
        move = self.board.best()
        if move:
            self.board = self.board.move(*move)
            self.update()
        self.app.config(cursor="")

    def update(self):
        for (x, y) in self.board.fields:
            text = self.board.fields[x, y]
            self.buttons[x, y]["text"] = text
            self.buttons[x, y]["disabledforeground"] = "black"
            if text == self.board.empty:
                self.buttons[x, y]["state"] = "normal"
            else:
                self.buttons[x, y]["state"] = "disabled"
            self.reset_btn["text"] = "Reset"
        winning = self.board.won()
        if winning:
            winner = ""
            for x, y in winning:
                self.buttons[x, y]["disabledforeground"] = "red"
                winner = self.buttons[x, y]["text"]
            for x, y in self.buttons:
                self.buttons[x, y]["state"] = "disabled"
            self.reset_btn["text"] = f"'{winner}' won! Click to reset."
        for (x, y) in self.board.fields:
            self.buttons[x, y].update()

    def mainloop(self):
        self.app.mainloop()


if __name__ == "__main__":
    GUI().mainloop()
