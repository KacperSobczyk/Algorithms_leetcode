"""
Napisz dekorator limituj_wywolania, który pozwala funkcji być wywołaną tylko określoną liczbę razy.
Jeśli liczba wywołań zostanie przekroczona, dekorator wyświetli komunikat:
Funkcja <nazwa_funkcji> została wywołana zbyt wiele razy!.

Dekorator powinien przyjmować jako parametr maksymalną liczbę dozwolonych wywołań.
"""
def limituj_wywolania(limit: int):
    def decorator(fun):
        iterator = 0
        def wywolaj():
            nonlocal iterator
            if iterator < limit:
                fun()
                iterator += 1
            else:
                print(f"Funkcja {fun.__name__} została wywołana zbyt wiele razy!")
        return wywolaj
    return decorator
        
@limituj_wywolania(4)
def przywitaj():
    print("Cześć")


if __name__ == "__main__":
    for i in range(10):
        przywitaj()
        