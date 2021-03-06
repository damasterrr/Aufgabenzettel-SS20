#Die folgende Exponentialfunktion beschreibt als Modell Vorg ̈ange in z.B. Natur, Technik oder Wirtschaft, die von einer geringen Ausgangsbasis explosionsartig und unbeschra ̈nkt anwachsen:
#B(t) = A · a^t
#A ist dabei ein gegebener Anfangsbestand, a die Zuwachsrate und I der Endbe- stand nach t Zeiteinheiten (z.B. Tagen). Schreiben Sie eine Funktion bestand(A, a, t), die das Ergebnis entsprechend der Gleichung berechnet und zuru ̈ckgibt (2 Punkte). Lo ̈sen Sie nun die folgenden Aufgaben:

#a. Welchen Endbestand gibt es fu ̈r A = 1000 bei einer Verdoppelung alle zwei Tage nach zwei Wochen? Geben Sie die Parameter und das Ergebnis am Bildschirm aus.(1 Punkte)
#b. Welchen Endzustand, wenn man die Verdoppelungsrate auf acht Tage reduzieren kann? Ausgabe wie vorher.(1 Punkte)
#c. Nehmen Sie die Daten wie in Aufgabe b an, ermitteln Sie jetzt aber die Bestandswerte mithilfe einer Schleife fu ̈r jeden Tag und geben Sie sie in zwei Spalten (Tag und Bestand) am Bildschirm aus. (2 Punkte)
#d. Verwenden Sie die Schleife von Aufgabec in einer neuenvFunktion bestandtab(A,T,t), wobei T die Verdoppelungsrate in Tagen ist. Das Ergebnis der Funktion soll eine Liste von Tupeln (Tag,Bestand) sein. Erzeugen Sie eine Tabelle fu ̈r 6 Wochen bei 500 Anfangsbestand und einer Verdoppelungsrate von 10 Tagen
#und geben Sie diese wiederum aus. (3 Punkte)
#Alle Ausgaben mu ̈ssen auf ganze Zahlen gerundet erfolgen; verwenden Sie dazu die interne Python-Funktion round(x). (insgesamt 9 Punkte)

#erster Teil der Aufgabe
def bestand(A, a, t):
	ergebnis = A * a**t
	return ergebnis

#a.
a_wert = bestand(1000,2,14/2) 
print('a. Bei A = 1000 umd einer Verdopplung alle zwei Tage hat man nach zwei Woche den Wert: ', int(a_wert), '', sep = '\n')

#b.
b_tage = 8
b_wert = bestand(1000,2,b_tage/2)
print('b. Wert bei einer Reduzierung auf 8 Tage: ',int(b_wert), '', sep ='\n')

#c.
print('c.')
c_tage = 0
while c_tage <= 8:
	c_wert = bestand(1000, 2, c_tage/2)
	c_tage = c_tage + 1
	print('Am ', c_tage, '. Tag ist der Wert: ', round(c_wert), sep = '')

#d. 
def bestandtab(A, T, t):
	while 
	ergebnistab = A * T ** t
	return ergebnistab
#neue Funktion mit Tupel. eher import pandas?



	
