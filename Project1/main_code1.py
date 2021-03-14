#importing libraries
import numpy as np
import matplotlib.pyplot as plt

#generating random dataset for testing
#making 10000 points and sampling 100 points
dataset = np.random.normal(0, 1, size= [10000,2])
index = np.random.choice(dataset.shape[0], size=100, replace= False)
dataset = dataset[index]

#min_max function
#take a list and return its min and max
def min_max(given_list):
    min_list = given_list[0]
    max_list = given_list[0]
    for i in range(1, len(given_list)):
        if given_list[i] < min_list:
            min_list = given_list[i]
        elif given_list[i] > max_list:
            max_list = given_list[i]
            
    return min_list, max_list
            

#generating random 2d datapoints
#using numpy


#performing min_max function on both features
#from generated dataset


#showing result
#scatter points and boundry lines
