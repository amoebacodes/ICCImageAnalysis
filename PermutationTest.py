import copy
import numpy as np
from MandersFormula import *
from matplotlib import pyplot as plt
def PermutationTest(seg_g, seg_r):
    """
    input: seg_g: green channel of the segmented image, should be a vector
           seg_r: red channel of the segmented image, should be a vector of the same size as seg_g
           
    output: histogram distribution of Mander's overlap coefficient after the permutation test
    
    The permutation test repeats shuffling values in one channel while keeping the other the same and calculating MOC
    """
    moc = [] # to be appended and returned
    
    # initializing values
        # create copies because np.random.Generator.shuffle does not return anything but alters the array passed in
    seg_g_copy = copy.deepcopy(seg_g)
    seg_r_copy = copy.deepcopy(seg_r) 
    
    # np.random.Generator
    rng = np.random.default_rng()
    
    # shuffling green channel
    for i in range(100):
        rng.shuffle(seg_g_copy)
        moc.append(calculate_manders_coefficient(seg_g_copy, seg_r_copy)[0])
        seg_g_copy = copy.deepcopy(seg_g) # so that when it exits the for loop, seg_g_copy is not shuffled; for the next for loop
    
    # shuffling red channel
    for i in range(100):
        rng.shuffle(seg_r_copy)
        moc.append(calculate_manders_coefficient(seg_g_copy, seg_r_copy)[0])
        seg_r_copy = copy.deepcopy(seg_r)
    
    # take a look
    plt.hist(moc)
    plt.show()
#     print("avg: %.2f"% (sum(moc)/len(moc)))
    
    return moc