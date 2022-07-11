import random

class Poonsawat:
	"""
	คลาส Poonsawat คือ
	ข้อมูลที่เกี่ยวข้องกับ พี่วันว์วาร์ และน้องพอใจ
	ประกอบด้วยชื่อเพจ
	ชื่อช่องยูทูป 

	Example
	# ------------------------
	poonsawat = Poonsawat()
	poonsawat.show_name()
	poonsawat.show_youtube()
	poonsawat.show_page()
	poonsawat.about()
	poonsawat.show_art()
	# ------------------------
	"""

	def __init__(self):
		self.name = 'วันวาร์ พาใจฝัน'
		self.page = 'https://www.glo.or.th'

	def show_name(self):
		print('สวัสดีค่ะ ฉันชื่อ {}'.format(self.name))

	def show_youtube(self):
		print('https://www.youtube.com/watch?v=R0V6eiIrbkY')

	def show_page(self):
		print('WWW Page : {}'.format(self.page))

	def about(self):
		text = '''
		---------------------------------------
		สวัสดีค่ะ หนูชื่อ วันวาร์ พาใจฝัน
		เป็นผู้ดูแลเพจ 'พี่วันวาร์ กับน้องพอใจ
		สามารถติดตามเพจนี้ได้ เพื่อชมการผจญภัยของเราทั้งสอง
		---------------------------------------
		'''
		print(text)

	def show_art(self):
		text = '''
		|\_____/|     ////\\
		|/// \\\\\|    //  \\\\\\
		 |/O O\\|     |/o o\\|
		 d  ^ .b     C  )  D    
		  \\\m//      | \_/ |
		   \_/        \___/
		 __ooo__    _/<|_|>\_
		/_     _\  / |/\_/\| \\
		| \_v_/ | |    |\|    |
		|| _/ _/\\| |  |\|  | |
		||)    ( \| |  |\|  | |
		||      \ | \\ |\|  | |
		||  --  |  (())\_/  | |
		((      |   |___|___|_|
		 |______|   |   Y   |))
		  |-||-|    |   |   |
		  | || |    |   |   |
		  | || |    |   |   |
		  | || |    |___|___|prs
		 /u\||/u\   /qp| |qp\\
		(_/\||/\_) (___/ \___)

		'''
		print(text)

	def dice(self):
		dice_list = ['⚀','⚁','⚂','⚃','⚄','⚅']
		first = random.choice(dice_list)
		second = random.choice(dice_list)
		total_point = 0
		if first == '⚀':
			point1 = 1
		elif first == '⚁':
			point1 = 2
		elif first == '⚂':
			point1 = 3
		elif first == '⚃':
			point1 = 4
		elif first == '⚄':
			point1 = 5
		else: 
			point1 = 6
		if second == '⚀':
			point2 = 1
		elif second == '⚁':
			point2 = 2
		elif second == '⚂':
			point2 = 3
		elif second == '⚃':
			point2 = 4
		elif second == '⚄':
			point2 = 5
		else: 
			point2 = 6
		total_point = point1 + point2
		print('คุณทอยเต๋าได้ : {} {} หรือเท่ากับ {} แต้ม'.format(first,second,total_point))


if __name__ == '__main__':
	poonsawat = Poonsawat()
	poonsawat.show_name()
	poonsawat.show_youtube()
	poonsawat.show_page()
	poonsawat.about()
	poonsawat.show_art()
	poonsawat.dice()