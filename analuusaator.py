import glob
import os
from datatime import datatime

f = open('kasutajad.txt', 'r')
print(dir(f))
f.close()

def leia_prokeltifailid(laiend):
    if not laiend.startswith("."):
        laiend = "." + laiend
    return glob.glob(f"*{laiend}")

def analuusi_faili_sisu(failitee):
