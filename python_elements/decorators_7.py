"""
Napisz dekorator loguj_do_pliku, który zapisuje szczegóły każdego wywołania funkcji do pliku log.txt.
Szczegóły powinny zawierać:
* datę i godzinę wywołania,
* nazwę funkcji,
* argumenty funkcji,
* wynik funkcji.
"""
import datetime

def loguj_do_pliku(filename):
    def decorator(fun):
        def operacja(*args, **kwargs):
            result = fun(*args, **kwargs)
            with open(filename, 'a', encoding='utf-8') as file:
                if args:
                    inputs = ", ".join([str(arg) for arg in args])
                    file.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Wywołano: {fun.__name__}({inputs}) -> Wynik: {result}\n")
                else:
                    inputs = ", ".join([f"{key} = {value}" for key,value in kwargs.items()])
                    file.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Wywołano: {fun.__name__}({inputs}) -> Wynik: {result}\n")
            return result
        return operacja
    return decorator

@loguj_do_pliku("wyniki.log")
def add_elements(*args, **kwargs):
    if args:
        print("Suma dodawania: ", sum(args))
        return sum(args)
    else:
        print("Suma dodawania: ", sum(kwargs.values()))
        return sum(kwargs.values())

if __name__ == "__main__":
    add_elements()
    add_elements(3,4,5)
    add_elements(a=2.5,b=4,c=0.25)
