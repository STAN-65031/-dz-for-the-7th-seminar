import model_sum as s1
import model_dif as s2
import model_multi as s3
import model_division as s4
import model_remainder_of_division as s5
import model_pow as s6
import model_integer_division as s7


def number_selection_menu ():
    while True:
        print("Введите 0 что бы закрыть")
        print("Введите 1 что бы выбрать целые числа")
        print("Введите 2 что бы выбрать рациональные числа")
        print("Введите 3 что бы выбрать комлексные числа")
        def input_numbers(inputText):
            okey = False
            while not okey:
                try:
                    number = int(input(f"{inputText}"))
                    okey = True
                    if 0 > number < 4:
                        okey = False
                        print("'это число не подходит")
                except ValueError:
                    print("Какое-то неправильное число!")
            return number

        s = input_numbers("Выберите действие: ")
        if s == 0:
            break
        if s == 1:
            return "whole"
        elif s == 2:
            return "fractional"
        elif s == 3:
            return "rational"




def grid (value_a, value_b, number_type):
    while True:
        print("Введите 0 что бы закрыть")
        print("Введите 1 что бы сложить")
        print("Введите 2 что бы вычесть")
        print("Введите 3 что бы умножить")
        print("Введите 4 что бы разделить")
        print("Введите 5 что бы узнать остаток от деления")
        print("Введите 6 что бы возвести в степень")
        print("Введите 7 что бы произвести целочисленное деление")
        def input_numbers(inputText):
            okey = False
            while not okey:
                try:
                    number = int(input(f"{inputText}"))
                    okey = True
                    if 0 > number < 8:
                        okey = False
                        print("'это число не подходит")
                except ValueError:
                    print("Какое-то неправильное число!")
            return number

        s = input_numbers("Выберите действие: ")
        if s == 0:
            break
        if s == 1:
            s1.init(value_a,value_b)
            return s1.do_it()
        elif s ==2:
            s2.init(value_a,value_b)
            return s2.do_it()
        elif s == 3:
            s3.init(value_a,value_b)
            return s3.do_it()
        elif s == 4:
            if value_b != 0:
                s4.init(value_a,value_b)
                return s4.do_it()
            else:
                print("Деление на ноль!")
        elif s == 5 and not number_type == "rational":
            s5.init(value_a,value_b)
            return s5.do_it()
        elif s == 6:
            s6.init(value_a,value_b)
            return s6.do_it()
        elif s == 7 and not number_type == "rational":
            s7.init(value_a,value_b)
            return s7.do_it()
        else:
            print("Неверный знак операции!")
            


