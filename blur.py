import os
import shutil
import cv2
from os import walk

x = 3
y = 10
func = 0

sigmaX = 0
sigmaY = 0
"""
print("I was about to explain this .py program, but it's troublesome.")
print("So no explaination")

input_path = raw_input("Enter the input path: ")
output_path = raw_input("Enter the output path: ")
print("0 = blur, 1 = GaussianBlur, 2 = medianBlur.\n(Defalt is 0)")
func = input("Choose the blur type tpye: ")

if len(input_path.strip()) == 0:
	input_path = "./"
if len(output_path.strip()) == 0:
	output_path = "./"
if func > 2 or func < 0 :
	func = 0
print("func Value is {}".format(func))
if func > 0:
	print("kernal size has to be odd.")
	print("median kernal is sqare. so ignore the y value")
x,y = input("Enter the Kernal Size x,y = ")
print("(x,y) = ({},{})".format(x,y))
if func == 1:
	print("Gaussian needs sigma value. (Defalts = 0)")
	sigmaX = input("Value: ")
	print("sigmaX = {}".format(sigmaX))
"""
input_path = "./test.txt"
output_path = "./blur/"

#""" img list, label list"""
"""
text_name_list = []
img_name_list = []
for (dirpath, dirnames, f) in walk(input_path):
	for name in f:
		if name.endswith('.txt'):
			text_name_list.append(name)
		elif name.endswith('.png') or name.endswith('.jpg') or name.endswith('.jpeg'):
			img_name_list.append(name)
"""
f = open(input_path,'r')

####Process
for img_path in f.readlines():#img_name_list:
#####Open input img files & copy to dst
#	img_path = input_path + img_name
	img_path = "./"+img_path[0:len(img_path)-1]
	li = img_path.rfind('/');
	img_name = img_path[li+1:len(img_path)]
	print("Input: " + img_path)
	print("Name: " + img_name)
	src = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
	if src is None:
		print("Wrong file")
		continue
	print("Success load img")
	dst = src.copy()
    
####blur processing
	if func == 0:
		print("blur function is called")
		dst = cv2.blur(src,(x,y))
	elif func == 1:
		print("Gaussian blur function is called")
		dst = cv2.GaussianBlur(src, (x,y), sigmaX)
	else:
		print("median blur function is called")
		# ksize must be odd & >1
		if (x % 2) == 0:
			x -= 1
		dst = cv2.medianBlur(src, x)
	
	# borderType = 	BORDER_REPLICATE	aaaaaa|abcdefgh|hhhhhhh
	#				BORDER_REFLECT:     fedcba|abcdefgh|hgfedcb
	#				BORDER_REFLECT_101: gfedcb|abcdefgh|gfedcba
	#				BORDER_WRAP:        cdefgh|abcdefgh|abcdefg
	# 				BORDER_CONSTANT:	iiiiii|abcdefgh|iiiiiii  with some specified 'i'
    
#####Save those images
	out_img = output_path + "blur_" + img_name
	cv2.imwrite(out_img, dst)

	
#	txt_name = text_name_list[img_name_list.index(img_name)]
#	shutil.copyfile(input_path+txt_name, output_path+"blur_"+txt_name)
	txt_path = img_path.replace(".jpg",".txt")
	txt_name = img_name.replace(".jpg",".txt")
	shutil.copyfile(txt_path,output_path+"blur_"+txt_name)



#adf	
