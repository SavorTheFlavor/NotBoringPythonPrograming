import pymysql
from random import randint

def generateCode():
	codes = []
	for _ in range(200):	
		#5个字母 + 19个数字
		code = [chr(randint(0,25)+ord('A')) for _ in range(5)]
		code = code + [str(randint(0,9)) for _ in range(19)]
		codes.append(''.join(code))
	return codes

if __name__ == '__main__':
	db = pymysql.connect("localhost","root",'23456','python')
	cursor = db.cursor()
	codes = generateCode()
	#python自带的类似printf之类的语法
	insertSql = "insert into codes(value) values('%s')"
	for item in codes:
		try:
			sql = insertSql % (item)
			cursor.execute(sql)
			db.commit()
		except Exception as e:
			db.rollback()
			continue
	db.close()

	#createSql = '''
	#	create table codes(
	#		id int(11) not null auto_increment primary key,
	#		value varchar(24)
	#		)
	#'''
	#cursor.execute(createSql)



