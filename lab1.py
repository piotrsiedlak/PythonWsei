# autor Piotr Siedlak
# numer albumu 12460

""" import datetime
name = "Piotr" #input("Podaj imię: ")
age = 30#int(input("Podaj ile masz lat: "))
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
 """

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
    tax_to_pay = 0.12*income
else:
    tax_to_pay = 0.32*income

