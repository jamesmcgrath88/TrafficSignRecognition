import shutil
import os
import csv

# 'Test.csv' contains the URL of each image and its class ID
# This script copies the images into subfolders by class ID,
# so it can be used with ImageDataGenerator

with open(os.path.join('Test.csv'), 'r') as f:
        reader = csv.reader(f)
        for rows in reader:
            name = rows[7]
            if (name == 'Path'):
                continue
            classid = rows[6]
            dest_path = './Test/' + classid + '/'
            if not os.path.isdir(dest_path):
                os.makedirs(dest_path)
            shutil.copy(name, dest_path)