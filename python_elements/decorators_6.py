"""
Napisz dekorator sprawdz_typy, który przyjmuje jako parametry oczekiwane typy argumentów funkcji (w formie tupli)
 oraz typ zwracanej wartości.
Jeśli którykolwiek argument lub wartość zwracana przez funkcję nie zgadza się z oczekiwanym typem,
 dekorator powinien rzucić wyjątek TypeError.
"""
def sprawdz_typy(arguments, results):
    def decorator(fun):
        def operacja(*args):         
            if len(args) != len(arguments):
                raise(TypeError("The number of input arguments is different than declared"))
            for i,arg in enumerate(args):
                if not isinstance(arg,arguments[i]):
                    raise(TypeError(f"Argument {i} should be of type {arguments[i].__name__}"))
            result = fun(*args)
            if type(result) != results:
                raise(TypeError(f"The output type is different than declared"))
            return result
        return operacja
    return decorator

@sprawdz_typy((int,int,int),int)
def funkcja_dodania(*args):
    suma = 0
    for arg in args:
       suma += arg
    return suma

if __name__ == "__main__":
    print(funkcja_dodania(3,5,7))
    try:
        print(funkcja_dodania(4, 1))
    except TypeError as e:
        print(e)
    try:
        print(funkcja_dodania(4,1,2.5))
    except TypeError as e:
        print(e)