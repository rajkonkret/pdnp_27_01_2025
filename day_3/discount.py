from datetime import datetime, date, timedelta

today = date.today()
print("Dzisiejsza data:", today)  # Dzisiejsza data: 2025-01-29
print(type(today))  # <class 'datetime.date'>

time = datetime.now()
print("Aktualny czas:", time)  # Aktualny czas: 2025-01-29 13:34:18.474611

print(time.year)  # 2025
print(today.day)  # 29

# tommorow = today + 1 # TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
#  days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tommorow = today + timedelta(days=1)
print("Jutro będzie", tommorow)  # Jutro będzie 2025-01-30

formated_data = datetime.now().strftime("%d/%m/%Y")
print(type(formated_data))  # <class 'str'>
print("Data sformatowana:", formated_data)  # Data sformatowana: 29/01/2025

# sformatowany czas 13:40
formated_time = datetime.now().strftime("%H:%M")
print(type(formated_time))  # <class 'str'>
print("Sformatowany czas:", formated_time)  # Sformatowany czas: 13:43

formated_time_usa = datetime.now().strftime("%I:%M %p")
print("Sdformatowany czas 12h:", formated_time_usa)  # Sdformatowany czas 12h: 01:44 PM

products = [
    {"sku": 1, "exp_date": today, "price": 100},
    {"sku": 2, "exp_date": today, "price": 50},
    {"sku": 3, "exp_date": tommorow, "price": 200},
    {"sku": 4, "exp_date": today, "price": 100.99},
    {"sku": 5, "exp_date": tommorow, "price": 500},
    {"sku": 6, "exp_date": today, "price": 250},
]

for product in products:
    # print(product)
    # print(type(product))
    print(product['exp_date'])
    if product['exp_date'] != today:
        continue  # zakończy działąnie pętli, weźmie kolejny elelemnt z listy i uruchomi kolejne przejscie pętli
    product['price'] *= 0.8  # price = price * 0.8
    print(f"""Price for sku {product['sku']}
is now {product['price']}""")
