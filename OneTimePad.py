######################################################
#                       Made By                      #
#                    Keegan Currie                   #
######################################################
#                      Created on                    #
#                    March 30, 2017                  #        
######################################################
#                       Version                      #
#                         3.0                        #
######################################################
import random, zlib, base64, argparse, re

#Argmuent Stuff
parser = argparse.ArgumentParser()

#Settings
parser.add_argument("-v","--view", help="Print key and fine details to screen", action="store_true")

#Encrypt args
parser.add_argument("-e","--encrypt", help="Encrypt mode", action="store_true")
parser.add_argument("-ko","--keyout", help="Output file name for your one time pad key. Default filename is pad.key")
parser.add_argument("-do","--dataout", help="Output file name for your encrypted data. Default will just print it to the screen")
parser.add_argument("-da","--data", help="Text you want to encrypt. Put data in quotes to avoid problems. If this argument is not used then you will be promoted an area to enter data")
#Decrypt args
parser.add_argument("-d","--decrypt", help="Decrypt mode", action="store_true")
parser.add_argument("-kf","--keyfile", help="File with your key stored in it. If a file is not specified the default file name 'pad.key' will be used")
parser.add_argument("-ef","--EnFile", help="File with your encrypted data. If a file is not specified you will be promoted an area to enter it")
parser.add_argument("-DD","--encryptedData", help="Text you want to decrypt. Put data in quotes to avoid problems. If this argument is not used then you will be promoted an area to enter data")
args = parser.parse_args()


#Check arguments for desired settings
if args.keyout:
    filename = args.keyout
else:
	filename = "pad.key"

if not (args.encrypt or args.decrypt):
    parser.error('You must specify a mode to use (--encrypt or --decrypt)')


if args.keyfile:
	keyfilePath = args.keyfile
else:
	keyfilePath = "pad.key"

if args.data:
	DataToEncrypt = args.data
else:
	DataToEncrypt = ""


def Encrypt():
	#Character that are allowed to be encrypted
	alpha = "abcdefghijklmnopqrstuvwxyz!@#$%^&*()[]{}<>\"'?.,;:\\|/1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ_=+- "
	waitUsed = list(alpha)
	
	if not DataToEncrypt:
		print "Enter text to encrypt"
		data = raw_input()
	else:
		data = DataToEncrypt

	keepGo = True

	#Check data for only allowed data
	for x in data:
		if x not in waitUsed and keepGo == True:
			keepGo = False
			print "Data not allowed to be encrypted"
			quit()

	usedKey = []

	print "Generating random one time pad..."
	#Generate key array and check for dups
	while waitUsed >= 1:
		key = random.randint(0000,9999)
		while any(key in sublist for sublist in usedKey) == True:
			key = random.randint(0000,9999)
		#Randomly select a letter from waitUsed and add it to usedkey then remove it
		if len(waitUsed) != 0:
			randChar = waitUsed[random.randint(0,len(waitUsed) - 1)]
			usedKey.append([key, randChar])
			del waitUsed[waitUsed.index(randChar)]
		else:
		 	break

	#Encrypt data typed in from user
	print "You entered \"" + data + "\" now encrypting this data with generated key "
	data = base64.b64encode(zlib.compress(data,9))
	EnData = ""
	for x in data:
		for i in usedKey:
			if i[1] == x:
				EnData += " " + str(i[0])
	

	EnData = "----DATA BEGIN----\n" + EnData + "\n----DATA END----\n"
	print EnData

	keyFile = open(filename, 'w')
	
	keyExport = "----KEY BEGIN----\n" 
	for x in usedKey:
		keyExport += str(x[0]) + " " + str(x[1]) + "\n"
	
	keyExport += "----KEY END----\n"
	
	keyFile.write(zlib.compress(keyExport, 9))
	keyFile.close()

	if args.view:
		print keyExport

	if args.dataout:
		try:
			dataoutFile = open(args.dataout, 'w')
			dataoutFile.write(EnData)
			dataoutFile.close()
		except:
			print "Error writing encrypted data to file"

def Decrypt():
	try:
		keyimport = open(keyfilePath, "r")
	except:
		parser.error('Your specified key to decrypt with does not exist')
	
	started = False
	key = []
	decompressedKey = zlib.decompress(keyimport.read())
	
	for x in decompressedKey.splitlines():
		if x == "----KEY BEGIN----":
			started = True
			continue
			
		if x == "----KEY END----":
			started = False
			continue
			
		if started == True:
			#key += x
			tmp = x.split()
			if len(tmp) == 1:
				key.append([tmp[0], " "])
			else:
				key.append([tmp[0], tmp[1]])


	if args.EnFile:
		try:
			enFilePath = open(args.EnFile, "r")
			EnData = enFilePath.readlines()
			enFilePath.close()
			if EnData[0] == '----DATA BEGIN----\n' and EnData[2] == '----DATA END----\n':
				EnData = EnData[1]
		except:
			parser.error('Your specified file with encrypted data does not exist')

	elif not args.encryptedData:
		print "Enter encrypted data below"
		EnData = raw_input()
	else:
		EnData = args.encryptedData

	print "Decrypting data..."
	#Check input with regex because why not!
	if re.match("[0123456789 ]", EnData) is None:
		print "Invalid data"
		quit()

	EnData = EnData.split()
	deData = ""

	#Match key with letter
	for y in EnData:
		for x in key:
			if x[0] == y:
				deData += x[1]
	try:
		print "Decrypted data: " + zlib.decompress(base64.b64decode(deData))
	except:
		print "Error decrypting. Please make sure you are using the correct key"
	

if __name__ == "__main__":
    if args.encrypt and args.decrypt:
    	parser.error("You cant use both modes at the same time")
    	quit()

    if args.encrypt:
    	Encrypt()

    if args.decrypt:
    	Decrypt()