import customtkinter as ctk
import tkinter
import time
# Game class

class Game():
    def __init__(self):
        self.root = ctk.CTk()
        self.board = [["" for _ in range(3)] for _ in range(3)]  # Initialize empty board
        self.current_player = "X"  # player starts as x
        self.check_var = tkinter.StringVar(master=self.root, value="on")
        self.startGui()

    # checkbox func (to check if the player wants to play first)
    def checkbox(self):
        print("Checkbox toggled, current value:", self.check_var.get())
        if self.check_var.get() == "on":
            self.current_player = "X"
        else:
            self.current_player = "O"

    def initGui(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        self.root.title("Tic-Tac-Toe")

        # Title
        self.main_title = ctk.CTkLabel(master=self.root, font=("Helvetica", 20, "bold"), text="Welcome to Tic-Tac-Toe!") 
        self.main_title.place(relx=0.5, rely=0.1, anchor=ctk.CENTER)

        self.play_first = ctk.CTkLabel(master=self.root, font=("Helvetica", 15, "bold"), text="Do you want to play first?")
        self.play_first.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)
        
        self.checkbox = ctk.CTkCheckBox(master=self.root, text="Yes", variable=self.check_var, onvalue="on", offvalue="off", command=self.checkbox)
        self.checkbox.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        # Start button
        self.label_button = ctk.CTkLabel(master=self.root, font=("Helvetica", 15, "bold"), text="Try to beat the AI ( •̀ᴗ•́ )و ̑̑")
        self.label_button.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)

        self.start_button = ctk.CTkButton(master=self.root, font=("Helvetica", 11), text="Ready!", command=self.startGame)
        self.start_button.place(relx=0.5, rely=0.7, anchor=ctk.CENTER)

        self.root.mainloop()

    def startGui(self):
        print("Initializing GUI...")
        self.initGui()

    def startGame(self):
        print("Starting game...")
        self.label_button.place_forget()
        self.start_button.place_forget()
        self.main_title.configure(text="Tic-Tac-Toe (Player vs AI)")

        self.current_turn = ctk.CTkLabel(master=self.root, text=f"Player {self.current_player}'s Turn", font=("Helvetica", 15, "bold"))
        self.current_turn.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)

        self.buttons = []
        board_layout = ctk.CTkFrame(master=self.root, width=300, height=300)
        board_layout.place(relx=0.5, rely=0.3, anchor=ctk.N)

        for i in range(3):
            row = []
            for j in range(3):
                cell = ctk.CTkButton(
                    master=board_layout,
                    text="",
                    font=("Helvetica", 24),
                    width=70,
                    height=70,
                    command=lambda x=i, y=j: self.putMark(x, y)
                )
                cell.grid(row=i, column=j, padx=5, pady=5)
                row.append(cell)
            self.buttons.append(row)

        # If AI plays first
        if self.current_player == "O":
            self.aiMove()

    def checkWin(self, player):
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or all(self.board[j][i] == player for j in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def gameFinish(self, result_text):
        for row in self.buttons:
            for cell in row:
                cell.configure(state="disabled")
        self.current_turn.configure(text=result_text)

        self.finish_button = ctk.CTkButton(master=self.root, text="Retry?", font=("Helvetica", 20, "bold"), command=self.retryGame)
        self.finish_button.place(relx=0.5, rely=0.9, anchor=ctk.CENTER)

    def checkDraw(self):
        return all(all(cell != "" for cell in row) for row in self.board)

    def putMark(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].configure(text=self.current_player, state="disabled")

            if self.checkWin(self.current_player):
                if self.current_player == "O":
                    self.gameFinish("AI Wins!")
                else:
                    self.gameFinish(f"Player {self.current_player} Wins!")
            elif self.checkDraw():
                self.gameFinish("It's a Draw!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.current_turn.configure(text=f"Player {self.current_player}'s Turn")
                if self.current_player == "O":
                    self.current_turn.configure(text="AI is thinking... (•_•)")
                    self.root.update_idletasks()
                    time.sleep(1)
                    self.aiMove()


    def aiMove(self):
        _, move = self.minimax(self.board, True)
        if move:
            self.putMark(move[0], move[1])

    def minimax(self, board, is_ai_turn):
        if self.checkWin("O"):
            return 1, None
        if self.checkWin("X"):
            return -1, None
        if self.checkDraw():
            return 0, None

        best_score = float("-inf") if is_ai_turn else float("inf")
        best_move = None

        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = "O" if is_ai_turn else "X"
                    score, _ = self.minimax(board, not is_ai_turn)
                    board[i][j] = ""
                    if is_ai_turn:
                        if score > best_score:
                            best_score, best_move = score, (i, j)
                    else:
                        if score < best_score:
                            best_score, best_move = score, (i, j)

        return best_score, best_move

    def retryGame(self):
        self.root.destroy()
        self.__init__()

# Run the game
if __name__ == "__main__":
    Game()
