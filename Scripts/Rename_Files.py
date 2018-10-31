import os

from glob import glob

imgs_files=glob('C:\\Users\\hehe\\Desktop\\FALL_Image\\*.jpg')

# print (len(imgs_files))

for i,img in enumerate(imgs_files):
	os.rename(img,(str)(i)+'.jpg')