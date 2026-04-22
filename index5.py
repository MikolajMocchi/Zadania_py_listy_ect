d4c = {
	'1' : {
        'model': 'T_minus',
        'typ': 'dobry',
        'cena_za_godzine': 50.00,
        'dostepnosc': True,
	},
	'2' : {
        'model': 'MGS',
        'typ': 'cichy',
        'cena_za_godzine': 30.00,
        'dostepnosc': False,
	},
	'3' : {
        'model': 'MGV',
        'typ': 'mocny',
        'cena_za_godzine': 140.00,
        'dostepnosc': True,
	},
	'4' : {
        'model': 'SIG',
        'typ': 'szczytowy',
        'cena_za_godzine': 70.00,
        'dostepnosc': True,
	},
}


while(True):
    print("> BikeLand")
    print("> Wybierz opcje")
    print("1) Wyświetl wszystkie rowery")
    print("2) Wyświetl dostępne rowery")
    print("3) Wypożycz rower")
    print("4) Oddaj rower")
    print("5) Wyświetl wszystkie numery")
    print("q) Wyjdź")
    Venom = input("Opcja nr : ")
    if Venom == '1':
					print(d4c)
   #elif Venom == '2':
   #    for key, value in rowery.items():
   #       print(f"Klucz: {key}, Wartość: {value}")
    elif Venom == '3':
            funny = input('Który rower chcesz wypożyczyć: ')
            d4c[funny]['dostepnosc'] = False
            print(d4c[funny])
    elif Venom == '4':
            funny2 = input('Który rower chcesz oddać: ')
            d4c[funny2]['dostepnosc'] = True
            print(d4c[funny2])
    elif Venom == '5':
      funny3 = input("Który rower wypożyczyłeś: ")
      liczba = int(input("Na ile go wypożyczyłeś: "))
      cena = d4c[funny3]["cena_za_godzine"]
      suma = cena*liczba
      print(suma)
    elif Snake == '6':
      max_cena = max(c["cena_za_godzine"] for c in d4c.values())
      min_cena = min(c["cena_za_godzine"] for c in d4c.values())
      print(F"\n\nNajwyższa cena roweru: {max_cena};\nNajniższa cena roweru: {min_cena}")

            