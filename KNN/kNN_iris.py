from kNN import kNN
import get_iris_dataset
import matplotlib.pyplot as plt
import numpy as np

def plot_data(InputTrian,OutputTrian,InputTest=[],OutputTest=[],ZTest=[]):
    color = { 
              "Iris-setosa" : "b",
              "Iris-versicolor" : "g",
              "Iris-virginica" : "r"
            }
    for i in range(0,len(InputTrian)):
        plt.plot(InputTrian[i][0],InputTrian[i][1],"x", c=color[OutputTrian[i]], mfc = "none")
    for i in range(0,len(InputTest)):
        plt.plot(InputTest[i][0],InputTest[i][1],"-", c="none", mfc = color[OutputTest[i]])
    for i in range(0,len(ZTest)):
        plt.plot(InputTrian[i][0],InputTrian[i][1],"o", c=color[ZTest[i]], mfc = "none")


if __name__ == "__main__":
    File_path = ".\\dataset\\iris.csv" # window file path
    split_train_test = 0.5
    InputTrian,OutputTrian,InputTest,OutputTest = get_iris_dataset.load_iris_dataset(File_path,split_train_test)

    plt.figure(1)
    rate = []
    K = range(1,len(InputTrian)+1)

    for k in K:
        ZTest = kNN(InputTrian,OutputTrian,InputTest,k)
        plot_data(InputTrian,OutputTrian,InputTest,OutputTest,ZTest)
        plt.title("k = " + str(k))
        plt.draw()
        plt.pause(0.001)
        plt.cla()
        rate.append(np.sum(ZTest == OutputTest) / len(OutputTest) * 100)
    
    plt.figure(2)
    plt.plot(K,rate)
    plt.axis([0,80,30,100])
    plt.xlabel("k")
    plt.ylabel("Accuracy rate (%)")
    plt.grid(True)
    plt.show()
    print(rate)

    plt.figure(3)
    k = rate.index(max(rate)) + 1
    ZTest = kNN(InputTrian,OutputTrian,InputTest,k)
    plot_data(InputTrian,OutputTrian,InputTest,OutputTest,ZTest)
    plt.title("k = " + str(k))
    plt.show()