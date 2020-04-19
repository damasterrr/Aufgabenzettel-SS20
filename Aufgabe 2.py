#Lassen Sie den Benutzer eine beliebige Zahl bis 100 einlesen und wandeln sie diese in bina ̈re und oktale Darstellung um. Fassen Sie nun diese Darstellung als 2 neue Dezimalzahlen auf und geben Sie diese aus. Fu ̈hren Sie nun mindestens 4 Ihnen bekannte bin ̈are Rechenoperationen mit diesen beiden Zahlen aus und geben Sie diese aus. (3 Punkte)
print(bin(5))
eingabe = int(input('gib eine Zahl von 1 bis 100 ein: '))
bin_wert = bin(eingabe)
oct_wert = oct(eingabe)
print('deine Zahl in binärer Darstellung: ', bin_wert[2:])
print('deine Zahl in oktaler Darstellung: ', oct_wert[2:])

#binäre Rechneoperationen
b = int(bin_wert[2:])
o = int(oct_wert[2:])
addition = b + o
subtraktion = b - o
multiplikation = b * o
division = b / o

print(addition, subtraktion, multiplikation, division)
#alles funktioniert
