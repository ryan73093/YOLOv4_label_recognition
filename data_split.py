# -*- coding: utf-8 -*-
"""
Created on Tue May 25 18:27:09 2021

@author: ryan7
"""
# split data to train and dev
import os, shutil
import random
curDir =os.path.abspath(os.path.dirname(__file__))


images_list = []
for img in os.listdir(curDir+"/data/images"):
    if img.endswith(".jpg"):
        images_list.append(img.split(".")[0])
        
random.shuffle(images_list)

# 90%訓練 10%驗證
train_ratio = 0.9
train_num = int(round(len(images_list) * train_ratio, 0))
# prepare train folder

annotations_folder = os.path.join(curDir+"//data//annotations")
images_folder = os.path.join(curDir+"//data//images")
train_folder = os.path.join(curDir+'//data//train')
dev_folder = os.path.join(curDir+'//data//dev')

try:
    shutil.rmtree(train_folder)
except FileNotFoundError:
    pass    
os.mkdir(train_folder)

try:
    shutil.rmtree(dev_folder)
except FileNotFoundError:
    pass
os.mkdir(dev_folder)



# train data 
for train_data in images_list[:train_num]:
    shutil.copyfile(os.path.join(images_folder, "{}.jpg".format(train_data)),  
                    os.path.join(train_folder, "{}.jpg".format(train_data)))
    shutil.copyfile(os.path.join(annotations_folder, "{}.txt".format(train_data)),  
                    os.path.join(train_folder, "{}.txt".format(train_data)))
   
# dev data
for test_data in images_list[train_num+1:]:
    shutil.copyfile(os.path.join(images_folder, "{}.jpg".format(test_data)),  
                    os.path.join(dev_folder, "{}.jpg".format(test_data)))
    shutil.copyfile(os.path.join(annotations_folder, "{}.txt".format(test_data)),  
                    os.path.join(dev_folder, "{}.txt".format(test_data)))
# show total data 
print("="*35)
print("number of training set :", len(images_list[:train_num]))
print("number of dev set :", len(images_list[train_num+1:]))
print("="*35)
