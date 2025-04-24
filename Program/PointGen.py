import time
import pickle as p
from generators import *

def point_gen():
    global gen1, points
    while True:
        time.sleep(1)
        points += gens["gen1"].amount * gens["gen1"].mult

def load_game():
    global points, gen1, gen1_bought, gen1_mult, gen1_mult_req, gen1_price
    with open('save.dat','rb') as save:
        points, gen1, gen1_bought, gen1_mult, gen1_mult_req, gen1_price = p.load(save)