#Erstellen Sie ein Tupel, das 3 unterschiedliche Datentypen als Eintra ̈ge hat. Ent- packen Sie den ersten Eintrag in eine Variable x und die restlichen beiden in eine Liste l. Fu ̈gen sie nun x als letztes Element der Liste l hinzu und kehren sie Rei- henfolge der Liste um. Fu ̈hren Sie nun den fehlenden Schritt aus um die Elemente der Liste in dieselbe Reihenfolge wie des Originaltupels zu bringen. Uberpru ̈fen Sie nun mit einer for Schleife, dass die Reihenfolge der Elemente im Tupel und der Liste tatsa ̈chlich u ̈bereinstimmen; falls nicht, soll eine Fehlermeldung ausgegeben werden. (4 Punkte)

integer = int(input('gib eine Zahl ein: '))
string = str(input('gib jetzt noch Text ein: '))
bool = bool(input('gib irgendwas ein, das ist die boolean value Eingabe: '))
tupel = (integer,string,bool)


x = tupel[0]
#output: 3

l = list(tupel[1:3])
#output: ['i', False]

l.append(x)
l.reverse()
#Reihenfolge der Liste: integer, bool, string
l[1],l[2] = l[2],l[1]

print('nun deine ursprugliche Liste nach allen Monipulationen: ',l)

#Wir überprüfen jetzt, die input und output Listen tatsächlich übereinstimmen 

for i in tupel_np:
	for o in l_np:
		print(i)
		if i+o == o+i:
			print('die beiden Listen sind tatsächlich identisch')
		else:
			raise Exception('irgendwas stimmt im Script nicht')
			
