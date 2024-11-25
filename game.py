'''
Klenn Jakek Borja
2022-03697
EF-5L
Exer 10 - Designing an AI Agent for a Tic-Tac-Toe Game (Last Exer)
'''

import customtkinter as ctk
# Game class
class Game():
    def __init__(self):
        self.root = ctk.CTk()
        self.startGui()
        pass

    def initGui(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.root.geometry("300x300")
        self.root.resizable(False, False)
        self.root.title("Tic-Tac-Toe")
        # title
        main_title = ctk.CTkLabel(master = self.root, font= ("Helvetica", 20, "bold"), text="Welcome to Tic-Tac-Toe!") 
        main_title.place(relx=0.5, rely=0.1, anchor=ctk.CENTER)

        # start button
        label_button = ctk.CTkLabel(master = self.root, font = ("Helvetica", 15, "bold"), text="Try to beat the AI ( •̀ᴗ•́ )و ̑̑")
        label_button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        # start button
        start_button = ctk.CTkButton(master = self.root, font = ("Helvetica", 11), text="Ready!", command=self.startGame)
        start_button.place(relx=0.5, rely=0.60, anchor=ctk.CENTER)
        self.root.mainloop()

        # frame1 = tk.Frame(master=self.root, height=100, bg="cyan")
        # frame1.pack(fill=tk.X)
        # self.root.mainloop()
        pass
    def startGui(self):
        print("Initializing GUI...")
        self.initGui()
        pass
    
    def startGame(self):
        print("Starting game...")
        pass