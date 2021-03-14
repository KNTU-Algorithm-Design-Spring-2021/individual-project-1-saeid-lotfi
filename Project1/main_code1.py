#importing libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

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

#performing min_max function on both features
#from generated dataset
hor_min, hor_max = min_max(dataset[:,0])
ver_min, ver_max = min_max(dataset[:,1])


#showing result
#scatter points and boundry lines
fig, ax = plt.subplots()
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.scatter(dataset[:,0], dataset[:,1], s= 5, c= 'r')
ax.add_patch(Rectangle((hor_min, ver_min), hor_max - hor_min, ver_max - ver_min,
                       edgecolor = 'g', fill= False, lw= 2))