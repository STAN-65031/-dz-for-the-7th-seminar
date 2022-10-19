from datetime import datetime

def logg_in():
    current_datetime = datetime.now().date()
    print("Как тебя зовут?!")
    name = input()
    print(f"Привет {name}")
    print(f"{name}, сейчас {current_datetime}")