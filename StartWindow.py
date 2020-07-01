import tkinter as tk

class StartWindow:
    wind = None
    def __init__(self):
        self.wind = tk.Tk()
        self.wind.geometry("700x700")
        lab1 = tk.Label(
            self.wind, 
            text="Welcome to BattleShip! Click here to start the game",
            height=int(700/2),
            width=int(700/2),
            font=("Helvetica", 18)
            )
        but1 =tk.Button(
            self.wind, 
            text="Start",
            font=("Helvetica", 10)
            )

        but1.place(height=int(200),width=int(200),relx=0.5, rely=0.5,)
        but1.pack()
        lab1.pack()

        self.wind.mainloop()
        


    