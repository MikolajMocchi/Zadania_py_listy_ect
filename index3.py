d4c = {
    "K": {
        "numer1": 101010101,
        "numer2": 101010101,
        "numer3": 101010101
    },
    "M": {
        "numer4": 101010101,
        "numer5": 101010101,
        "numer6": 101010101
    }
}


while(True):
    print("> There's is six")
    print("> Wybierz opcje")
    print("1) Podaj numer który chcesz zapisać")
    print("2) Usuń osobe z egzystencji")
    print("3) Sprawdź dostępność numeru")
    print("4) Wyświetl wszystkie numery")
    print("q) Wyjdź")
    Venom = input("Opcja nr : ")
    if Venom == '1':
        xd = input("Jaką płeć chcesz dodać (K=Kobieta, M=Mężczyzna): ")
        klucz = input("Podaj imie osobt: ")
        value = int(input("Podaj numer osoby: "))
        d4c[xd][klucz] = value
        print(d4c)
     
    elif Venom == '2':
        xd2 = input("Jaką płeć chcesz usunąć (K=Kobieta, M=Mężczyzna): ")
        klucz2 = input("Wprowadź imie osoby którą chcesz usunąć: ")
        del d4c[xd2][klucz2]
        print(d4c)
      
    elif Venom == '3':
        xd3 = input("Jaką płeć zobaczyć (K=Kobieta, M=Mężczyzna): ")
        klucz3 = input("Wprowadź imie osoby którą chcesz zobaczyć wyświetlić: ")
        print(d4c[xd3][klucz3])
       
    elif Venom == '4':
        xd4 = input("Jaką płeć chcesz zobaczyć? (K=Kobieta, M=Mężczyzna): ")
        d4c[xd4]
        print(d4c)
     
    elif Venom == "q":
        break