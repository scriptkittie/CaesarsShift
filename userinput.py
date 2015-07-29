import sys
import cipher

#We import the classes and libraries we'll need.

class user():
	
	cipher_instance =  cipher.cipher()
	
	def keycheck(self,keycode):
		while(True):
			if(len(keycode) == 4):
				keycode = int(keycode)
				break
			elif(len(keycode ) < 4):
				print "This is too small of a keycode.  Please type only 4 digits."
				keycode = raw_input("Please give the four digit code to decrypt the message: ")
			else:
				print "This is too large of a keycode.  Please type only 4 digits."
				keycode = raw_input("Please give the four digit code to decrypt the message: ")

		return keycode
		
#This creates the keycode function, prompting the user a four digit code that will be added onto the encrypted file so no one
#can use the program to immediately decrypt their message.  We use  the keycheck to see if it fits our requirements.
	
	
	def keyblade(self):
		keycode = raw_input("Please give us a four digit code that will be the key to your encrypted message: ")
		self.keycheck(keycode)
		return keycode

	def greeting(self):
		while(True):
			runprogram = raw_input("Hello and welcome to the Caesar Shift Encryption program.  Would you like to run this program?" )

			if runprogram == 'Yes' or runprogram == 'yes' or runprogram == 'Y' or runprogram == 'y':
				break
			elif  runprogram == 'No' or runprogram == 'no' or runprogram == 'N' or runprogram == 'n':
				print "Shutting down the program.  Have a nice day."
				sys.exit()
			else:
				print "Error 404: please input yes or no into the prompt."

#We create the greeting function so we can call it whenever we need to. This introduces the user to the program
#and whether or not to continue. 


	def usercipher(self):
		while(True):

			userinput = raw_input("Would you like to encrypt or decrypt a message? Please input \"e\" for encryption or \"d\" for decryption.  To go back to the main screen, type quit.")

			if userinput == 'Encrypt' or userinput == 'E' or userinput == 'encrypt' or userinput == 'e':
				self.cipher_instance.createfile()
				self.cipher_instance.getdata()
				self.cipher_instance.encryption()
				key = self.keyblade()
				self.cipher_instance.encryptkey(key)
			elif userinput == 'Decrypt' or userinput == 'D' or userinput == 'decrypt' or userinput == 'd':
				self.cipher_instance.createfile()
				self.cipher_instance.getdata()
				key = self.keyblade()
				self.decryptpermission(key)
				self.cipher_instance.decryption()
			elif userinput == 'Quit' or userinput == 'Q' or userinput == 'quit' or userinput == 'q':
				break
			else:
				print "Error 404: please input e, d, or quit."

#We offer whether the user would like to encrypt or decrypt a file.  We implement a simple system for whether or not they do not choose
#either option, or exit.  We make if-else statements because it seems the most efficient. 

	def filecheck(self):
		while(True):

			userinput = raw_input ("Is this the file you were wanting to encrypt or decrypt? (y/n)")

			if userinput == 'Yes' or userinput == 'yes' or userinput == 'Y' or userinput == 'y':
				self.usercipher()
			elif  userinput == 'No' or userinput == 'no' or userinput == 'N' or userinput == 'n':
				self.cipher_instance.createfile()
			else:
				print "Error 404: please input yes or no into the prompt."

#This function is to check whether or not the file that is being opened or created is the correct file the user would
#like to decrypt or encrypt.

	def decryptpermission(self, keycode):
		while(True):
			userinput = raw_input("Please give the four digit code to decrypt the message: ")
			self.keycheck(userinput)
			self.cipher_instance.getdata()
			if self.cipher_instance.data[-4:] == userinput:
				break
			else:
				print "You have entered the wrong keycode."


#This function is using the keycode that we created and added to the encrypted file.  This checks whether or not
#the keycode that was added into the encrypted file is the same as what the user input.
#We create this function to decrypt the key should the user want to open up their message.  We take the stored
#encrypted file and check the last four digits of the file.  If the last four digits that was encrypted in the
#file match the four that the user input, we grant them permission to decrypt.   We use the decryptpermission
#function within the user instance.  The decryptpermission function takes the userinput, which will be four digits
#and checked if the key passes all the requirements of being a key (not being a letter, no characters, etc)
#and we run through whether or not the four digits entered match the last four digits of our encrypted file,
#and we grant them the permission to decode the document.

