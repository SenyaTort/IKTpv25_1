paev=input("Sisesta päeva nimetus (näiteks esmaspäev): ")
#1. kui on neljapäev, siis "Huraaa, programmeerimine!
if paev.lower()=="neljapäev":
    print("Huraaa, programmeerimine!")

#2. kui on neljapäev, siis "Huraaa, programmeerimine!, kui on reede, siis "igatsen, programmeerimine
if paev.lower()=="neljapäev":
    print("Huraaa, programmeerimine!")
else:
    print("Igatsen, programmeerida tahaks!")
#3. tööpaevad ja nädalavahetus 
if paev.lower()=="laupäev" or paev.lower()=="pühapäev":
    print("Lõpuks ometi nädalavahetus!")
else:
    print("tööpäev, pean tööl käima!")