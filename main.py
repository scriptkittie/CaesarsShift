import sys
import cipher
import userinput

#We import the classes we've constructed, so we can make the main program clean and simply managed,

def main():
	cipher_instance =  cipher.cipher()
	user_instance = userinput.user()

#We create the instances of the classes, assigning them to "self" so they are called.

	print """

	Welcome to the Caesar Shift Encryption System.  This program will encrypt your messages with a rudimentary
	encryption method, design a specific and manual keycode, and allow messages to be decrypted.  Play around with
	coded messages with a friend, or encrypt bad poetry, or send sweet encrypted love letters to that person next 
	door you are too terrified to tell how you feel -- just pray they're not a cryptographer. Good luck and cryptograph
	responsibly.

	Program is by Roya Shams.

	"""

#Give the user an introduction as to what the program does.
	while(True):
		user_instance.greeting()
	
		user_instance.usercipher()
	
		user_instance.filecheck()
	

main()