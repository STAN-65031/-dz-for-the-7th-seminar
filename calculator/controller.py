import  menu as s
import view

def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    result = s.grid(value_a, value_b)
    view.view_data(result, "resul ")