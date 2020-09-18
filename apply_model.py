
import keras
import matplotlib.pyplot as plt
import numpy as np
import random
import tensorflow as tf

from matplotlib import cm

import common as c
import libloaddata as data

RGB = 3

def main(model_name, test_data_name, NUM):
    with tf.device("/gpu:0"):
        model = keras.models.load_model(model_name)
        image = data.read_images(test_data_name, NUM, RGB)
        count_ok = 0
        msgs = []
        for i in range(c.TEST_DATA_SIZE*c.CATEGORY):
            #index = random.randint(0, NUM - 1)
            index = i
            result = model.predict(image[index].reshape([1, c.IMG_SIZE, c.IMG_SIZE, RGB]))

            cat = np.argmax(result)
            score = result[0, cat]
            ans = int(i/c.TEST_DATA_SIZE)
            if cat == ans and score > 0.5:
                msg = "%d, OK, category = %d, score = %f"%(i, cat, score)
                print(msg)
                count_ok += 1
            else:
                msg = "%d, NG, category = %d, score = %f"%(i, cat, score)
                print(msg)
            
            if((i + 1)%c.TEST_DATA_SIZE == 0):
                msgs.append("category %d, accuracy_rate = %f"%(ans, count_ok/c.TEST_DATA_SIZE))
                count_ok = 0

            plt.figure(figsize=[6, 6])
            fig = plt.imshow(image[index].reshape([c.IMG_SIZE, c.IMG_SIZE, RGB]))
            fig.axes.get_xaxis().set_visible(False)
            fig.axes.get_yaxis().set_visible(False)
            plt.show()

        print()
        for line in msgs:
            print(line)

if __name__=='__main__':
    #main("model_100_shuffle.h5", './data/testImage256_shuffle.txt', c.TEST_DATA_SIZE*c.CATEGORY)
    #main("model_300_shuffle.h5", './data/testImage256_shuffle.txt', c.TEST_DATA_SIZE*c.CATEGORY)
    main("model_300.h5", './data/testImage256.txt', c.TEST_DATA_SIZE*c.CATEGORY)

    