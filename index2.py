ligma = {
    "bułka": 30,
    "czteropak": 30,
    "liżme" : 20
}   


while(True):
    print("> Happy Lista :D")
    print("> Wybierz opcje")
    print("1) Dodaj produkt")
    print("2) Usuń produkt")
    print("3) Wyświetl wszystkie produkty")
    print("q) Wyjdź")
    Venom = input("Opcja nr : ")
    if Venom == '1':
        klucz = input("Wprowadź co dodać jako produkt: ")
        value = int(input("Wprowadź ile produktów dodać: "))
        ligma[klucz] = value
        print(ligma)

    elif Venom == '2':
        klucz2 = input("Wprowadź co usunąć: ")
        del ligma[klucz2]
        print(ligma)
   
    elif Venom == '3':
        print(ligma)
    
    elif Venom == "q":
        break