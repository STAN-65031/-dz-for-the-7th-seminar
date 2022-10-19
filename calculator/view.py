
def view_data(data, title):
    print(f'{title} = {data}')

def get_value(number_type):
    if number_type == "whole":
        okey = False
        while not okey:
            try:
                number = int(input("Введите число: "))
                okey = True
            except ValueError:
                print("Какое-то неправильное число!")
            return number
    elif number_type == "fractional":
        okey = False
        while not okey:
            try:
                number = float(input("Введите число: "))
                okey = True
            except ValueError:
                print("Какое-то неправильное число!")
            return number
    elif number_type == "rational":
        def input_numbers(inputText):
            okey = False
            while not okey:
                try:
                    number = int(input(f"{inputText}"))
                    okey = True
                except ValueError:
                    print("Какое-то неправильное число!")
            return number
        num1 = input_numbers(f"Введите 1 число комплексного числа: ")
        num2 = input_numbers(f"Введите 2 число комплексного числа: ")
        number = complex(num1, num2)
        return number
