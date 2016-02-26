import json,os
path = os.getcwd()

extenstion = '.jpg'
with open("export.json") as json_file:
    json_data = json.load(json_file)


# for i in json_data:
# 	image_now = i['url']
# 	image_title = i['title']
# 	if (extenstion in image_now):
# 		if not os.path.exists(image_title[0:30]):
# 			os.mkdir(image_title[0:30])
# 			os.chdir(path+'/'+image_title[0:30])
# 			os.system('wget ' + i['image_urls'][0] )
# 			os.chdir(path)
       	
# 	else:
# 		print "Error"

count = 0
for i in json_data:
	image_now = i['url']
	image_title = i['title']
	count+=1
	if (extenstion in image_now):
		if not os.path.exists(image_title):
			os.mkdir(image_title)
			os.chdir(path+'/'+image_title)
			os.system('wget ' + i['image_urls'][0] )
			os.chdir(path)
	# print image_title
	# print image_now
	# print count
	if count == 10:
		break

