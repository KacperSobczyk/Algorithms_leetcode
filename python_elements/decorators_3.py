"""
Napisz dekorator sprawdz_uprawnienia, który sprawdzi, czy użytkownik ma odpowiednie uprawnienia do wywołania funkcji.

Funkcja przyjmuje argument uzytkownik, który jest słownikiem z kluczami nazwa i uprawnienia.
Dekorator powinien przyjmować listę wymaganych uprawnień jako parametr.
Jeśli użytkownik nie ma wszystkich wymaganych uprawnień, funkcja nie zostanie wywołana, a dekorator wyświetli komunikat: Brak uprawnień dla użytkownika <nazwa_uzytkownika>.

"""
def sprawdz_uprawnienia(uprawnienia: list):
    def decorator(fun):
        def operacja(user):
            for uprawnienie in user["uprawnienia"]:
                if uprawnienie in uprawnienia:
                    fun(user)
                    break
            else:
                print(f"Brak uprawnień dla użytkownika {user['nazwa']}")
        return operacja
    return decorator

@sprawdz_uprawnienia(["admin", "edytor"])
def usun_post(user: dict):
    print(f"Użytkownik {user['nazwa']} usunął post")

@sprawdz_uprawnienia(["admin", "edytor", "czytelnik"])
def kliknij_post(user):
    print(f"Uzytkownik {user['nazwa']} wyświetlił zawartość strony")

if __name__ == "__main__":
    jacek = {"nazwa": "Jacek", "uprawnienia": ["czytelnik"]}
    kliknij_post(jacek)
    usun_post(jacek)