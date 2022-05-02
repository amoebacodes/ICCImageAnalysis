from MandersFormula import *
from PermutationTest import *
from scipy import stats
import numpy as np

def MandersPValPerCell(seg, sec1, sec2):
    """
    for local perm test
    input: seg: segmentation mask from SeededWatershed
           comp: composite image
    output: average Mander's overlap coefficient
    """

    manders_pVal = np.array([])
    
    for i in range(1, seg.max() + 1):
        if i in seg and (sum(sum(seg == i)) > 10): # if the field exists and is greater than 10 pixels
            # get green and red signals in the segmented field
            seg_g = sec1[seg == i]
            seg_r = sec2[seg == i]
            
            # calculate moc for this field
            this_moc = calculate_manders_coefficient(seg_g, seg_r)[0]
            print(this_moc)
            
            # do permutation test on the field; get all (200) moc values from test
            perm_moc = PermutationTest(seg_g, seg_r)
            
            # convert to nparray
            perm_moc = np.array(perm_moc)
            
            # Get empirical p value
            emp_pVal = sum(perm_moc > this_moc) / perm_moc.size
            manders_pVal = np.append(manders_pVal, emp_pVal)
    
    return manders_pVal
        
    