# Funktion zur Addition zweier Zahlen
from audioop import add


def addition(a, b):
    return a + b # Rückgabe der Summe
def multiplikation(a, b):
    return a * b
def subtraktion(a, b):
    return a - b
def division(a, b):
    return a / b

# Eingabe von zwei Zahlen durch den Benutzer und Rechenweg-Auswahl
eingabe = input("Welche Rechenoperation möchten Sie wählen?\n1) Addition\n2) Subtraktion\n3)Multiplikation\n4) Subtraktion\n5) Exit")
a = int(input("Gib die erste Zahl ein: "))
b = int(input("Gib die zweite Zahl ein: "))

if(b == 0 and eingabe == "4"):
    print("Fehler. b kann nicht 0 sein")
    b = int(input("Gib erneut eine zweite Zahl ein: "))
    print("Ergebnis:", division(a, b))

match(eingabe):
    case "1":
        print("Ergebnis:", addition(a, b))
    case "2":
        print("Ergebnis:", subtraktion(a, b))
    case "3":
        print("Ergebnis:", multiplikation(a, b))
    case "4":
        print("Ergebnis:", division(a, b))
    case "5":
        print("exit")



