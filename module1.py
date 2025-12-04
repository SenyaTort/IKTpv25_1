
# import msvcrt
# Sisestamise ajal asendatakse kõik tähted @-märgiga
# täht=""
# while True:
#     t=msvcrt.getwch()
#     print(t.replace(t,"*")),end="",flush=True)
#     täht+=t
#     if t=='\r': #Enter
#         break
# print()
# print(täht)


#list-loend
#Loome listi
# l=[] #tühi list
# print(f"Listi algseis: {l}")
# while True:
#     print("Tee valik:")
#     print("1-Lisa elemente\n2-Lisa elemente pos-le\n3-Eemalda")
#     print("4- Eemalda element nime järgi")
#     while True:
#         try:
#             valik=int(input())
#             break
#         except:
#             print("Arvud: 1...n")
#     print("Töö listiga")
#     if valik==1:
#         while True: 
#             try: 
#                 i=int(input("Mitu elementi soovid lisada? "))
#                 if i>0:
#                     break
#                 else:
#                     print("Arvud >0")
#             except:
#                 print("Täisarvud on vaja kasutada")
#         for element_id in range(i):
#             element=input(f"{element_id}. element:")
#             l.append(element)
#         print("Uuendatud list on {l}")
#     elif valik==2:
#         while True:
#             try:
#                 pos=int(input(f"Positsioon kuhu soovid lisada (0-{len(l)}): "))
#                 if 0<=pos<=len(l):
#                     break
#                 else:
#                     print(f"Positsioon peab olema vahemikus 0 kuni {len(l)}")
#             except:
#                 print("Täisarv on vaja kasutada")
#         element=input("Sisesta element mida soovid lisada: ")
#         l.insert(pos,element) #Lisab elemendi soovitud positsioonile

#     elif valik==3:
#             while True:
#                 try:
#                     pos=int(input(f"Positsioon kuhu soovid lisada (0-{len(l)}): "))
#                     if 0<=pos<=len(l):
#                         break
#                     else:
#                         print(f"Positsioon peab olema vahemikus 0 kuni {len(l)}")
#                 except:
#                     print("Täisarv on vaja kasutada")
#             eem_element=l.pop(pos)
#             print(f"Eemaldatud element on {eem_element}")
#     elif valik==4:
#         element=input("Sisesta element mida soobid eemaldada: ")
#         mitu=l.count(element)
#         if mitu==0:
#             print("Elementi ei leitud")
#         else:
#             for 0 in range(mitu):
#                 print(f"Eemaldame element "{element}" {l.index(element)} poeitsioonilt")
#                 l.remove(element)
#         print(f"Eemaldati {mitu} elementi")
# print(f"Uuendatud list on {l}")

#loend.extend()
#loend.sort()
#loend.reverse()
#loend.clear()
#lornd.index()
#loend.list

# l=[]
# print("Mitu lehte soovite luua?")
# while True:
#     print("Mitu lehe sa luua tahad?")
