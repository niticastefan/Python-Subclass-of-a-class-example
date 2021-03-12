class Catalog:

    # variabila clasei/globala
    lista_obiecte = [] # parinte
    clasa = [] # copil
    subclasa = [] # nepot

    def __init__(self, pret, consum, producator, cod_produs):
        self.pret = pret
        self.consum = consum
        self.producator = producator
        self.cod_produs = cod_produs
        Catalog.lista_obiecte.append(self)

    def sorteaza_dupa_pret(self):
        """->> Sorteaza Catalogul de produse dupa pret"""
        for pret in sorted(Catalog.lista_obiecte, key=lambda self: self.pret):
            # obiect._afiseaza_rezultat() # extra
            print(f"{pret.producator}: {pret.pret}")

    def sorteaza_dupa_consum(self):
        """->> Sorteaza Catalogul de produse dupa consum"""
        for consum in sorted(Catalog.lista_obiecte, key=lambda self: self.consum):
            print(f"{consum.producator}: {consum.consum}")
        # obiect._afiseaza_rezultat() # extra
        

    def afisare_producatori(self):
        """ Afisare producatori distincti din Catalog """
        i=0
        temp_list = []
        for prod in sorted(Catalog.lista_obiecte, key=lambda self: self.producator):
            if prod.producator not in temp_list:
                temp_list.append(prod.producator)
                i +=1
                print(f"{i}:{prod.producator}")
           
        # obiect._afiseaza_rezultat() # extra
        
    @staticmethod
    def afisare_dupa_producator(s):
        """ Afisare produse dupa producator """
        ##result = filter(lambda self: self.producator == s, Catalog.lista_obiecte)
        print("Produsele producatorului:",s)
        for item in Catalog.lista_obiecte:
            if item.producator == s:
                print(f"{vars(item)}")
             
            
    @staticmethod
    def afiseaza_obiecte_subclasa(c):
        """ Afisare obiecte subclasa """
        print(f"Obiectele / itemele clasei / sublcasei {c} sunt: \n")
        for item in Catalog.lista_obiecte:
            if type(item).__name__ == c:
                print(f"{vars(item)}")
        print ("----------------------------------------\n")

    @staticmethod
    def afiseaza_toate_produsele():
        """ Afisare obiecte subclasa """
        print(f"Obiectele / itemele instantei sunt: \n")
        for item in Catalog.lista_obiecte:
            print(f"{vars(item)}")    
        print ("----------------------------------------\n")
        
    @staticmethod
    def printeaza_elemente_subclasa(nume_clasa):
        item = {}
        print(f"Obiectele / itemele clasei / sublcasei {nume_clasa} sunt: \n")
        for item in globals():
            if type(globals()[item]).__name__ == nume_clasa:
                print (item)   
        print ("----------------------------------------\n")


class Electrocasnice_mari(Catalog):
    """ Mosteneste Clasa Catalog """
    def __init__(self, pret, consum, producator, cod_produs,adancime, latime, inaltime):
        super().__init__(pret, consum, producator, cod_produs)
        self.adancime = adancime
        self.latime = latime
        self.inaltime = inaltime
    pass

class Electrocasnice_mici(Catalog):
    """ Mosteneste Clasa Catalog """
    def __init__(self, pret, consum, producator, cod_produs,lungime_cablu,baterie):
        super().__init__(pret, consum, producator, cod_produs)
        self.lungime_cablu = lungime_cablu
        self.baterie = baterie
    pass

class Frigider(Electrocasnice_mari):
    """ Mosteneste SubClasa Electrocasnice_mari """
    def __init__(self, pret, consum, producator, cod_produs, adancime, latime, inaltime, capacitate_congelator, capacidate_frigider):
        super().__init__(pret, consum, producator, cod_produs,adancime, latime, inaltime)
        self.capacitate_congelator = capacitate_congelator
        self.capacidate_frigider = capacidate_frigider
        Catalog.clasa.append("Electrocasnice mari")
        Catalog.subclasa.append("Frigider")
    pass


class Aragaz(Electrocasnice_mari):
    """ Mosteneste SubClasa Electrocasnice_mari """
    def __init__(self, pret, consum, producator, cod_produs, adancime, latime, inaltime, nr_arzatoare):
        super().__init__(pret, consum, producator, cod_produs,adancime, latime, inaltime)
        self.nr_arzatoare = nr_arzatoare
        Catalog.clasa.append("Electrocasnice mari")
        Catalog.subclasa.append("Aragaz")
    pass


