import random
class stringgen:
	def gen():
		pl = []
		l = 5
		pl.append(l)
		alphabet = "abcdefghijkRTYUIOPMNBVCXZlmnopqrstuvwxyzASDFGHJKLQWE"
		for i in pl:
			gstring = ""
			for j in range(i):
				next_letter_index = random.randrange(len(alphabet))
				gstring = gstring + alphabet[next_letter_index]

			return gstring


