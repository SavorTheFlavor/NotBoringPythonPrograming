import redis
from random import randint

class RedisDemo(object):

	def __init__(self):
		self.conn = redis.Redis(host='localhost', port=6379,db=0)

	def generateCode(self):
		codes = []
		for _ in range(200):	
			#5个字母 + 19个数字
			code = [chr(randint(0,25)+ord('A')) for _ in range(5)]
			code = code + [str(randint(0,9)) for _ in range(19)]
			codes.append(''.join(code))
		return codes

	def test(self):
		codes = self.generateCode()
		r = self.conn
		for i in range(len(codes)):
			r.set(i,codes[i])
		print("dbsize:"+str(r.dbsize()))
		print(r.mget(['33','77']))

if __name__ == '__main__':
	rd = RedisDemo()
	rd.test()

