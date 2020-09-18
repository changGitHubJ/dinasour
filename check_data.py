import matplotlib.pyplot as plt
import numpy as np

import common as c
import libloaddata as data

RGB = 3

def readImages(filename, DATA_SIZE):
    images = np.zeros((DATA_SIZE, c.IMG_SIZE, c.IMG_SIZE, RGB), dtype=np.float)
    fileImg = open(filename)
    for k in range(DATA_SIZE):
        line = fileImg.readline()
        if(not line):
            break
        val = line.split(',')
        for i in range(c.IMG_SIZE):
            for j in range(c.IMG_SIZE):
                for n in range(RGB):
                    images[k, i, j, n] = float(val[RGB*(c.IMG_SIZE*i + j) + n + 1])/255.0
    return images

def main_py():
    NUM = c.TEST_DATA_SIZE*c.CATEGORY
    train_image = readImages('./data/testImage256.txt', NUM)

    for i in range(NUM):
        print(i)
        plt.figure(figsize=[5, 5])
        fig = plt.imshow(train_image[i, :, : , :].reshape([c.IMG_SIZE, c.IMG_SIZE, RGB]), vmin=0, vmax=1)
        fig.axes.get_xaxis().set_visible(False)
        fig.axes.get_yaxis().set_visible(False)
        plt.show()

def main_cpp(data_name, num):   
    train_image = data.read_images(data_name, num, RGB)

    for i in range(num):
        print(i)
        plt.figure(figsize=[5, 5])
        fig = plt.imshow(train_image[i, :, : , :], vmin=0, vmax=1)
        fig.axes.get_xaxis().set_visible(False)
        fig.axes.get_yaxis().set_visible(False)
        plt.show()

if __name__=='__main__':
    #main_py()
    main_cpp('./data/trainImage256_300.txt', c.TRAIN_DATA_SIZE1*c.CATEGORY)
