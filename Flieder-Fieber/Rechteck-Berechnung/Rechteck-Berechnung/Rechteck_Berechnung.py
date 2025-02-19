Erneut = True
while Erneut == True:
    


    x = float(input("Bitte geben Sie Ihr Mass einer Flächenseite ein:"))


    if(x <= 0):
        while x <=0:
            print("Zahl zu klein, bitte erneut eingeben:")
            x = float (input())



    y = float(input("Bitte geben Sie Ihr Mass einer Flächenseite ein:"))

    if(y <= 0):
        while y <=0:
            print("Zahl zu klein, bitte erneut eingeben:")
            y = float (input())



    def Flaechenberechnung(x, y):
        Ergebnis = x*y
        print("Ihre Fläche Beträgt:", Ergebnis)
        return Ergebnis


    Flaechenberechnung(x, y)


    
    eingabe = int (input("Möchten Sie eine erneute Berehnung vornehmen? 1. Ja 2. Nein"))
    if (eingabe == 1):
        Erneut = True
    elif(eingabe ==2):
        Erneut = False
        
    















