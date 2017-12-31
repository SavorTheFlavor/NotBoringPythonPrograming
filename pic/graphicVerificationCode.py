import string
import random
import sys
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

number = 5 #生成的验证码位数
width,height = (100,50)
bgcolor = (207,207,207)
fontcolor = (0,0,255)
linecolor = (255,192,203)

def generate_letters():
	return ''.join(random.sample(string.ascii_letters,number))

	#画干扰线
def draw_interfering_line(draw,w,h):
	for _ in range(0,number - 1):
		#生成随机的两个点
		begin = (random.randint(0, width), random.randint(0, height))
		end = (random.randint(0, width), random.randint(0, height))
		draw.line([begin, end], fill=linecolor)
	
def generate_gcode():
	image = Image.new('RGBA',(width,height),bgcolor)
	font = ImageFont.truetype('C:/Windows/Fonts/ALGER.TTF',25)
	draw = ImageDraw.Draw(image)
	text = generate_letters()
	print(text)
	font_width, font_height = font.getsize(text)
	draw.text(((width - font_width) / number, (height - font_height) / number),text,\
	font= font,fill=fontcolor) #填充字符串
	
	draw_interfering_line(draw,width,height);
	
	image = image.transform((width+20,height+10), Image.AFFINE, (1,-0.3,0,-0.1,1,0),Image.BILINEAR)  #创建扭曲
	image = image.filter(ImageFilter.EDGE_ENHANCE_MORE) #滤镜，边界加强
	image.save('idencode.png') #保存验证码图片

if __name__ == '__main__':
	generate_gcode()
     
