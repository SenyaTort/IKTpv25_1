import glob
import os

f = open('kasutajad.txt', 'r')
print(dir(f))
f.close()

def leia_prokeltifailid(laiend):
    if not laiend.startswith("."):
        laiend = "." + laiend
    return glob.glob(f"*{laiend}")

def analuusi_faili_sisu(failitee):
    element=input("Sisesta rida, mida faili otsida: ")
    loend.append(element)
    with open(Test.txt,encoding="utf-8") as f:


def loo_raporti_kataloog(nimi="Analüüsi_Raportid")->bool:
    """loomise funktsioon raportite kataloogi jaoks.
    kui kataloog ei eksisteeri, loob selle ja tagestab True.
    kui kataloog juba eksisteerib, tagastab False.
    nimi: kataloogi nimi vaikimisi "Analüüsi raportid").
    """
    if not os.path.exists(nimi):
        os.mkdir(nimi)
        return True
    return False

def leia_failid_algustahega(taht:str):
    """
    otsib praegusest kataloogist faile, mis algavad määratud tähega.
    täht: Algustäht
    """
    return glob.glob(f"{taht}*.*")

def otsi_faili(faili_nimi, otsingu_tee="."):
    for juur, failid in os.walk(otsingu_tee):
        if faili in failid:
            return os.path.join(juur, faili_nimi)
        return "Faili ei leitud"
    
# naide kasutamisest
# otsitav_fail=input("Sisesta otsitava faili nimi (nt minu_fail.txt): ")
# tulemus = otsi_faili(otsitav_fail)
# print(tulemus)