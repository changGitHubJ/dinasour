import math
import numpy as np
import os
import random

from matplotlib import pyplot as plt
from PIL import Image

if __name__ == "__main__":
    directories = ["tyrannosaurus",
                   "triceratops",
                   "brachiosaurus",
                   "stegosaurus",
                   "iguanodon",
                   "ornithomimus",
                   "pteranodon"]
    for directory in directories:
        files = os.listdir(directory)
        for file in files:
            try:
                img = Image.open(directory + '/' + file)
                # plt.imshow(img)
                # plt.show()
                width, height = img.size
                if(height >= width):
                    resized = Image.new(img.mode, (height, height), (255, 255, 255))
                    resized.paste(img, ((height - width)//2, 0))
                else:
                    resized = Image.new(img.mode, (width, width), (255, 255, 255))
                    resized.paste(img, (0, (width - height)//2))
                resized = resized.resize((256, 256), Image.LANCZOS)
                # plt.imshow(resized)
                # plt.show()
                file = file.split('.')[0]
                print("writing " + directory + '/' + file + '_256.jpg')
                resized.save(directory + '/' + file + '_256.jpg')
                arr_rgb = np.asarray(resized)
                np.savetxt(directory + '/' + file + '_256.txt', arr_rgb.reshape([256*256*3]), fmt="%d", delimiter=",")
            except:
                print("cannot output: " + directory + '/' + file + '_256.jpg')