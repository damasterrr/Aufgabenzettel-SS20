#Erstellen Sie ein Tupel, das 3 unterschiedliche Datentypen als Eintra ̈ge hat. Ent- packen Sie den ersten Eintrag in eine Variable x und die restlichen beiden in eine Liste l. Fu ̈gen sie nun x als letztes Element der Liste l hinzu und kehren sie Rei- henfolge der Liste um. Fu ̈hren Sie nun den fehlenden Schritt aus um die Elemente der Liste in dieselbe Reihenfolge wie des Originaltupels zu bringen. Uberpru ̈fen Sie nun mit einer for Schleife, dass die Reihenfolge der Elemente im Tupel und der Liste tatsa ̈chlich u ̈bereinstimmen; falls nicht, soll eine Fehlermeldung ausgegeben werden. (4 Punkte)

integer = int(input('gib eine Zahl ein: '))
string = str(input('gib jetzt noch Text ein: '))
bool = bool(input('gib irgendwas ein, das ist die boolean value Eingabe: '))
tupel = (integer,string,bool)

x = int(tupel[0])
#integer

liste = list(tupel[1:3])
#['string', bool]
liste.append(x)
liste.reverse()

#Reihenfolge der Liste: integer, bool, string. wir müssen also [1] mit [2] wechseln

liste[1],liste[2] = liste[2],liste[1]

print('nun deine ursprugliche Liste nach allen Monipulationen: ',liste)

#Wir überprüfen jetzt, die input und output Listen tatsächlich übereinstimmen 
for t in tupel:
	if tupel.index(t) == liste.index(t):
		print("alles ist gut, die beiden Listen sind identisch")
	else:
		raise TypeError("irgendwas ist im Script falsch")
			
