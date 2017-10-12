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
	cs = generateCode()
	print(cs)

