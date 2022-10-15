def view_data(data, title):
    print(f'{title} = {data}')

def get_value():
    okey = False
    while not okey:
        try:
            number = int(input("Введите число: "))
            okey = True
        except ValueError:
            print("Это не число!")
    return number