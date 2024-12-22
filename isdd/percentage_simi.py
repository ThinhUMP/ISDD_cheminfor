import numpy as np

def get_percentage_simi(similarity_matrix, threshold_min, threshold_max):
    conditional_matrix = (similarity_matrix > threshold_min) & (similarity_matrix <= threshold_max)
    percentage = round(np.mean(conditional_matrix) * 100, 2)
    return percentage