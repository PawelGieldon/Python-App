#%%

from funkcje import licz_sume_salatek, licz_sume_miesa, licz_sume_sokow , licz_sume_deserow


start = True
wyniki_sałatek = []
wyniki_mieso = []
wyniki_soki = []
wyniki_desery = []



def co_chcesz_zrobic(opcja):
    if opcja == 'tak':
        print('Menu\n\t 1. salatka \n\t 2. mieso \n\t 3. soki \n\t 4. desery' )
        menu = input('Wybierz danie: ').lower()

        if menu == 'salatka' or menu == '1':            
            ilosc = int(input('Podaj ilość sałatek (Maksymalnie 5) '))
            suma = licz_sume_salatek(ilosc)
            print(f" ilość {ilosc} sałatek wynosi {suma} zł")
            wyniki_sałatek.append(suma)

        elif menu == 'mięso' or menu == 'mieso' or menu == '2':
            ilosc = int(input('Podaj ilość mięs (Maksymalnie 5) '))
            suma = licz_sume_miesa(ilosc)
            print(f" ilość {ilosc} mięs wynosi {suma} zł")
            wyniki_mieso.append(suma)

        elif menu == 'soki'  or menu == '3':
            ilosc = int(input('Podaj ilość soków (Maksymalnie 5) '))
            suma = licz_sume_sokow(ilosc)
            print(f" ilość {ilosc} soków wynosi {suma} zł")
            wyniki_soki.append(suma)

        elif menu == 'desery'  or menu == '4':
            ilosc = int(input('Podaj ilość deserów (Maksymalnie 5) '))
            suma = licz_sume_deserow(ilosc)
            print(f" ilość {ilosc} deserów wynosi {suma} zł")
            wyniki_desery.append(suma)
            

    elif opcja == 'nie':
        
        with open('wyniki.txt','w') as file:
            for wynik in wyniki_sałatek:
                file.write(f"Kwota do zaplacenia za salatki: {str(wynik)} zl\n")
            for wynik in wyniki_mieso:
                file.write(f"Kwota do zaplacenia za mieso: {str(wynik)} zl\n")
            for wynik in wyniki_soki:
                file.write(f"Kwota do zaplacenia za soki: {str(wynik)} zl\n")
            for wynik in wyniki_desery:
                file.write(f"Kwota do zaplacenia za desery: {str(wynik)} zl\n")
        quit()
        
        

while start:
        opcja = input('Czy chcesz uruchomić program?(tak/nie)').lower()
        co_chcesz_zrobic(opcja)


# %%
