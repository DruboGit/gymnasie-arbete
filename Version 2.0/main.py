from customtkinter import *
import classes as c
import threading
import time
from decimal import Decimal

c.root.resizable(False, False)
c.root.geometry("500x500")

class App():
    def __init__(self):
        c.root.grid_columnconfigure(0, weight=1)

        self.genFrame = CTkFrame(c.root, width=500)
        self.upgContainer = CTkFrame(c.root, width=500)
        self.upgFrame = CTkFrame(self.upgContainer, width=300)
        self.upgDetailsFrame = CTkFrame(self.upgContainer, width=200)
        self.setFrame = CTkFrame(c.root, width=500)


        c.point_label.grid(column=0, row=0, sticky="")
        self.nav = CTkFrame(master=c.root)
        self.nav.grid(column=0, row=1, sticky="")
        self.generatorsButton = CTkButton(master=self.nav, text="Generators", command=self.generatorsPage)
        self.generatorsButton.grid(column=0, row=0)
        self.upgradesButton = CTkButton(master=self.nav, text="Upgrades", command=self.upgradesPage)
        self.upgradesButton.grid(column=1, row=0)
        self.settingsButton = CTkButton(master=self.nav, text="Settings", command=self.settingsPage)
        self.settingsButton.grid(column=2, row=0)
        self.spacer = CTkLabel(c.root, text=" ")
        self.spacer.grid(column=0, row=2)

        self.generators = [c.Generator(self.genFrame, 1, "points", 10), c.Generator(self.genFrame, 2, "gen1", 100), c.Generator(self.genFrame, 3, "gen2", 10000), c.Generator(self.genFrame, 4, "gen3", 1000000), c.Generator(self.genFrame, 5, "gen4", 100000000)]
        self.upgrades = [c.Upgrade(self.upgFrame, self.upgDetailsFrame, "Test", "Test desription, dont mind", 100)]

        point_thread = threading.Thread(target=self.generate)
        point_thread.daemon = True
        point_thread.start()

    def generatorsPage (self):
        self.setFrame.grid_forget()
        self.upgContainer.grid_forget()
        self.genFrame.grid(column=0, row=3, sticky="nsew")
        k = 0
        for i in self.generators:
            i.label.grid(column=0, row=k, sticky="W")
            i.price_tag.grid(column=2, row=k)
            i.buy_button.grid(column=3, row=k, sticky="E")
            k += 1
        self.genFrame.grid_columnconfigure(1,weight=1)
        
    def upgradesPage (self):
        self.genFrame.grid_forget()
        self.setFrame.grid_forget()
        self.upgContainer.grid(column=0, row=3, sticky="NSEW")
        self.upgFrame.grid(column=0, row=0)
        self.upgDetailsFrame.grid(column=1, row=0)
        k = 0
        for i in self.upgrades:
            i.icon.grid(column=0, row=k, sticky="N")
            k += 1
        self.upgContainer.grid_columnconfigure(1, weight=1)
    
    def settingsPage (self):
        self.genFrame.grid_forget()
        self.upgContainer.grid_forget()
        self.setFrame.grid(column=0, row=3)

    def generate (self):
        while True:
            time.sleep(1)
            for i in self.generators:
                match i.generate:
                    case "points":
                        c.points += self.generators[0].amount
                        if c.points >= 10000:
                            c.points_show = format(Decimal(c.points), ".3e")
                        else:
                            c.points_show = c.points
                        c.point_label.configure(text=f"{c.points_show} Points")
                    case "gen1":
                        self.generators[0].amount += self.generators[1].amount
                        self.generators[0].label.configure(text=f"Generator {self.generators[0].number} | {self.generators[0].amount}")
                    case "gen2":
                        self.generators[1].amount += self.generators[2].amount
                        self.generators[1].label.configure(text=f"Generator {self.generators[1].number} | {self.generators[1].amount}")
                    case "gen3":
                        self.generators[2].amount += self.generators[3].amount
                        self.generators[2].label.configure(text=f"Generator {self.generators[2].number} | {self.generators[2].amount}")
                    case "gen4":
                        self.generators[3].amount += self.generators[4].amount
                        self.generators[3].label.configure(text=f"Generator {self.generators[3].number} | {self.generators[3].amount}")
                    case "gen5":
                        self.generators[4].amount += self.generators[5].amount
                        self.generators[4].label.configure(text=f"Generator {self.generators[4].number} | {self.generators[4].amount}")
                if c.points < i.price:
                    i.buy_button.configure(state=DISABLED)
                else:
                    i.buy_button.configure(state=NORMAL)
            for i in self.upgrades:
                if c.points < i.cost:
                    i.buyButton.configure(state=DISABLED)
                elif not i.owned:
                    i.buyButton.configure(state=NORMAL)
    

App()
c.root.mainloop()