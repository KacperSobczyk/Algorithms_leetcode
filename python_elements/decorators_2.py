import time
"""
Napisz dekorator sprawdz_czas, który mierzy czas wykonania funkcji i wyświetla komunikat:
Funkcja <nazwa_funkcji> wykonała się w czasie: <czas> sekund.
Użyj tego dekoratora do ozdobienia funkcji przetworz_liste,
która przyjmuje listę liczb i zwraca listę tych samych liczb podniesionych do kwadratu.
"""
def sprawdz_czas(fun):
    def transform_list(l):
        start_time = time.time()
        new_l = fun(l)
        end_time = time.time()
        print(f"Funkcja {fun.__name__} wykonała się w czasie: {round(end_time - start_time, 2)} sekund.")
        
        return new_l
    return transform_list

@sprawdz_czas
def square_power_list(lista):
    time.sleep(3)
    return [a*a for a in lista]

if __name__ == "__main__":
    power_list = square_power_list([2,5,8,3,11,7])
    print(power_list)