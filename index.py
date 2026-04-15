d4c = {
    "Jedzenie": {
        "bułka": 30,
        "czteropak": 30,
        "liżme" : 20
    },
    "Picie": {
        "Sok": 45,
        "Cola": 25,
        "Alkochol" : 24
    }
}


while(True):
    print("> Dinozaur :*")
    print("> Wybierz opcje")
    print("1) Dodaj produkt")
    print("2) Usuń produkt")
    print("3) Sprawdź dostępność produktu")
    print("4) Wyświetl wszystkie produkty")
    print("q) Wyjdź")
    Venom = input("Opcja nr : ")
    if Venom == '1':
        xd = input("Do której kategorii dodać: ")
        klucz = input("Wprowadź co dodać jako produkt: ")
        value = int(input("Wprowadź ile produktów dodać: "))
        d4c[xd][klucz] = value
        print(d4c)
    elif Venom == '2':
        xd2 = input("Z jakiej kategorii usunąć: ")
        klucz2 = input("Wprowadź co usunąć: ")
        del d4c[xd2][klucz2]
        print(d4c)
        
    elif Venom == '3':
        xd3 = input("Jaką kategorie chcesz zobaczyć?: ")
        klucz3 = input("Wprowadź co wyświetlić: ")
        print(d4c[xd3][klucz3])
        
    elif Venom == '4':
        xd4 = input("Jaką kategorie chcesz zobaczyć?: ")
        d4c[xd4]
        print(d4c)
    
    elif Venom == "q":
        break