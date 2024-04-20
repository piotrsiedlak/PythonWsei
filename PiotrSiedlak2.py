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


# zadanie 3
import calendar
def number_to_month(number):
    month_name = calendar.month_name[number]
    return month_name

def pesel_validate(pesel_list):

    control_sum = 0
    weights = [1,3,7,9,1,3,7,9,1,3]
    for number in range(len(weights)):
        control_sum = control_sum + ((weights[number]*pesel_list[number]) % 10)
    control_number = 10 - (control_sum % 10)
    if(control_number == pesel_list[-1]):
        return True
    else:
        return False


pesel = "66122464924"
pesel_tab = list(pesel)
pesel_num = []
for num in pesel_tab:
    pesel_num.append(int(num))

print(pesel_num)
day = pesel_num[4] * 10 + pesel_num[5]
month = pesel_num[2] * 10 + pesel_num[3]
year = pesel_num[0] * 10 + pesel_num[1]
if(month>20):
    year = year + 2000
    month = month - 20
else:
    year = year + 1900

print(f"Data: {day}-{number_to_month(month)}-{year}")

if(pesel_num[9] % 2 == 0):
    print("Kobieta")
else:
    print("Mezczyzna")

pesel_validate(pesel_num)


# zadanie 4 

def get_any_float(argument): 
    while True: 
        value = float(input(argument)) 
        return value 

a = get_float("Podaj liczbę a: ") 
b = get_float("Podaj liczbę b: ") 
c = get_float("Podaj liczbę c: ") 

def triangle_field(a,b,c): 
    if(a > 0 and b > 0 and c > 0): 
        half_length = 0.5*(a+b+c) 
        return pow((half_length*(half_length-a)*(half_length-b)*(half_length-c)),0.5) 
    else: 
        return -1 
result = triangle_field(a,b,c)
print(f"Pole trojkata wynosi: {result}") 


def square_root(a,b,c): 
    delta = (b*b)-(4*a*c) 
    print(delta) 
    if(delta<0): 
        return -1 
    else: 
        
        if(delta == 0): 
            return (-1*b)/(2*a) 
        else:
            sqrt_delta = math.sqrt(delta)  
            return ((-1*b)-sqrt_delta)/(2*a), ((-1*b)+sqrt_delta)/(2*a) 
         
#result = square_root(-4,2,-5) # brak rzeczywistych 
#result = square_root(2,4,2) # jedno rozw 
result = square_root(2,2,-12) # dwa rozw rzeczywiste 
print(result) 
if(result == -1): 
    print("Równanie nie ma rozwiązań rzeczywistych.") 
else: 
    print(f"Rozwiazaniami rownania kwadratowego jest/są: {result}") 


#zadanie 5
def print_triangle_iterative(height):
    for i in range(1, height + 1):
        print('*' * i)
print_triangle_iterative(4)

def print_triangle_recursive(height):
    if height > 0:
        print_triangle_recursive(height - 1)
        print('*' * height)
print_triangle_recursive(4)
