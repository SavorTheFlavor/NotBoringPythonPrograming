import json
import xlwt

with open('students.txt', 'r') as f:
	data = f.read()
	
data = json.loads(data)
workbook = xlwt.Workbook(encoding='utf8')
worksheet = workbook.add_sheet('stupid students ranking')
for stu_id_str in data:
	stu_id = int(stu_id_str)
	worksheet.write(stu_id, 0, label=stu_id_str)
	for index,item in enumerate(data[stu_id_str]):
		worksheet.write(stu_id, index+1, label=item)
workbook.save('students.xls')