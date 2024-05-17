"""
 Sprawdza, czy podany numerek jest "szczęśliwy" i oferuje ponowną próbę.

 Argumenty:
   Brak argumentów (pobiera numerek od użytkownika).

 Zwraca:
   Nic (funkcja działa interaktywnie z użytkownikiem).
 """


def szczesliwy_numerek():
  while True:
    # Pobierz numerek od użytkownika
    numerek = input("Podaj 6 cyfr: ")
    while len(numerek) != 6 or not numerek.isdigit():  # Dopóki numerek jest niepoprawny
      print("Błędny format numerka. Wprowadź 6 cyfr.")
      numerek = input("Podaj 6 cyfr: ")  # Poproś o ponowne wprowadzenie

    # Podziel numerek na dwie części
    pierwsze_trzy_cyfry = numerek[:3]
    ostatnie_trzy_cyfry = numerek[3:]

    # Zamień cyfry na liczby
    suma_pierwszych_cyfr = sum(int(cyfra) for cyfra in pierwsze_trzy_cyfry)
    suma_ostatnich_cyfr = sum(int(cyfra) for cyfra in ostatnie_trzy_cyfry)

    # Porównaj sumy cyfr
    if suma_pierwszych_cyfr == suma_ostatnich_cyfr:
      wynik = "szczęśliwy"
    else:
      wynik = "zwykły"

    # Wyświetl numerek i wynik
    print(f"Numerek {numerek} jest {wynik}")

    # Zapytaj o ponowną próbę
    kolejna_proba = input("Czy chcesz sprawdzić kolejny numerek? (tak/nie): ")
    if kolejna_proba.lower() != "tak":
      break  # Zakończ pętlę, jeśli użytkownik nie chce dalej sprawdzać


# Wywołanie funkcji
szczesliwy_numerek()

'''



def szczesliwy_numerek():
  """
  Sprawdza, czy podany numerek jest "szczęśliwy" i wyświetla wynik.

  Argumenty:
    Brak argumentów (pobiera numerek od użytkownika).

  Zwraca:
    Nic (funkcja działa interaktywnie z użytkownikiem).
  """

  # Pobierz numerek od użytkownika
  while True:
    numerek = input("Podaj 6 cyfr: ")
    # Sprawdź poprawność formatu numerka
    if len(numerek) == 6 and numerek.isdigit():
      break  # Poprawny format
    else:
      print("Błędny format numerka. Wprowadź 6 cyfr.")

  # Podziel numerek na dwie części
  pierwsze_trzy_cyfry = numerek[:3]
  ostatnie_trzy_cyfry = numerek[3:]

  # Zamień cyfry na liczby (użycie `int()`)
  suma_pierwszych_cyfr = sum(int(cyfra) for cyfra in pierwsze_trzy_cyfry)
  suma_ostatnich_cyfr = sum(int(cyfra) for cyfra in ostatnie_trzy_cyfry)

  # Porównaj sumy cyfr
  if suma_pierwszych_cyfr == suma_ostatnich_cyfr:
    wynik = "szczęśliwy"
  else:
    wynik = "zwykły"

  # Wyświetl numerek i wynik
  print(f"Numerek {numerek} jest {wynik}")

# Wywołanie funkcji
szczesliwy_numerek()  # Pobierz numerek i sprawdź wynik '''
