def printList():
    print("WYBIERZ DACHÓWKE:")
    print("===================================")
    print("||           1. Simpla           ||")
    print("===================================")
    print("||           2. Titania          ||")
    print("===================================")
    print("||           3. Premion          ||")
    print("===================================")
    print("||           4. Domino           ||")
    print("===================================")
    print("||           5. Futura           ||")
    print("===================================")
    print("|| 6. GOTEBORG/HEIDELBERG/VERONA ||")
    print("===================================")
    print("||           7. Harmonic        ||")
    print("===================================")


def calculate(min, max, height):
    for i in range(1, 100):
        result = height / i
        if result > min and result < max:
            print(f"Łacisz na {result} cm, liczba łat to {i}")


def calculate1(min, max, height):
    for i in range(1, 100):
        result = height / i
        if result > min and result < max:
            print(
                f"Obcinka: {height} cm, liczba łat: {i}, wymiar łacenia: {result}cm\n")


def welcome():
    print("===================================")
    print("|| PROGRAM DO OBLICZANIA ŁACENIA ||")
    print("===================================")
    print("\nCo chcesz zrobić ? : ")
    print("===================================")
    print("||     1. Obliczyć łacenie       ||")
    print("===================================")


def ObliczanieLacenia():
    printList()
    while True:
        try:
            choice = int(input(f"\nWybierz model 1-7 >>> "))
            print("===================================")
        except:
            print("Wybierz poprawny numer")
        else:
            if choice == 0 or choice > 7:
                print("Wybierz poprawny numer modelu")
            else:
                break
    while True:
        try:
            height = float(input("Podaj wysokość dachu (cm) >>> "))
            print("===================================")
        except:
            print("Podaj liczbę")
        else:
            break
    while True:
        try:
            isTrue = str(
                input("Czy dach jest równy z obydwu stron ? t/n >>> "))
            print("===================================")
        except:
            print("\nWpisz t lub n")
        else:
            if isTrue == "t" or isTrue == "n":
                break
            else:
                print("Wpisz t lub n")

    if isTrue == "n":
        while True:
            try:
                second_height = float(
                    input("Podaj wysokość drugiej strony (cm) >>> "))
                print("===================================")
            except:
                print("Podaj liczbę")
            else:
                break
        if choice == 1:
            print(f"\nSIMPLA: ")
            print(f"\n============= ")
            min = 33.8
            max = 36.6
            print(f"Jej przedział to: {min}cm - {max}cm\n")
            print("===================================")
            print(f"WYMIARY PIERWSZEJ STRONY: ")
            calculate(min, max, height)
            print("===================================")
            print(f"WYMIARY DRUGIEJ STRONY: ")
            calculate(min, max, second_height)
            print("===================================")

        elif choice == 2:
            print(f"\nTITANIA: ")
            print("===================================")
            min = 38.2
            max = 42.5
            print(f"Jej przedział to: {min}cm - {max}cm\n")
            print("===================================")
            print(f"WYMIARY PIERWSZEJ STRONY: ")
            calculate(min, max, height)
            print("===================================")
            print(f"WYMIARY DRUGIEJ STRONY: ")
            calculate(min, max, second_height)
            print("===================================")
        elif choice == 3:
            print(f"\nPREMION: ")
            print("===================================")
            min = 35.7
            max = 37.9
            print(f"Jej przedział to: {min}cm - {max}cm\n")
            print("===================================")
            print(f"WYMIARY PIERWSZEJ STRONY: ")
            calculate(min, max, height)
            print("===================================")
            print(f"WYMIARY DRUGIEJ STRONY: ")
            calculate(min, max, second_height)
            print("===================================")
        elif choice == 4:
            print(f"\nDOMINO: ")
            print("===================================")
            min = 34.3
            max = 35.4
            print(f"Jej przedział to: {min}cm - {max}cm\n")
            print("===================================")
            print(f"WYMIARY PIERWSZEJ STRONY: ")
            calculate(min, max, height)
            print("===================================")
            print(f"WYMIARY DRUGIEJ STRONY: ")
            calculate(min, max, second_height)
            print("===================================")
        elif choice == 5:
            print(f"\nFUTURA: ")
            print("===================================")
            min = 36
            max = 38.8
            print(f"Jej przedział to: {min}cm - {max}cm\n")
            print("===================================")
            print(f"WYMIARY PIERWSZEJ STRONY: ")
            calculate(min, max, height)
            print("===================================")
            print(f"WYMIARY DRUGIEJ STRONY: ")
            calculate(min, max, second_height)
            print("===================================")
        elif choice == 6:
            print(f"\nGOTEBORG/HEIDELBERG/VERONA: ")
            print("===================================")
            min = 31
            max = 34
            print(f"Jej przedział to: {min}cm - {max}cm\n")
            print("===================================")
            print(f"WYMIARY PIERWSZEJ STRONY: ")
            calculate(min, max, height)
            print("===================================")
            print(f"WYMIARY DRUGIEJ STRONY: ")
            calculate(min, max, second_height)
            print("===================================")
        elif choice == 7:
            print(f"\nHARMONICA: ")
            print("===================================")
            min = 36.4
            max = 37.5
            print(f"Jej przedział to: {min}cm - {max}cm\n")
            print("===================================")
            print(f"WYMIARY PIERWSZEJ STRONY: ")
            calculate(min, max, height)
            print("===================================")
            print(f"WYMIARY DRUGIEJ STRONY: ")
            calculate(min, max, second_height)
            print("===================================")

    elif isTrue == "t":
        if choice == 1:
            print(f"\nSIMPLA: ")
            print("===================================")
            min = 33.8
            max = 36.6
            print(f"Jej przedział to: {min}cm - {max}cm\n")
            print("===================================")
            print(f" WYMIARY: ")
            calculate(min, max, height)
            print("===================================")

        elif choice == 2:
            print(f"\nTITANIA: ")
            print("===================================")
            min = 38.2
            max = 42.5
            print(f"Jej przedział to: {min}cm - {max}cm\n")
            print("===================================")
            print(f" WYMIARY: ")
            calculate(min, max, height)
            print("===================================")
        elif choice == 3:
            print(f"\nPREMION: ")
            print("===================================")
            min = 35.7
            max = 37.9
            print(f"Jej przedział to: {min}cm - {max}cm\n")
            print("===================================")
            print(f" WYMIARY: ")
            calculate(min, max, height)
            print("===================================")
        elif choice == 4:
            print(f"\nDOMINO: ")
            print("===================================")
            min = 34.3
            max = 35.4
            print(f"Jej przedział to: {min}cm - {max}cm\n")
            print("===================================")
            print(f" WYMIARY: ")
            calculate(min, max, height)
            print("===================================")
        elif choice == 5:
            print(f"\nFUTURA: ")
            print("===================================")
            min = 36
            max = 38.8
            print(f"Jej przedział to: {min}cm - {max}cm\n")
            print("===================================")
            print(f" WYMIARY: ")
            calculate(min, max, height)
            print("===================================")
        elif choice == 6:
            print(f"\nGOTEBORG/HEIDELBERG/VERONA: ")
            print("===================================")
            min = 31
            max = 34
            print(f"Jej przedział to: {min}cm - {max}cm\n")
            print("===================================")
            print(f" WYMIARY: ")
            calculate(min, max, height)
            print("===================================")
        elif choice == 7:
            print(f"\nHARMONICA: ")
            print("===================================")
            min = 36.4
            max = 37.5
            print(f"Jej przedział to: {min}cm - {max}cm\n")
            print("===================================")
            print(f" WYMIARY: ")
            calculate(min, max, height)
            print("===================================")
        else:
            print("Złe wprowadzenie")


welcome()

while True:
    try:
        first_choice = int(input(">>> "))
        if first_choice > 1 or first_choice < 1:
            print("Wpisz poprawny numer")
    except:
        print("Wpisz liczbę")
    else:
        if first_choice == 1:
            ObliczanieLacenia()
            break
