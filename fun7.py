def connect(**opcje):  # ** - argumenty słownikowe, nazwane
    print(opcje)
    conect_param = {
        'host': '127.0.0.7',
        'port': '8080'
    }
    conect_param['pwd'] = opcje
    print(conect_param)  # {'host': '127.0.0.7', 'port': '8080', 'pwd': {'a': 7}}


def all_args(*args, **kwargs):
    print(args, kwargs)


connect()  # {} słownik para klucz wartosc
connect(a=7)  # {'a': 7}
connect(name="Radek")  # {'name': 'Radek'}
connect(a=7, b=9, name="Radek")  # {'a': 7, 'b': 9, 'name': 'Radek'}
connect(a=None)

all_args()
all_args(1, 2, 3)
all_args(a=1, b=2, c=3)
all_args(1, 2, 3, 4, b=2, c=3)
# all_args(a=1, 2)  # SyntaxError: positional argument follows keyword argument
all_args(None)  # (None,) {}
