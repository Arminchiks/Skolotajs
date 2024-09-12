
class Skolotajs: 
    def __init__(self, uzvards, stundu_skaits_nedela, tips):
        
        self.uzvards=uzvards
        self.stundu_skaits_nedela=stundu_skaits_nedela
        self.tips=tips
    def izdrukat(self):
        pass

class SakumskolasSkolotajs:
    def __init__(self, uzvards, stundu_skaits_nedela,klase, tips):
        
        self.uzvards=uzvards
        self.stundu_skaits_nedela=stundu_skaits_nedela
        self.tips=tips
        self.klase=klase
    def izva():
        return ("Skolotājs {} māca {} stundas {} klasē").format(uzvards,stundu_skaits_nedela, klase)

class VidusskolasSkolotajs:
    def __init__(self, uzvards, stundu_skaits_nedela, tips, kopa):
        self.uzvards=uzvards
        self.pp=pp
        self.stundu_skaits_nedela=stundu_skaits_nedela
        self.op=op
        self.tips=tips
        self.kopa=kopa
    def izv():
        return ("skolotājs {} māca šādus priekšmetus: {} un {}, kopā {} stundas").format(uzvards,pp,op,kopa)


tipins=int(input("Ievadiet kuru tipu gribat 1 vai 3?: "))
if tipins==1:
    uzvards=input("Ievadiet sākumskolas skolotāja uzvārdu: ")
    klase=input("Ievadiet skolotāja klasi: ")
    stundu_skaits_nedela=int(input("Ievadiet skolotaja stundu skaitu: "))
    print(SakumskolasSkolotajs.izva())
elif tipins==3:
    uzvards=input("Ievadiet vidusskolas skolotāja uzvārdu: ")
    pp=input("Ievadiet pirmo pasniegto priekšmetu: ")
    stundu_skaits_nedela=int(input("Ievadiet pirmā priekšmeta stundu skaitu: "))
    op=input("Ievadiet otro pasniegto priekšmetu: ")
    stn=int(input("Ievadiet otrā priekšmeta stundu skaitu: "))
    kopa=stundu_skaits_nedela+stn
    print(VidusskolasSkolotajs.izv())
else:
    print("")







 








##Ievadiet sākumskolas skolotāja uzvārdu: Bērziņš
#Ievadiet skolotāja klasi: 2.a
#Ievadiet skolotāja stundu skaitu: 15
#Ievadiet vidusskolas skolotāja uzvārdu: Ozols
#Ievadiet pirmo pasniegto priekšmetu: matemātika
#Ievadiet pirmā priekšmeta stundu skaitu: 12
#Ievadiet otro pasniegto priekšmetu: datorika
#Ievadiet otrā priekšmeta stundu skaitu: 8
#Izvades piemērs:
#Sākumskolas (tips – 1) skolotājs Bērziņš māca 15 stundas 2.a klasē.
#Vidusskolas (tips – 3) skolotājs Ozols māca šādus priekšmetus: matemātika un datorika, kopā 20 stundas.

