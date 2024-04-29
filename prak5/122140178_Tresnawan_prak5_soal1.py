import tkinter as tk
from tkinter import messagebox

class Board(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("TIK TAK TU")
        self.geometry("300x300")
        self.current_player = "X"
        self.board_buttons = []
        self.initialize_board()

    def initialize_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self, text="", font=("Jersey 20", 20), width=6, height=3,
                                   command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i, column=j, sticky="nsew")
                row.append(button)
            self.board_buttons.append(row)

    def on_button_click(self, row, col):
        if self.board_buttons[row][col]["text"] == "":
            self.board_buttons[row][col]["text"] = self.current_player
            if self.check_winner(row, col):
                messagebox.showinfo("Alert!", f"Pemain {self.current_player} menang!")
                self.reset_board()
            elif self.check_board_full():
                messagebox.showinfo("Alert!", "Imbang!")
                self.reset_board()
            else:
                self.switch_player()

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, row, col):
        if (self.board_buttons[row][0]["text"] == self.board_buttons[row][1]["text"] == self.board_buttons[row][2]["text"] == self.current_player):
            return True
        if (self.board_buttons[0][col]["text"] == self.board_buttons[1][col]["text"] == self.board_buttons[2][col]["text"] == self.current_player):
            return True
        if (self.board_buttons[0][0]["text"] == self.board_buttons[1][1]["text"] == self.board_buttons[2][2]["text"] == self.current_player):
            return True
        if (self.board_buttons[0][2]["text"] == self.board_buttons[1][1]["text"] == self.board_buttons[2][0]["text"] == self.current_player):
            return True
        return False

    def check_board_full(self):
        for row in self.board_buttons:
            for button in row:
                if button["text"] == "":
                    return False
        return True

    def reset_board(self):
        for row in self.board_buttons:
            for button in row:
                button["text"] = ""
        self.current_player = "X"


if __name__ == "__main__":
    app = Board()
    app.mainloop()
