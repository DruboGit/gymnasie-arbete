from customtkinter import *

points = 10
gens = {}

class generator:
    def __init__(self, label: str, master: CTkFrame, price: int):
        self.amount = 0
        self.bought = 0
        self.mult = 1
        self.mult_req = 10
        self.price = price

        self.label = CTkLabel(master=master, text=f"Point Generator: {self.amount} ({self.bought}) ({self.mult}x)", font=("Arial", 16))
        self.label.place(x=0, y=0)
        self.button = CTkButton(master=master, text="Buy", font=("Arial", 16), width=10, command=self.purchase)
        self.button.place(x=450, y=0)
        self.pricetag = CTkLabel(master=master, text=f"Price: {self.price}", font=("Arial", 14))
        self.pricetag.place (x=350, y=0)
        gens[label] = self

    
    def purchase(self):
        global points
        self.bought += 1
        self.amount += 1
        points -= self.price
        if points < self.price:
            self.button.configure(state="disabled")
        if self.bought >= self.mult_req:
            self.mult *= 2
            self.mult_req += 10
        self.label.configure(text=f"Point Generator: {self.amount} ({self.bought}) ({self.mult}x)")
