## An automatic process to remove the background from images
# Requires dependency: pip install backgroundremover

import os

path_to_img_dir = "~/Downloads/Training_set-20220903T075348Z-001/Training_set/"

for i in range(46):
    bashCommand = "backgroundremover -i " + path_to_img_dir + str(i) + ".png -o " + path_to_img_dir + str(i) + "_bkgndrem.png"
    print("Running: " + path_to_img_dir + str(i) + ".png")
    os.system(bashCommand)