#Lassen Sie den Benutzer eine beliebige Zahl bis 100 einlesen und wandeln sie diese in bina ̈re und oktale Darstellung um. Fassen Sie nun diese Darstellung als 2 neue Dezimalzahlen auf und geben Sie diese aus. Fu ̈hren Sie nun mindestens 4 Ihnen bekannte bin ̈are Rechenoperationen mit diesen beiden Zahlen aus und geben Sie diese aus. (3 Punkte)
eingabe = int(input('gib eine Zahl von 1 bis 100 ein: '))
print('deine Zahl in binärer Darstellung: ',bin(eingabe))
print('deine Zahl in oktaler Darstellung: ',oct(eingabe))

#Die beiden Argumente wieder in die ursprungliche Form umwandeln

print('deine eingegebene Zahl wieder: ',int(bin(eingabe), base = 2))
