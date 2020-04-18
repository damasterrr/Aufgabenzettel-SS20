#Erstellen Sie einen String, der Ihren Vornamen entha ̈lt, und einen weiteren mit Ihrem Nachnamen. Berechnen Sie die La ̈nge Ihres gesamten Namens und speichern Sie dann Vor- und Nachname in einen weiteren String, getrennt durch ein Leerzeichen. Geben Sie nun Ihren Namen und seine La ̈nge in einem zusammengesetzten String aus. Erstellen Sie eine Liste mit den 5 Vokalen der deutschen Sprache.

#Uberpru ̈fen Sie, ob jener Vokal in Ihrem Namen vorhanden ist, der an der Stelle der Liste ist, welche der La ̈nge Ihres Namens mod 5 entspricht. Geben Sie die gewonnene Erkenntnis aus. Testen Sie nun mit einer for Schleife, ob alle 5 Vokale in Ihrem Namen vorkommen und geben Sie auch diese Erkenntnis aus. (6 Punkte)

vorname = input('Gib deinen Vornamen an: ')
nachname = input('Gib deinen Nachnamen an: ')
gesamter_name = vorname + ' ' + nachname
laenge = len(gesamter_name)
print('die Länge deines gesamten Namen ist: ',laenge)

vokale = ['a', 'e', 'o', 'u', 'i']

vokal = vokale[laenge % 5]
try:
	print('die gesuchte Variable ist in deinem Namen an der Stelle: ', gesamter_name.index(vokal))
except :
	print('Du hast anscheinend keine nötige Variable im Namen')
	
for n in gesamter_name:
	for v in iter(vokale):
		if n == v:
			print("Hier ist ein Vokal in deinem Namen:", gesamter_name.index(n))
