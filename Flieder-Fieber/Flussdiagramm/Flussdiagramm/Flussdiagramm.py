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

# Eingabe von zwei Zahlen durch den Benutzer
eingabe = input("Welche Rechenoperation möchten Sie wählen?\n1) Addition\n2) Subtraktion\n3)Multiplikation\n4) Subtraktion\n5) Exit")
a = int(input("Gib die erste Zahl ein: "))
b = int(input("Gib die zweite Zahl ein: "))

if(b == 0 and eingabe == "4"):
    print("Fehler. b kann nicht 0 sein")
    b = int(input("Gib erneut eine zweite Zahl ein: "))
else:
    match(eingabe):
        case "1":
            addition(a, b)
        case "2":
            subtraktion(a, b)
        case "3":
            multiplikation(a, b)
        case "4":
            division(a, b)
        case "5":
            print("exit")


# Aufruf der Funktion und Ausgabe des Ergebnisses
print("Ergebnis:", addition(a, b))