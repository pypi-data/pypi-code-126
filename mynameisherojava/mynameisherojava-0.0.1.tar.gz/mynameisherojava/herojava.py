class Herojava:
	"""
	คลาส Herojava คือ
	ข้อมูลเกี่ยวกับ Herojava
	
	Example
	#----------------------------
	herojava = Herojava()
	herojava.show_name()
	herojava.show_youtube()
	herojava.show_page()
	herojava.about()
	herojava.show_art()
	#----------------------------
	"""

	def __init__(self):
		self.name = 'Herojava'
		self.page = 'www.google.co.th'

	def show_name(self):
		print(f'สวัสดีฉันชื่อ {self.name}')

	def show_youtube(self):
		print('www.youtube.com')

	def show_page(self):
		print(f'เพจของฉันคือ :: {self.page}')

	def about(self):
		text = """
		สวัสดีจ้านี้ Herojava เอง ไม่มีอะไรให้ตามหรอครับ
		ลองเขียนแบบหลายๆ บรรทัดตามลุงวิศวะกร สอนคำนวณ
		"""
		print(text)

	def show_art(self):
		text = """
        _.---.__
      .'        `-.
     /      .--.   |
     \\/  / /    |_/
      `\\/|/    _(_)
   ___  /|_.--'    `.   .
   \\  `--' .---.     \\ /|
    )   `       \\     //|
    | __    __   |   '/||
    |/  \\  /  \\      / ||
    ||  |  |   \\     \\  |
    \\|  |  |   /        |
   __\\\\@/  |@ | ___ \\--'
  (     /' `--'  __)|
 __>   (  .  .--' &"\\
/   `--|_/--'     &  |
|                 #. |
|                 q# |
 \\              ,ad#'
  `.________.ad####'
    `#####""""""''
     `&#"
      &# "&
      "#ba"

		"""
		print(text)

if __name__ == '__main__':
	herojava = Herojava()
	herojava.show_name()
	herojava.show_youtube()
	herojava.show_page()
	herojava.about()
	herojava.show_art()