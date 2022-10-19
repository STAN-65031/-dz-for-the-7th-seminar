import  menu as s
import view
import logg

def button_click():
    logg.logg_in()
    print()
    number_type = s.number_selection_menu()
    print()
    value_a = view.get_value(number_type)
    value_b = view.get_value(number_type)
    print()
    result = s.grid(value_a, value_b)
    print()
    view.view_data(result, "resul ")