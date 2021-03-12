class Catalog:

    # variabila clasei/globala
    lista_obiecte = []
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
        

    def afisare_dupa_producator(self, s):
        """ Afisare produse dupa producator """
        self.s = s
        result = filter(lambda self: self.producator == s, Catalog.lista_obiecte)
        print("Produsele producatorului:",s)
        ##print(list(result))
        for produs in result:
            print(f"{produs.producator}: cod produs -> {produs.cod_produs} | pret -> {produs.pret} | consum -> {produs.consum} ")
             
            

    def afiseaza_obiecte_subclasa(self):
        pass


class Electrocasnice_mari(Catalog):
    """ Mosteneste Clasa Catalog """
    def __init__(self, pret, consum, producator, cod_produs,adancime, latime, inaltime):
        super().__init__(pret, consum, producator, cod_produs)
        self.adancime = adancime
        self.latime = latime
        self.inaltime = inaltime
        ##Electrocasnice_mari.clasa.append(self)
        
    # initul trebuie sa mosteneasca initul parintelui, super()
    pass


class Electrocasnice_mici(Catalog):
    #def __init__(self, lungime_cablu, baterie):
    # initul trebuie sa mosteneasca initul parintelui, super()
    pass

class Frigider(Electrocasnice_mari):
    #def __init__(self, capacitate_congelator, capacitate_frigider)
    # initul trebuie sa mosteneasca initul parintelui, super()
    pass


class Aragaz(Electrocasnice_mari):
    #def __init__(self, numar_arzatoare):
    # initul trebuie sa mosteneasca initul parintelui, super()
    pass


class Aragaz(Electrocasnice_mari):
    #def __init__(self, adancime, inaltime, latime):
    # initul trebuie sa mosteneasca initul parintelui, super()
    pass

class Mixer(Electrocasnice_mici):
    #def __init__(self, rotatii_min):
    # initul trebuie sa mosteneasca initul parintelui, super()
    pass


class Fier_calcat(Electrocasnice_mici):
    #def __init__(self, rezervor):
    # initul trebuie sa mosteneasca initul parintelui, super()
    pass

a = Catalog(300,  8, "Dedeman"   ,  4)
b = Catalog(200,  5, "Ikea"      , "KV")
c = Catalog(100,  9, "Jysk"      , "JK")
d = Catalog(1000, 22,"Arabesque" , "AR")
e = Catalog(900,  15, "Arabesque", "AR1")
f = Catalog(50,   9, "Jysk"      , "JK1")


e = Electrocasnice_mari(99,66,"TEST","T1",60,60,170)

print("------SORTARE PRET-------")
a.sorteaza_dupa_pret()
print("------SORTARE CONSUM-------")
a.sorteaza_dupa_consum()
print("------AFISARE PRODUCATORI DISTINCTI-------")
a.afisare_producatori()
print("------AFISARE PRODUSE DUPA PRODUCATOR-------")
a.afisare_dupa_producator("Arabesque")
e.afisare_dupa_producator("TEST")###test din clasa copil Electrocasnice_mari
print ("------------------------------------------------------------------------")
