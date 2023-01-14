class ListaRzeczyDoZabrania:

    def __init__(self, lista, nazwa):
        self.nazwa = nazwa
        self.lista = lista
        # for i in range(poczatkowa_liczba_pozycji):
        #     self.lista.append(f'A-{i+1}')
        self.zbior_rzeczy_zabranych = {''}

    def dodaj_rzecz_do_zabrania(self):
        self.lista.append(input('Podaj co chcesz zabrać: '))

    def _kwadracik(self, element):
        if element in self.zbior_rzeczy_zabranych:
            return "[x]"
        return "[ ]"

    def pokaz_liste(self):
        print(f'Zawartość listy o nazwie {self.nazwa}')
        for element in self.lista:
            print(f"{self._kwadracik(element)} {element}")

    def oznacz_rzecz_jako_zabrana(self):
        for i, element in enumerate(self.lista):
            print(f'{i+1}. {element}')
        indeks_do_oznaczenia = int(input('Który element oznaczyć? ')) - 1
        self.zbior_rzeczy_zabranych.add(self.lista[indeks_do_oznaczenia])

    def usun_rzecz_do_zabrania(self):
        for i, element in enumerate(self.lista):
            print(f'{i+1}. {element}')
        indeks_do_usuniecia = int(input('Który element chcesz usunąć? ')) - 1
        del self.lista[indeks_do_usuniecia]

    def ustaw_rzecz_na_poczatek(self):
        for i, element in enumerate(self.lista):
            print(f'{i + 1}. {element}')
        indeks_do_ustawienia_na_poczatek = int(input('Który element chcesz przenieść? ')) - 1
        element_na_poczatek = self.lista.pop(indeks_do_ustawienia_na_poczatek)
        self.lista.insert(0, element_na_poczatek)