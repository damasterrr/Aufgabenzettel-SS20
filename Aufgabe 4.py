#Die Summe der ersten Quadratzahlen kann wie folgt berechnet werden: 
		#Summe k=1 bis n k^2 = [n(n + 1)(2n + 1)]/6 
#Zeigen Sie mit einer Schleife fu ̈r n = 1, 2, 3, ..., dass die Formel zumindest fu ̈r die ersten 30 natu ̈rlichen Zahlen korrekt ist. Geben Sie in einer Tabelle n sowie das Ergebnis der linken und auch der rechten Seite am Bildschirm aus.(3 Punkte)

sum_1 = 0
k = 1
werte_n = range(1,31)
for n in werte_n: 
	sum_1 = sum_1 + k**2
	k = k+1
	sum_2 = (n*(n+1)*(2*n+1))/6
	if n <= 13:
		print(sum_1, sum_2, sep = 2*'\t') #weil die kleineren Zahlen kürzer sind
	else:
		print(sum_1, sum_2, sep = '\t')