class Mixer(Electrocasnice_mici):
    """ Mosteneste SubClasa Electrocasnice_mici  """
    def __init__(self, pret, consum, producator, cod_produs, lungime_cablu, baterie, rotatii_min):
        super().__init__(pret, consum, producator, cod_produs, lungime_cablu, baterie)
        self.rotatii_min = rotatii_min
        Catalog.clasa.append("Electrocasnice mici")
        Catalog.subclasa.append("Mixer")


class Fier_calcat(Electrocasnice_mici):
    """ Mosteneste SubClasa Electrocasnice_mici  """
    def __init__(self, pret, consum, producator, cod_produs, lungime_cablu, baterie, rezervor):
        super().__init__(pret, consum, producator, cod_produs, lungime_cablu, baterie)
        self.rezervor = rezervor
        Catalog.clasa.append("Electrocasnice mici")
        Catalog.subclasa.append("Fier_calcat")

a = Catalog(300,  8, "Dedeman"   ,  4)
b = Catalog(200,  5, "Ikea"      , "KV")
c = Catalog(100,  9, "Jysk"      , "JK")
d = Catalog(1000, 22,"Arabesque" , "AR")
e = Catalog(900,  15, "Arabesque", "AR1")
f = Catalog(50,   9, "Jysk"      , "JK1")


g = Electrocasnice_mari(99,66,"El_Mari","e1",60,60,170)
gg = Electrocasnice_mari(88,55,"El_Mari","e2",65,65,175)

h = Electrocasnice_mici(1234,54321,"El_mici","em1",60,60)
hh = Electrocasnice_mici(1,2,"El_mici","em2",60,60)

i = Frigider(88,55,"Frigo1","F1",65,65,175,"300L","50L")
ii = Frigider(88,55,"Frigo2","F2",65,65,175,"200L","150L")

j = Aragaz(99,66,"Aragazul S.R.L","A1",60,60,170,2)
jj = Aragaz(999,66,"Arzatorul S.R.L","A2",60,60,170,4)

k = Mixer(111,222,"Mixer 1","MM1",60,60,'500/rpm')
kk = Mixer(1,2,"Mixer 2","MM2",60,60,'1000/rpm')

l = Fier_calcat(11,22,"Fier 1","ff1",60,60,"1L")
ll= Fier_calcat(1,2,"Fier 2","ff2",60,60,"1.5L")
print("------SORTARE PRET-------")
a.sorteaza_dupa_pret()


print("------SORTARE CONSUM-------")
a.sorteaza_dupa_consum()


print("------AFISARE PRODUCATORI DISTINCTI-------")
a.afisare_producatori()


print("------AFISARE PRODUSE DUPA PRODUCATOR-------")
a.afisare_dupa_producator("Arabesque")
a.afisare_dupa_producator("Frigo")
e.afisare_dupa_producator("El_Mari")
g.afisare_dupa_producator("El_mici")


###cerinta optionala?

print("------AFISARE OBIECTE Clasa / Subclasa -------") 
Catalog.afiseaza_obiecte_subclasa("Catalog")
Catalog.afiseaza_obiecte_subclasa("Electrocasnice_mari")
Catalog.afiseaza_obiecte_subclasa("Electrocasnice_mici")
Catalog.afiseaza_obiecte_subclasa("Frigider")
Catalog.afiseaza_obiecte_subclasa("Aragaz")
Catalog.afiseaza_obiecte_subclasa("Mixer")
Catalog.afiseaza_obiecte_subclasa("Fier_calcat")

###cerinta optionala?
print("------AFISARE numele obiectelor Subclasa -------")
Catalog.printeaza_elemente_subclasa("Electrocasnice_mari")
Catalog.printeaza_elemente_subclasa("Electrocasnice_mici")
Catalog.printeaza_elemente_subclasa("Frigider")
Catalog.printeaza_elemente_subclasa("Aragaz")
Catalog.printeaza_elemente_subclasa("Mixer")
Catalog.printeaza_elemente_subclasa("Fier_calcat")


Catalog.afiseaza_toate_produsele()

####clasa[] si subclasa [] ?
e = 1
for element in Catalog.clasa:
    print(f"{e}.{element}")
    e += 1

e = 1
for element in Catalog.subclasa:
    print(f"{e}.{element}")
    e += 1    
