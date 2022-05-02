import numpy as np
from scipy.stats import linregress
from sklearn.linear_model import LinearRegression
import random as rd

# dir_text is '/Users/yiqingmelodywang/Desktop/CMU/Murphy Lab'
'''

Get keysIdx[_][1] (second channel in taskRegexDict) background
Get spillover from first to second channel in taskRegexDict

secCh = firstCh * spillover + secChBackground
'''
def LinReg(keysIdx, values):
    # there should only be one condition so first index is 0
    firstChImg = values[keysIdx[0][0]]
    secondChImg = values[keysIdx[0][1]]

    model = LinearRegression()
    lm_coeff, lm_intercept = [],[]

    assert len(firstChImg) == len(secondChImg), "missing images, number of images in the two sec channels don't match up"
    #FIXME: build in something to check that the firstChImg[i] and secondChImg[i] come from the same field in the same well

    imgShape = firstChImg[0].shape
    for i in range(len(firstChImg)):
        # randThousand = rd.sample(range(imgShape[0]*imgShape[1]),50000)
        # x = firstChImg[i].reshape(imgShape[0]*imgShape[1])[randThousand]
        # y = secondChImg[i].reshape(imgShape[0]*imgShape[1])[randThousand]
        x = firstChImg[i]
        y = secondChImg[i]
        lm = model.fit(x.reshape(-1,1),y.reshape(-1,1))
        lm_coeff.append(lm.coef_)
        lm_intercept.append(lm.intercept_)

    return lm_coeff, lm_intercept


# %%
# %%
