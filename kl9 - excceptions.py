class MyExeption(Exception):  # dziedziczymy po klasie Exception, tworzymy własny wyjątek
    def __init__(self, message):
        super().__init__(message)


try:
    # print(5 / 0)
    raise ZeroDivisionError("Nie dziel przez zero")  # rzucenie wyjątku
except ZeroDivisionError as e:
    print("Nie dziel przez zero", e)

x = 0
try:
    if x == 0:
        raise MyExeption("X nie może być 0")
except MyExeption as e:
    print("X nie może być 0", e)
# Nie dziel przez zero Nie dziel przez zero
# X nie może być 0 X nie może być 0
