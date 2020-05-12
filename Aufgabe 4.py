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
	if sum_1 == sum_2:
		gleich = '='
		if n <= 13: #weil die kleineren Zahlen kürzer sind 
			print(sum_1, gleich, sum_2, sep = 2*'\t')
		else:
			print(sum_1, gleich, sum_2, sep = '\t')	
			#ich habe versucht mit if sum1=sum2: try und except, aber hat nicht funktioniert.
	else:
		if n <= 13:  
			print(sum_1, '!=', sum_2, sep = '\t')
		else:
			print(sum_1, '!=', sum_2, sep = '\t')	
			
			#meine Lösung ist interaktiv, zeigt ob jede einzelne Zeile tatsächlich entsprechendem Wert gleicht.
	
