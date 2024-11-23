"""
Napisz dekorator powitanie, który przed wywołaniem funkcji wyświetli komunikat "Witaj!" oraz "Miło cię widzieć!".
Użyj tego dekoratora do ozdobienia funkcji przywitaj,
która przyjmuje imię i wyświetla Cześć, <imię>!.

"""
def powitanie(fun):
    def welcome(name):
        print("Witaj!")
        print("Miło cię widzieć!")
        fun(name)
    return welcome

@powitanie
def display_name(disp_name):
    print(f"Cześć {disp_name}!")

if __name__ == "__main__":
    display_name("Kacper")
