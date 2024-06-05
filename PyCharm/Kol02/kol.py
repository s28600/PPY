class Produkt:
    def __init__(self, id, nazwa, kategoria, cena):
        if cena <= 0:
            raise ValueError("Cena musi być większa od zera")

        self.id = id
        self.nazwa = nazwa
        self.kategoria = kategoria
        self.cena = cena

    def __lt__(self, other):
        return self.nazwa < other.nazwa

    def __eq__(self, other):
        return self.nazwa == other.nazwa

    def __str__(self):
        return f"{self.id} {self.nazwa} {self.kategoria} {self.cena:.2f}"


class Magazyn:
    def __init__(self):
        self.lista_produkty = list()
        self.stan_magazynu = dict()

    def add_produkt(self, produkt):
        if produkt.id not in self.stan_magazynu.keys():
            self.stan_magazynu[produkt.id] = 1
            self.lista_produkty.append(produkt)
        else:
            self.stan_magazynu[produkt.id] += 1

    def wyswietl_produky(self):
        for produkt in sorted(self.lista_produkty, key=lambda p: p.nazwa):
            print(produkt)

    def wartosc_magazynu(self):
        wartosc = 0
        for produkt in self.lista_produkty:
            wartosc += produkt.cena * self.stan_magazynu[produkt.id]
        return wartosc

    def zapisz_stan_magazynu(self):
        with open("stan_magazynu", 'w') as file:
            for produkt in sorted(self.lista_produkty, key=lambda p: p.nazwa):
                file.write(f"{produkt} {self.stan_magazynu[produkt.id]}\n")

    def dodaj_produkty_z_pliku(self, nazwa_pliku):
        with open(nazwa_pliku, "r") as f:
            read_content = f.read()
            for line in read_content.splitlines():
                params = line.split(" ")
                new_produkt_id = int(params[0])
                new_produkt_ilosc = int(params[4])
                if new_produkt_id not in self.stan_magazynu.keys():
                    self.add_produkt(Produkt(new_produkt_id, params[1], params[2], float(params[3])))
                    self.stan_magazynu[new_produkt_id] = new_produkt_ilosc
                else:
                    self.stan_magazynu[new_produkt_id] += new_produkt_ilosc


produkt1 = Produkt(1, "Nazwa1", "Kategoria", 20)
produkt2 = Produkt(2, "Nazwa2", "Kategoria", 30)
produkt3 = Produkt(3, "Nazwa3", "Kategoria", 10)
magazyn = Magazyn()
magazyn.add_produkt(produkt3)
magazyn.add_produkt(produkt2)
magazyn.add_produkt(produkt1)
magazyn.add_produkt(produkt1)
magazyn.add_produkt(produkt3)
magazyn.add_produkt(produkt3)
magazyn.wyswietl_produky()
print(magazyn.stan_magazynu)
print(magazyn.wartosc_magazynu())
magazyn.zapisz_stan_magazynu()
magazyn.dodaj_produkty_z_pliku("dodatkowe_produkty")
magazyn.wyswietl_produky()
print(magazyn.stan_magazynu)
print(magazyn.wartosc_magazynu())
