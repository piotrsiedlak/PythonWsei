# autor Piotr Siedlak
# numer albumu 12460

import datetime
import calendar
""" name = "Piotr" #input("Podaj imię: ")
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

""" is_yearly = input("Podaj sposób podawania dochodu roczny (R) albo miesięczny (M): ")
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
    print(f"Jesteś w drugim progu podatkowym. Twój podatek do zapłacenia to: {tax_to_pay} zł") """
    

# Napisz prosty program do obliczania pola figur geometrycznych. Użytkownik proszony jest o podanie nazwy figury w formie stringa (np. “prostokąt”, “trójkąt”, “koło” itd. - wersja 
# polska lub angielska), następnie w zależności od wybranej figury musi podać parametry - bok, średnica, wysokość itp. Przed obliczeniami wartości muszą być sprawdzone (np. > 0). 
# Po wpisaniu wszystkich wartości program wyświetla pole figury w formie pełnej odpowiedzi (np. “Pole figury <wybrana_figura> wynosi: <pole>”). Zadbaj o odpowiednie nazwy 
# zmiennych (po angielsku!) oraz rzutowanie typów. 
# UWAGA: Program wydaje się “szkolny”, ale będziemy do niego wielokrotnie wracać - przy pętlach dodamy do niego ponowne proszenie o podanie liczby, potem przeniesiemy
# obliczenia do funkcji, dodamy obsługę wyjątków, napiszemy to z wykorzystaniem OOP, a chętni mogą nawet podpiąć Turtle i narysować te figury. Ale cierpliwości :-)
    

# Zdefiniuj słownik, którego wartościami będą wydatki na życie w ostatnich kilku miesiącach, a kluczami nazwy miesięcy. Wyznacz i wyświetl wartość minimalną, maksymalną, sumę i 
# wartość średnią (wykonaj odpowiednie operacje na liście wartości). Sprawdź czy kwota za ostatni miesiąc przekracza wartość średnią - jeśli tak, to wyświetl tekst ostrzeżenia 
# “zacznij oszczędzać”, a jeśli nie, informację “jesteś bezpieczny”. Używając pętli wyświetl elementy słownika, każdy w innej linii, ale tylko jeśli przekraczają wartość średnią.
    
expensess = {"January" : 1200, "February" : 1500, "March" : 1000, "April" : 1900, "May" : 1800, "June" : 2000, "July" : 1600, "August" : 1500, "September" : 1700, "October" : 1800, "November" : 1500, "December" : 2200}
print(f"Wartość minimalna wydatków to: {min(expensess.values())} zł")
print(f"Wartość maksymalna wydatków to: {max(expensess.values())} zł")
print(f"Suma wydatków to: {sum(expensess.values())} zł")
average_expensess = sum(expensess.values())/12
print(f"Średnia wydatków to: {average_expensess:.2f} zł")

if expensess[calendar.month_name[datetime.datetime.now().month]] > average_expensess:
    print("Zacznij oszczędzać!")
else:
    print("Jesteś bezpieczny")


