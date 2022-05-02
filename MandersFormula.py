import copy
import numpy as np
import math

def calculate_manders_coefficient(image_for_protein1, image_for_protein2):
    """
    Function to calculate Manders Coefficients as a quantification for colocalization
    input:
        green and red channels in a segmented image, area corresponding to one cell
    
    output:
        manders_overlap_coeffient
        image_for_protein1_to_image_for_protein2_fractional_overlap
        image_for_protein2_to_image_for_protein1_fractional_overlap
    
    """
    image_for_protein1 = image_for_protein1.astype('float64')
    image_for_protein2 = image_for_protein2.astype('float64')
    image_for_protein1_copy = copy.deepcopy(image_for_protein1)
    image_for_protein2_copy = copy.deepcopy(image_for_protein2)

    image_for_protein1_copy[image_for_protein2 == 0] = 0
    image_for_protein2_copy[image_for_protein1_copy == 0] = 0
    
    manders_overlap_coefficient = np.dot(image_for_protein1, image_for_protein2) / (
        math.sqrt(np.dot(image_for_protein1, image_for_protein1)) * 
        math.sqrt(np.dot(image_for_protein2, image_for_protein2))
    )

    image_for_protein1_to_image_for_protein2_fractional_overlap = np.sum(
        image_for_protein1_copy
    ) / np.sum(image_for_protein1)

    image_for_protein2_to_image_for_protein1_fractional_overlap = np.sum(
        image_for_protein2_copy
    ) / np.sum(image_for_protein2)

    return (
        manders_overlap_coefficient,
        image_for_protein1_to_image_for_protein2_fractional_overlap,
        image_for_protein2_to_image_for_protein1_fractional_overlap,
    )