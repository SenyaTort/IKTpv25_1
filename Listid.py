# import string
# t=[ 'a', 'e', 'i', 'o', 'u', 'ü', 'ä', 'ö', 'õ']
k=[ 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 'š', 'z', 'ž', 't', 'v', 'w', 'x', 'y' ]
# m=string.punctuation + string.whitespace
# sõna_lause=input("Sisesta sõna või lause: ").lower()
# täishäälijud=0
# kaashäälikud=0
# märgid=0
# for täht in sõna_lause:
#     if täht in t:
#         täishäälijud+=1
#     elif täht in k:
#         kaashäälikud+=1
#     elif täht in m:
#         märgid+=1
# print(f"Sõnas/lauses on {täishäälijud} täishäälikut, {kaashäälikud} kaashäälikut ja {märgid} märki.")


# names = []
# for i in range(5):
#     ask = input("Sisesta palun 5 nimi:")
#     names.append(ask)

# print(names)
# vimane_nimi = names [-1]
# names.sort()
# print(names)
# print(vimane_nimi)
# replace = input("Kas sa tahad muuta nimi? ")
# if replace == "jah":
#     ask2 = input("Mis nimi muutame?")
#     ask3 = input("Mis uus nimi?")
#     find = names.index(ask2)
#     names[find] = ask3
#     print(names)
# else:
#     print(names)

# vanused = [12, 15, 16, 19, 26]
# suurim = max(vanused)
# väiksem = min(vanused)
# kogusumma = sum(vanused)
# keskmist = kogusumma / len(vanused)
# print(f"Suurim vanus on {suurim}, väiksem vanus on {väiksem}, vanuste kogusumma on {kogusumma} ja vanuste keskmine on {keskmist}.")


# rida = [7, 5, 3, 3, 2, 1]
# for i in rida:
#     print("*" * i)
#     numbrid = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     paaris = []
#     for number in numbrid:
#         if number % 2 == 0:
#             paaris.append(number)



# indexid = ["Tallinn", "Narva, Narva-Jõesuu", "Kohtla-Järve", "Ida-Virumaa, Lääne-Virumaa", "Tartu", "Tartumaa, Põlvamaa, Võrumaa, Valgamaa", "Viljandimaa, Järvamaa, Harjumaa, Raplamaa", "Pärnumaa", "Läänemaa, Hiiumaa, Saaremaa"]
# while True:
#     try:
#         index=int(input("Sisesta oma postiinedeks (5-kohaline): "))
#         if 10000 <= index <= 99999:
#             break
#         else:
#             print("Palun sisesta kehtiv 5-kohaline postiindeks.")
#     except:
#         print("vigane andmetüüp")
# index_list=list(str(index))
# n1=int(index_list[0])
# print(f"Sinu postiindeksiga {index} kuulub piirkonda: {indexid[n1-1]}")
# if n1 in [0,1,2,7]:
#     print("Mine merre!")
# else:
#     print("Mine metsa!")

# from random import  randint, choice
# loend_arvud=[]
# loend_tähed=[]
# loend_kaashäälikud=[]
# mitu=randint(2, 20)
# for i in range(mitu):
#     elem=randint(0, 100)
#     loend_arvud.append(elem)
#     elem=chr(randint(65,90))
#     loend_tähed.append(elem)
#     elem=choice(k)
#     loend_kaashäälikud.append(elem)
#     print(f"Kokku on {mitu} elemente loendis")
#     while True:
#         try:
#             paaride_arv=int(input(f"Sisesta mitu paarist soovid vaadata: "))
#             if 1 <= paaride_arv <= mitu//2:
#                 break
#             else:
#                 print(f"Palun sisesta arv vahemikus 1 kuni {mitu//2}")
#         except:
#             print("Vigane andmetüüp, proovi uuesti")


from random import  randint
loend_arvud=[]
mitu=randint(2, 20)
for i in range(mitu):
    elem=randint(0, 100)
    loend_arvud.append(elem)
print(loend_arvud)
suurim=max(loend_arvud)
kus_asub=loend_arvud.index(suurim)
suurim_muudatud=suurim/mitu
loend_arvud[kus_asub]=round(suurim_muudatud,2)
print(f"Muutmise järel:{loend_arvud}")