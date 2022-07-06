import random
import os

class NellException(Exception):
	pass

class EasyClass:

	def random(self):

		return random.random()

	def system(self):

		return os.system()

	def randint(self, a, b):

		try: 
			return random.randint(a, b)

		except:

			return NellException("Gived invalid arguments")