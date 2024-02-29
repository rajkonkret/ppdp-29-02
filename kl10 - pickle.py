import pickle

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

with open("lista.txt", "w") as f:
    f.write(str(lista))

with open("lista.txt", "r") as f:
    dane = f.read()

print(dane)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(dane))  # <class 'str'>
print(dane[0])  # [
print(dane.split())  # ]['[1,', '2,', '3,', '4,', '5,', '6,', '7,', '8,', '9]']
print(dane.split(","))  # ['[1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9]']

with open("lista.pickle", "wb") as f:
    pickle.dump(lista, f)

with open("lista.pickle", "rb") as f:
    loaded_list = pickle.load(f)

print(loaded_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(loaded_list))  # <class 'list'>
print(loaded_list[0])  # 1

# serializacja pickle
ser_lista = pickle.dumps(lista)
print(ser_lista)
# b'\x80\x04\x95\x17\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03K\x04K\x05K\x06K\x07K\x08K\te.'

# deserializacja pickle
print(pickle.loads(ser_lista))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
