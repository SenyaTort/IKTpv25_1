# 5.1
# 1

# def float_kontroll(sisend:str)->float:
#     """Kontrolib, kas sisestatud andmed on teisendatavad float arvuks
#     :param str sisend: kasutaja sisestatud andmed 
#     :return/rtype: teisendatud float arv
#     """
#     while True:
#             try:
#                 arv=float(sisend)
#                 return arv
#             except ValueError:
#                 sisend=input("Palun sisesta arv: ")

# def arithmetic(a:float,b:float,tehe:str)->any:
#     """Lihtne Kalkulaator:
#     + - Liitmine
#     - - Lahutamine 
#     * - Korrutamine
#     / - Jagamine
#     Muul juhul tagastab "Tundmatu tehe"
#     :param float a: esimene arv
#     :param float b: teine arv
#     :param str tehe: tehe,mis tuleb teha
#     :return/rtype: tehte tulemus float või str 
#     """
#     if tehe in ["+", "-", "*", "/"]:
#         if tehe=="/" and b==0:
#             vastus = "Nulliga jagamine pole lubatud"
#         else:
#             vastu=eval(f"(a)(tehe)(b)") #tehe teostamine eval funktsiooniga 
#     else:
#         vastus="Tundmatu tehe"
#     return vastus

# 2
# def is_year_leap(aasta:int)->bool:
#     """Kontrollib, kas aasta on liigaasta
#     :param int aasta: aasta arvuma
#     :return/rtype: True kui liigaasta, False kui tavaline aasta
#     """
#     if (aasta % 4 == 0 and aasta % 100 != 0):
#         return True
#     else:
#         return False

#3
# def square(külg:float)->any:
#     """Arvutab ruudu ümbermõõdu, pindala ja diagonaali
#     :param float külg: ruudu külje pikkus
#     :return/rtype: ümbermõõt, pindala, diagonaal
#     """
#     ümbermõõt=4*külg
#     pindala=külg*külg
#     diagonaal=külg**0,5*2
#     return ümbermõõt, pindala, diagonaal
#4
# def season(kuu:int)->str:
#     """tagastab aastaaja kuu numbri põhjal
#     :param int kuu: kuu number (1-12)
#     :return/rtype: hooaja nimetus str
#     """
#     if kuu in [12,1,2]:
#         return "talv"
#     elif kuu in [3,4,5]:
#         return "kevad"
#     elif kuu in [6,7,8]:
#         return "suvi"
#     elif kuu in [9,10,11]:
#         return "sügis"
#     else:
#         return "Vigane kuu number"

#5
def bank(a:float.years:int)->float:
    """Arvutab lõppsumma koos intressiga 
    :param float a: algsumma
    :param int years: aastate arv
    :return/rtype: lõppsumma float
    """
    intress=0.1
    for i in range(years):
        a+=a*intress
    return a
#6