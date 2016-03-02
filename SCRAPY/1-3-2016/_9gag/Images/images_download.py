import json,os
path = os.getcwd()
print path

extenstion = '.jpg'
os.chdir(path)
with open("output.json") as json_file:
    json_data = json.load(json_file)


count = 0
for i in json_data:
	image_now = i['img_url']
	image_now = ''.join(image_now)
	image_title = i['title']
	count+=1
	if (extenstion in image_now):
		# os.chdir(path+'/'+'Images')
		if not os.path.exists(image_title):
			os.mkdir(image_title)
			os.chdir(path+'/'+image_title)
			os.system('wget ' + i['img_url'][0] )
			os.chdir(path)
	if count == 90:
		break

# str1 = ''.join(list1)