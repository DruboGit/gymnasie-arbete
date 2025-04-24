from customtkinter import *
import threading
import pickle as p
import time as t
import os.path
import time
import PointGen as point
from generators import *

set_appearance_mode("System")
app = CTk()
app.geometry("500x500")
app.resizable(False, False)
app.title("Project Incremental")
gen_page = CTkFrame(app)
upg_page = CTkFrame(app)
opt_page = CTkFrame(app)


def main():
    global point_count
    save_exist = os.path.isfile("save.dat")
    if save_exist == True:
        point.load_game()
    point_count = CTkLabel(master=app, text=f"{points} Points", font=("Arial",20))
    point_count.place(relx=0.5, rely=0.05, anchor=CENTER)
    generators_button = CTkButton(master=app, text="Generators", width=10, fg_color="gray", command=generators)
    generators_button.place(relx=0.352, rely=0.1, anchor=CENTER)
    upgrades_button = CTkButton(master=app, text="Upgrades", width=10, fg_color="gray", command=upgrades)
    upgrades_button.place(relx=0.5, rely=0.1, anchor=CENTER)
    options_button = CTkButton(master=app, text="Options", width=10, fg_color="gray", command=options)
    options_button.place(relx=0.63, rely=0.1, anchor=CENTER)
    generators()
    point_thread = threading.Thread(target=point.point_gen)
    point_thread.daemon = True
    point_thread.start()
    point_update_thread = threading.Thread(target=point_update)
    point_update_thread.daemon = True
    point_update_thread.start()

def generators():
    global gen_page
    gen_page.destroy()
    upg_page.destroy()
    opt_page.destroy()
    gen_page = CTkFrame(app, width=500, height=425)
    gen_page.place(x=0, y=75)
    generator("gen1", gen_page, 10)

def upgrades():
    global upg_page
    gen_page.destroy()
    upg_page.destroy()
    opt_page.destroy()
    upg_page = CTkFrame(app, width=500, height=425)
    upg_page.place(x=0, y=75)

def options():
    global opt_page
    gen_page.destroy()
    upg_page.destroy()
    opt_page.destroy()
    opt_page = CTkFrame(app, width=500, height=425)
    opt_page.place(x=0, y=75)
    CTkButton(master=opt_page, text="Save", command=save_game).place(x=0, y=0)

def point_update():
    while True:
        time.sleep(0.1)
        point_count.configure(text=f"{points} Points")
        if points > gens["gen1"].price:
            gens["gen1"].button.configure(state="enabled")

def save_game():
    with open('save.dat','wb') as save:
        p.dump([point.points, point.gen1, point.gen1_bought, point.gen1_mult, point.gen1_mult_req, point.gen1_price], save, protocol=2)

main()
app.mainloop()