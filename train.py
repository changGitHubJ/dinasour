import numpy as np
import os
import sys
import time

import common as c
import model
import libloaddata as data

training_epochs = 100
batch_size = 12

def main(training_data, train_data_size, test_data, output_name, log_name):
    y_train = np.zeros([train_data_size*c.CATEGORY, c.CATEGORY], dtype=np.int32)
    y_test = np.zeros([c.TEST_DATA_SIZE*c.CATEGORY, c.CATEGORY], dtype=np.int32)
    for i in range(train_data_size*c.CATEGORY):
        category = int(i / train_data_size)
        y_train[i, category] = 1
    for i in range(c.TEST_DATA_SIZE*c.CATEGORY):
        category = int(i / c.TEST_DATA_SIZE)
        y_test[i, category] = 1
    x_train = data.read_images(training_data, train_data_size*c.CATEGORY, 3)
    x_test = data.read_images(test_data, c.TEST_DATA_SIZE*c.CATEGORY, 3)
    
    input_shape = (c.IMG_SIZE, c.IMG_SIZE, 3)

    model.create_model(input_shape)
    history = model.training(x_train, y_train, x_test, y_test)
    accuracy = history.history["accuracy"]
    loss = history.history["loss"]
    val_accuracy = history.history["val_accuracy"]
    val_loss = history.history["val_loss"]

    model.save(output_name)

    with open(log_name, "w") as f:
        for i in range(training_epochs):
            line = "%f,%f,%f,%f\n"%(loss[i], accuracy[i], val_loss[i], val_accuracy[i])
            f.write(line)

if __name__=='__main__':
    args = sys.argv
    training_data = args[1]
    train_data_size = int(args[2])
    test_name = args[3]
    output_name = args[4]
    log_name = args[5]

    model = model.Model(batch_size, c.CATEGORY, training_epochs)
    main(training_data, train_data_size, test_name, output_name, log_name)
    