import sys
import os
from PIL import Image

# grab first and second arguments
input_image_folder = sys.argv[1]
output_image_folder = sys.argv[2]
print(output_image_folder)

# check if Output/ exists, if not create it
if not os.path.exists(output_image_folder):
    os.makedirs(output_image_folder)

# convert all
for filename in os.listdir(input_image_folder):
    img = Image.open(f'{input_image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_image_folder}{clean_name}.png','png')
    print('all done!')