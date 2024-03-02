# autor Piotr Siedlak
# numer albumu 12460

import datetime
import calendar
import math

name = input("Podaj imię: ")
age = int(input("Podaj ile masz lat: "))
print("Cześć "+ name +"!")
print("Twoje imię ma " + str((len(name))) + " liter i zaczyna się od " + name[0])
print("Teraz masz " + str(age) + "lat, a za rok będzie to " + str(age+1) + ". Rok urodzenia to : " + str(datetime.datetime.now().year-age))

age = 12#int(input("Podaj ile masz lat: "))
money = 10#int(input("Podaj ile masz siana: "))
if (age >= 18) and (money >= 20):
    print("Jesteś pełnoletni i masz wystarczającą ilość pieniędz")
elif (age >= 18) and (money < 20):
    print("Brakuje Ci " + str(20-money) + " zł")
elif (age < 18) and (money >= 20):
    print("Brakuje Ci " + str(18-age) + " lat do pełnoletności.")
else:
    print("Brakuje Ci " + str(20-money) + " zł oraz "+ str(18-age) + " lat do pełnoletności.")


is_yearly = input("Podaj sposób podawania dochodu roczny (R) albo miesięczny (M): ")
if is_yearly.upper() == "R":
    is_yearly = True
else:
    is_yearly = False

income = int(input("Podaj dochód brutto: "))

if not is_yearly:
    income *= 12

tax_bracket = 120000
if(income <= 120000):
    print(f"Jesteś w pierwszym progu podatkowym. Twój podatek do zapłacenia to: {0.12*income} zł")
else:
    tax_to_pay = 0.12*120000 + 0.32*(income - 120000)
    print(f"Jesteś w drugim progu podatkowym. Twój podatek do zapłacenia to: {tax_to_pay} zł")
    

type_of_shape = input("Podaj nazwę figury (prostokąt / trójkąt / koło: ")
if type_of_shape == "prostokąt":
    side_len1 = float(input("Podaj długość jednego boku: "))
    side_len2 = float(input("Podaj długość drugiego boku: "))
    if side_len1 >0 and side_len2:
        print(f"Pole prostokąta wynosi {side_len1*side_len2:.2f}")
    else:
        print("Długość nie może być mniejsza od zera!!!")
elif type_of_shape == "trójkąt":
    base_len = float(input("Podaj długość podstawy: "))
    height_len = float(input("Podaj długość wysokości: "))
    if base_len > 0 and height_len > 0:
        print(f"Pole trójkąta wynosi {0.5*base_len*height_len:.2f}")
    else:
        print("Długość nie może być mniejsza od zera!!!")
elif type_of_shape == "koło":
    diameter_len = float(input("Podaj długość średnicy: "))
    if diameter_len > 0:
        print(f"Pole koła wynosi {math.pi*((0.5*diameter_len)**2):.2f}")
    else:
        print("Długość nie może być mniejsza od zera!!!")
        
expensess = {"January" : 1200, "February" : 1500, "March" : 1000, "April" : 1900, "May" : 1800, "June" : 2000, "July" : 1600, "August" : 1500, "September" : 1700, "October" : 1800, "November" : 1500, "December" : 2200}
print(f"Wartość minimalna wydatków to: {min(expensess.values())} zł")
print(f"Wartość maksymalna wydatków to: {max(expensess.values())} zł")
print(f"Suma wydatków to: {sum(expensess.values())} zł")
average_expensess = sum(expensess.values())/12
print(f"Średnia wydatków to: {average_expensess:.2f} zł")

if expensess[calendar.month_name[datetime.datetime.now().month]] > average_expensess:
    print("W tym miesiącu zacznij oszczędzać!\n")
else:
    print("W tym miesiącu jesteś bezpieczny\n")

for month_to_be_listed, amount_to_be_listed in expensess.items():
    if(amount_to_be_listed > average_expensess):
        print(f"{month_to_be_listed} -> {amount_to_be_listed} zł")
