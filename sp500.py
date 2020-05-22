import sys
import finsymbols

sp500 = finsymbols.get_sp500_symbols()

f = open('tickers.txt', 'w')
for tickets in sp500:
	for key, value in tickets.items():
		if key == 'symbol':
			f.write(value.rstrip() + "\n")
						
print('file was created')