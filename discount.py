from datetime import date, timedelta, datetime

today = date.today()
print(today)  # 2024-02-27
print(type(today))  # <class 'datetime.date'>

time = datetime.now()
print(time)  # 2024-02-27 12:36:03.054250

# tomorrow = today + 1  # TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
# days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0):
tomorrow = today + timedelta(days=1)
print(tomorrow)  # 2024-02-28

print(time.time())
print(today.day)  # 27

formatted_date = datetime.now().strftime('%d/%m/%Y')
print(formatted_date)  # 27/02/2024

formated_time = datetime.now().strftime('%H:%M')
print(formated_time)  # 12:40

products = [
    {'sku': 1, 'exp_date': today, 'price': 100.0},
    {'sku': 2, 'exp_date': today, 'price': 80.0},
    {'sku': 3, 'exp_date': tomorrow, 'price': 200},
    {'sku': 4, 'exp_date': today, 'price': 500.00},
]
# print(products)

for p in products:
    # print(p)  # {'sku': 1, 'exp_date': datetime.date(2024, 2, 27), 'price': 100.0}
    if p['exp_date'] != today:
        continue  # weź kolejny element z listy
    p['price'] *= 0.8
    print(f"""
Price for sku {p['sku']}
is now {p['price']}
""")

# Price for sku 1
# is now 80.0
#
#
# Price for sku 2
# is now 64.0
#
#
# Price for sku 4
# is now 400.0
# 13:30