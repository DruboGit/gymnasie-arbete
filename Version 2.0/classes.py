from customtkinter import *
from decimal import Decimal

root = CTk()
points = 190
points_show = points
point_label = CTkLabel(master=root, text=f"{points} Points", font=("Arial",20))

class Generator():
    def __init__(self, genFrame, number, generate, price):
        self.amount = 0
        self.generate = generate
        self.number = number
        self.price = price
        self.label = CTkLabel(genFrame, text=f"Generator {self.number} | {self.amount}")
        self.price_tag = CTkLabel(genFrame, text=f"Price: {format(Decimal(self.price), ".0e") if self.price >= 10000 else self.price}")
        self.buy_button = CTkButton(genFrame, text="Buy", width=10, command=self.buy)

    def buy (self):
        global points
        self.amount += 1
        self.label.configure(text=f"Generator {self.number} | {self.amount}")
        points -= self.price
        point_label.configure(text=f"{points} Points")

class Upgrade():
    def __init__(self, upgFrame, upgDetailsFrame, name, desc, cost):
        self.name = name
        self.desc = desc
        self.cost = cost
        self.owned = False

        self.icon = CTkButton(upgFrame, text=self.name, width=300, command=self.openUpgrade)

        self.nameLabel = CTkLabel(upgDetailsFrame, text=self.name, font=("Arial", 20))
        self.descLabel = CTkLabel(upgDetailsFrame, text=self.desc)
        self.priceTag = CTkLabel(upgDetailsFrame, text=f"{self.cost} Points")
        self.buyButton = CTkButton(upgDetailsFrame, text="Buy", command=self.buy)
    
    def openUpgrade(self):
        self.nameLabel.grid(column=0, row=0)
        self.descLabel.grid(column=0, row=1)
        self.priceTag.grid(column=0, row=2)
        self.buyButton.grid(column=0, row=3)
        if points < self.cost:
            self.buyButton.configure(state=DISABLED)

    def buy(self):
        global points
        self.owned = True
        points -= self.cost
        self.buyButton.configure(text="Bought", state=DISABLED)