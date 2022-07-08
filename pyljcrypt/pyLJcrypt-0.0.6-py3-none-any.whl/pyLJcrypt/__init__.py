import os
from cryptography.fernet import Fernet

class LJcrypt:
	
	def encrypt(self, fileName, keyName):
		key = Fernet.generate_key()
		
		with open(keyName + '.key', 'wb') as k:
			k.write(key)
		
		with open(fileName, 'rb') as f:
			data = f.read()
		encrypted = Fernet(key).encrypt(data)
		
		with open(fileName, 'wb') as f:
			f.write(encrypted)
	
	def decrypt(self, fileName, keyName):
		with open(keyName + '.key', 'rb') as k:
			key = k.read()
		
		with open(fileName, 'rb') as f:
			data = f.read()
		decrypted = Fernet(key).decrypt(data)
		
		with open(fileName, 'wb') as f:
			f.write(decrypted)
		
		os.remove(keyName + '.key')
	
	def author(self):
		print('Louiejay S. Boglosa')
		
crypt = LJcrypt() 