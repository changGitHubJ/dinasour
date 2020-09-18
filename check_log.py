import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    log_100 = np.loadtxt("./training_log_100.txt", delimiter=",")
    log_100_shuffle = np.loadtxt("./training_log_100_shuffle.txt", delimiter=",")
    log_300 = np.loadtxt("./training_log_300.txt", delimiter=",")
    log_300_shuffle = np.loadtxt("./training_log_300_shuffle.txt", delimiter=",")

    plt.figure(figsize=[17, 4])
    plt.subplot(1, 4, 1)
    plt.plot(log_100_shuffle[:, 1], label="accuracy of training", color="blue")
    plt.plot(log_100_shuffle[:, 3], label="accuracy of test", color="orange")
    plt.xlabel("epoch")
    plt.ylabel("accuracy")
    plt.ylim([0.0, 1.1])
    plt.legend()

    plt.subplot(1, 4, 2)
    plt.plot(log_300_shuffle[:, 1], label="accuracy of training", color="blue")
    plt.plot(log_300_shuffle[:, 3], label="accuracy of test", color="orange")
    plt.xlabel("epoch")
    plt.ylabel("accuracy")
    plt.ylim([0.0, 1.1])
    plt.legend()

    plt.subplot(1, 4, 3)
    plt.plot(log_100[:, 1], label="accuracy of training", color="blue")
    plt.plot(log_100[:, 3], label="accuracy of test", color="orange")
    plt.xlabel("epoch")
    plt.ylabel("accuracy")
    plt.ylim([0.0, 1.1])
    plt.legend()

    plt.subplot(1, 4, 4)
    plt.plot(log_300[:, 1], label="accuracy of training", color="blue")
    plt.plot(log_300[:, 3], label="accuracy of test", color="orange")
    plt.xlabel("epoch")
    plt.ylabel("accuracy")
    plt.ylim([0.0, 1.1])
    plt.legend()

    plt.show()