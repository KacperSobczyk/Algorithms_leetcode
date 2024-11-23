"""
Napisz dekorator cache, który będzie pamiętał wyniki wcześniejszych wywołań funkcji i zwracał zapamiętany wynik,
jeśli funkcja zostanie wywołana z tymi samymi argumentami.
Jeśli wynik nie istnieje w pamięci podręcznej, funkcja powinna zostać wykonana, a wynik zapisany w cache.

"""
def cache(fun):
    schowek = {}
    def operacja(liczba):
        nonlocal schowek
        if liczba not in schowek:
            wartosc = fun(liczba)
            schowek[liczba] = wartosc
            print("Wartość wywolana pierwszy raz:")
            return wartosc
        else:
            print("Wartość ze schowka:")
            return schowek[liczba]
    return operacja

@cache
def czy_parzysta(num):
    return num % 2 == 0

if __name__ == "__main__":
    for i in range(10):
        print(czy_parzysta(i))
    for i in range(1,10,2):
        print(czy_parzysta(i))



