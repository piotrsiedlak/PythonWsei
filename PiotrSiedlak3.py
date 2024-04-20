# Katalog bazowy zawiera foldery o nazwach np. "wakacje", "zima", "wyjazd" itd.,
# które zawierają zdjęcia w formacie .jpg lub .png (rozszerzenie może być pisane dużymi lub małymi literami). 
# Napisz skrypt, który stworzy w katalogu bazowym nowy folder "kopie",
# następnie wylistuje zawartość każdego folderu (tylko pliki ze zdjęciami!) 
# i skopiuje pliki z każdego folderu do "kopie", nadając im nowe nazwy według wzorca: 
# NAZWAFOLDERU_NR (+.jpg/.png), gdzie NR to numer porządkowy zdjęcia w folderze liczony od 0.
#  Przygotuj też raport z operacji - zapisz w pliku txt nazwę każdego folderu 
#  z pełną ścieżką bezwzględną, a pod nim stare nazwy plików. 
#  Wykorzystaj wbudowane moduły os - do operacji na ścieżkach i nazwach plików
#    oraz shutil - do kopiowania

# autor Piotr Siedlak
# numer albumu 12460

# zadanie 1
import shutil
import os

os.makedirs("kopie", exist_ok=True)
with open("raport.txt", "w") as report_file:
    for folder in os.listdir():
        if os.path.isdir(folder):
            report_file.write(f"{os.path.abspath(folder)}\n")
            for file in os.listdir(folder):
                if file.split(".")[-1].lower() in ["jpg", "png"]:
                    shutil.copy(f"{folder}/{file}", f"kopie/{folder}_{os.listdir(folder).index(file)}.{file.split('.')[-1]}")
                    report_file.write(f"{os.path.abspath(file)}\n")