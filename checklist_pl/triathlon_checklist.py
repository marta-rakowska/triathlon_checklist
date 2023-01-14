from lista_rzeczy_do_zabrania import ListaRzeczyDoZabrania
from listy_rzeczy import lista_plywanie, lista_rower, lista_bieg, lista_inne

def wypisz_menu():
    print('1. Wybierz listę.')
    print('2. Dodaj rzecz do listy.')
    print('3. Oznacz rzecz jako spakowaną.')
    print('4. Pokaż rzeczy do spakowania i spakowane.')
    print('5. Usuń rzecz do spakowania.')
    print('6. Ustaw konkretną rzecz na początku.')
    print('7. Wyjdź z programu.')

def pobierz_opcje_do_zabrania():
    while True:
        i = input('Co chcesz zrobić? (1-6): ')
        try:
            liczba = int(i)
        except ValueError:
            print('To musi być liczba.')
            continue
        if 1 <= liczba <= 7:
            return liczba
        print('To musi być liczba od 1 do 7.')

def petla_glowna_programu():
    lista_rzeczy_plywanie = ListaRzeczyDoZabrania(lista_plywanie, nazwa='Pływanie')
    lista_rzeczy_rower = ListaRzeczyDoZabrania(lista_rower, nazwa='Rower')
    lista_rzeczy_bieg = ListaRzeczyDoZabrania(lista_bieg, nazwa='Bieg')
    lista_rzeczy_inne = ListaRzeczyDoZabrania(lista_inne, nazwa='Inne')
    lista_rzeczy_do_zabrania = lista_rzeczy_plywanie
    while True:
        wypisz_menu()
        opcja = pobierz_opcje_do_zabrania()
        if opcja == 1:
            odp = input('Na którą listę chcesz zmienić? (Pływanie, Rower, Bieg, Inne): ').lower()
            if odp.startswith('p'):
                lista_rzeczy_do_zabrania = lista_rzeczy_plywanie
            elif odp.startswith('r'):
                lista_rzeczy_do_zabrania = lista_rzeczy_rower
            elif odp.startswith('b'):
                lista_rzeczy_do_zabrania = lista_rzeczy_bieg
            elif odp.startswith('i'):
                lista_rzeczy_do_zabrania = lista_rzeczy_inne
            print(f"Lista została zmieniona na {lista_rzeczy_do_zabrania.nazwa}")
        elif opcja == 2:
            lista_rzeczy_do_zabrania.dodaj_rzecz_do_zabrania()
        elif opcja == 3:
            lista_rzeczy_do_zabrania.oznacz_rzecz_jako_zabrana()
        elif opcja == 4:
            lista_rzeczy_do_zabrania.pokaz_liste()
        elif opcja == 5:
            lista_rzeczy_do_zabrania.usun_rzecz_do_zabrania()
        elif opcja == 6:
            lista_rzeczy_do_zabrania.ustaw_rzecz_na_poczatek()
        elif opcja == 7:
            return

petla_glowna_programu()