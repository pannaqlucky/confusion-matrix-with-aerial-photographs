from PIL import Image
import os
import pandas as pd 
import csv
from tqdm import trange

Image.MAX_IMAGE_PIXELS = 1000000000000000000000000000000000
k = open("confusion_matrix_pre_label.csv", 'w+')

pre_folder = "./pre_label"

imlist = os.listdir(pre_folder)
imlist.sort()

width,height = 1388,589

for imagename in imlist:
	imurl = os.path.join(pre_folder,imagename)
	print(imurl)
	im = Image.open(imurl)
	rgb_im = im.convert('RGB')
	for a in trange(width):
		for h in range(height):
		 r, g, b = rgb_im.getpixel((a, h))
		 if  r==0 and g==0 and b==255 :
		  pre_label = 0 # water
		 elif r==150 and g==50 and b==20 :
		  pre_label = 1 # bare_ground
		 elif r==255 and g==255 and b==0 :
		  pre_label = 2 # grass
		 elif r==0 and g==200 and b==255 :
		  pre_label = 3 # tree
		 elif r==255 and g==0 and b==0 :
		  pre_label = 4 # bamboo
		 elif r==20 and g==150 and b==150 :
		  pre_label = 5 #road
		 elif r==0 and g==0 and b==0 :
		  pre_label = 6 # clutter
#		 elif r==255 and g==255 and b==255 :
#		  pre_label[5]=pre_label[5]+1
		 else :
		  pre_label = 7 # background
#		 elif pre_label[0] >0 or pre_label[1] >0 or pre_label[2] >0 or pre_label[3] >0 or pre_label[4] >0 :
#		  pre_label[5]=0
		 print(pre_label, file=k)

with open('confusion_matrix_pre_label.csv',newline='') as k:
	 r = csv.reader(k)
	 data = [line for line in r]
with open('confusion_matrix_pre_label.csv','w',newline='') as k:
	 w = csv.writer(k)
	 w.writerow(['pre_label'])
	 w.writerows(data)

print('完成')

