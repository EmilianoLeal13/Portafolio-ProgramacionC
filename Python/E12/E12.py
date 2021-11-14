import argparse
import detectSpanish

def Cifrado_Cesar(message,clave):
	#message = input('Ingresa el mensaje: ')
	espacios = 1
	while espacios > 0:
	    #clave = input('Ingresa tu palabra clave para cifrar: ')
	    espacios = clave.count(' ')
	    if clave.isalpha() == False:
	        espacios += 1
	key = len(clave)

	SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

	translated = ''

	for symbol in message:
	    # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
	    if symbol in SYMBOLS:
	        symbolIndex = SYMBOLS.find(symbol)
	        translatedIndex = symbolIndex + key
	        
	        if translatedIndex >= len(SYMBOLS):
	            translatedIndex = translatedIndex - len(SYMBOLS)
	        elif translatedIndex < 0:
	            translatedIndex = translatedIndex + len(SYMBOLS)

	        translated = translated + SYMBOLS[translatedIndex]
	    else:
	        # Append the symbol without encrypting/decrypting:
	        translated = translated + symbol

	print(translated)

def Descifrado_Cesar(message,clave):
	#message = input('Ingresa el mensaje: ')
	espacios = 1
	while espacios > 0:
	    #clave = input('Ingresa tu palabra clave para cifrar: ')
	    espacios = clave.count(' ')
	    if clave.isalpha() == False:
	        espacios += 1
	key = len(clave)

	SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

	translated = ''

	for symbol in message:
	    # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
	    if symbol in SYMBOLS:
	        symbolIndex = SYMBOLS.find(symbol)
	        translatedIndex = symbolIndex - key
	        
	        if translatedIndex >= len(SYMBOLS):
	            translatedIndex = translatedIndex - len(SYMBOLS)
	        elif translatedIndex < 0:
	            translatedIndex = translatedIndex + len(SYMBOLS)

	        translated = translated + SYMBOLS[translatedIndex]
	    else:
	        # Append the symbol without encrypting/decrypting:
	        translated = translated + symbol

	print(translated)

def Crackeo_Cesar(message):
	#message = input('Ingresa el mensaje: ')
	SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

	# Loop through every possible key:
	for key in range(len(SYMBOLS)):
	    # It is important to set translated to the blank string so that the
	    # previous iteration's value for translated is cleared.
	    translated = ''

	    # The rest of the program is almost the same as the original program:

	    # Loop through each symbol in `message`:
	    for symbol in message:
	        if symbol in SYMBOLS:
	            symbolIndex = SYMBOLS.find(symbol)
	            translatedIndex = symbolIndex - key

	            # Handle the wrap-around:
	            if translatedIndex < 0:
	                translatedIndex = translatedIndex + len(SYMBOLS)

	            # Append the decrypted symbol:
	            translated = translated + SYMBOLS[translatedIndex]

	        else:
	            # Append the symbol without encrypting/decrypting:
	            translated = translated + symbol

	    #print(detect(translated))
	    # Display every possible decryption:
	    if detectSpanish.isSpanish(translated):
	    	print("Posibles Spanish Key")
	    	print('Key #%s: %s' % (key, translated))



parser = argparse.ArgumentParser()
parser.add_argument('-e', help='encript mode', action='store_true')
parser.add_argument('-de', help='desencript mode', action='store_true')
parser.add_argument('-c', help='crack mode', action='store_true')

parser.add_argument('-m', type=str, help='message')
parser.add_argument('-k', type=str, help='key')
#args = parser.parse_args()
args, leftovers = parser.parse_known_args()
if args.e:
	Cifrado_Cesar(args.m,args.k)
if args.de:
	Descifrado_Cesar(args.m,args.k)
if args.c:
	Crackeo_Cesar(args.m)

