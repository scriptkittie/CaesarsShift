import sys
#Import the classes needed to manage the file.

class cipher():

#Create the instance for the class, then code that we will be using the userinput.py with the instance
#of the user class.

	created_file = ""
	fileopen = ""
	encrypt_file = ""
	data = ""
	decrypt_file = ""
	file_name = ""

#Initialize the variables that we'll be holding globally, we leave them blank as we'll be placing values
#in them throughout the code being run.

	def encryptkey(self, keycode):
		with open(self.file_name, 'a') as f:
			f.write(keycode)

#This function is encrypting the key to the file.  The argument is self so it can be called by itself.
#We call the keyblade function that is in the user class, call it by calling itself, the user instance, and
#then what function we'll be calling within the user class.  We then assign the information we get from the
#keyblade function, which requires the user to input the four digit code that would be encrypted in the file,
#check whether or not it fits our keycode requirements, stores the keycode and returns it - the keycode then
#is encrypted inside the file and the variable is stored with new data of the new encrypted file.

	def createfile(self):
		while(True):
			userinput = raw_input("Would you like to encrypt a current existing file, or would you like to create a file to encrypt  Type create or open.")

			if userinput == 'Create' or userinput == 'create' or userinput == 'C' or userinput == 'c':
				print "Creating new text file.\n"
				name = raw_input("Enter a name for the text file: \n")
				name = name +'.txt.'
				self.file_name = name

				try:
					created_file = open(name, 'w')
					filedata = raw_input("Please type what you would want written in the file: \n")
					with open(self.file_name, 'a') as f:
						f.write(filedata)
					encrypt_file = created_file
					break
				except:
					print("404: unable to create.  Returning back to the main menu.")

			elif  userinput == 'Open' or userinput == 'open' or userinput == 'O' or userinput == 'o':
				fileopen = raw_input("What is the .txt file you wish to open?\n" )
				fileopen = fileopen +'.txt'
				self.file_name = fileopen
				try:
					with open(fileopen, 'r') as f:
						self.data = f.read()
					break
				except:
					print("404: unable to create.  Returning back to the main menu.")
					
				else:
					print "Error 404: please input create or open into the prompt."

#We create this function to create a file to encrypt or to open a file to ecrypt.  We prompt the user whether
#or not they need to create the file to encrypt or they have another file they can open and encrypt.  We make
#the options for the user to choose and have the program run the appropriate function.
		
	def getdata(self):
		with open(self.file_name) as file:
			self.data = file.read()
		return self.data

#This function we get data from the file we just created or opened.  We download all the content into the
#data variable and return it.  This variable will be used in the encryption process.

	def encryption(self):
		encrypt_input = self.data
		output_string = ""

#This function is for the encryption.  We take the data that we created in getdata with the created/opened
#file and create the output string. We download this content into the output string.

		with open(self.file_name, 'w') as f:		
			for encryptcode in encrypt_input:
				character_code = ord(encryptcode)
				character_code = character_code + 9
				character_code = chr(character_code)
				f.write(character_code)
		self.getdata()
		return self.data

#We take the encrypt_input and make a variable called encrypt_code, and we make instructions for our "for statement"
#by saying we will make the character code assigned to ord, which will take each letter and transform it into an
#integer associated with that word.  We then ask the character code to add 9 values to the numbers it generated,
#we re-assign this new character code, and we ask for these reassigned values to be transformed back into letters by
#using the chr function.  We then ask for this to be written into the encrypt file, and to return the variable
#encrypt file with the new encrypted information.

	def decryption(self):
		decrypt_input = self.data[:-4]
		output_string = ""

#We download the data that we get from the opened file, which in this case is hopefully the encrypted file.
#We then use the same formula as we did encrypting the file, only instead of adding 9 values to the character
#number associated to the letters, we subtract the 9, which would put them in the correct placement.

		with open(self.file_name, 'w') as f:
			for decryptcode in decrypt_input:
				character_symbol = ord(decryptcode)
				character_symbol = character_symbol - 9
				character_symbol = chr(character_symbol)
				f.write(character_symbol)
		self.getdata()
		return self.data