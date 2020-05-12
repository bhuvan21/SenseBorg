import numpy as np

def unit_vector(vector):
    return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    sf = 1
    if v2_u[0] > 0:
        sf = -1
    return sf*np.degrees(np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0)))