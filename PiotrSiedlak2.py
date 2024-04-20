# autor Piotr Siedlak
# numer albumu 12460



#zadanie2
import math

def square(side_len1, side_len2):
    return round(side_len1*side_len2, 2)

def triangle(base_len, height_len):
    return round(0.5*base_len*height_len, 2)

def circle(diameter_len):
    radius = diameter_len / 2
    area = math.pi * (radius ** 2)
    return round(area, 2)

def get_float(argument):
    while True:
        value = float(input(argument))
        if value > 0:
            return value
        else:
            print("Błędna wartość")

while True:
    type_of_shape = input("Podaj nazwę figury (prostokąt / trójkąt / koło / stop): ")
    if type_of_shape == "prostokąt":
        side_len1 = get_float("Podaj długość jednego boku: ")
        side_len2 = get_float("Podaj długość drugiego boku: ")
        print(f"Pole prostokąta wynosi {square(side_len1,side_len2)}")
    elif type_of_shape == "trójkąt":
        base_len = get_float("Podaj długość podstawy: ")
        height_len = get_float("Podaj długość wysokości: ")
        print(f"Pole trójkąta wynosi  {triangle(base_len, height_len)}")
    elif type_of_shape == "koło":
        diameter_len = get_float("Podaj długość średnicy: ")
        print(f"Pole koła wynosi {circle(diameter_len)}")
    elif type_of_shape == "stop":
        break


