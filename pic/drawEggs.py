from PIL import Image,ImageDraw,ImageFont

def white_to_transparent(img):
	img = img.convert('RGBA')
	datas = img.getdata()
	newdata = []
	for item in datas:
		#turn the colors nearing white into transparent....
		if(item[0] > 244 and item[1] > 244 and item[2] > 233):
                        newdata.append((255,255,255,0))
		else:
			newdata.append(item)
	img.putdata(newdata) #从图像的左上角（0，0）位置开始,会覆盖
	return img

if __name__ == '__main__':
	img = Image.open('user.jpg')
	#p2_image=Image.open(p2_name)
	#p2_image=white_to_transparent(p2_image)
	#p1_image.paste(p2_transparent,(0,0),p2_transparent)
	font = ImageFont.truetype("arial.ttf", 32)
	draw = ImageDraw.Draw(img)
	draw.text((img.width - 70,0),u'999+',font=font,fill=(255,0,0,128))
	img.show()


