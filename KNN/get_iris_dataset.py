import pandas as pd
import os
import numpy as np

def load_iris_dataset(File_path,split_train_test):
    if os.path.isfile(File_path): # load data set from file path
        iris = pd.read_csv(File_path)
    else: # load data set from website
        url = "http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
        iris = pd.read_csv(url,header=None)
        iris.to_csv(File_path,index=False)
    
    input_set = iris.iloc[:,:4].values
    output_set = iris.iloc[:,-1].values

    if split_train_test:
        classes = np.unique(output_set)
        itrain = np.empty((0,), dtype=np.int)
        itest = np.empty((0,), dtype=np.int)
        for i in classes:
            idx = np.where(output_set == i)[0]
            split = int(len(idx) * split_train_test)
            itrain = np.concatenate((itrain,idx[:split]))
            itest = np.concatenate((itest,idx[split:]))
        return input_set[itrain],output_set[itrain],input_set[itest],output_set[itest]

    return input_set, output_set

if __name__ == "__main__":
    File_path = ".\\dataset\\iris.csv" # window file path
    split_train_test = 0
    input_dataset , output_dataset = load_iris_dataset(File_path,split_train_test)
    print(input_dataset)
    print(output_dataset)