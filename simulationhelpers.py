import colorsys
import numpy as np
 
def HSVToRGB(h, s, v):
    (r, g, b) = colorsys.hsv_to_rgb(h, s, v)
    return (int(255*r), int(255*g), int(255*b))
 
def getDistinctColors(n):
    ret = []
    huePartition = 1.0 / (n + 1)
    for value in range(0, n):
        HSVToRGB(huePartition * value, 1.0, 1.0)
        ret.append(HSVToRGB(huePartition * value, 1.0, 1.0)) 
    return ret

def angle_between_rad_vec(rad, vec):
    ang1 = rad
    ang2 = np.arctan2(*vec[::-1])
    angle_360 = np.rad2deg((ang1 - ang2) % (2 * np.pi))
    if angle_360 <= 180:
        return angle_360
    else:
        return -1*(360 - angle_360)


def get_bee_2D_vision(posX, posY, orientation, neighbour_positions, max_visual_range, num_bins = 36):
    """
    Seperate environment of an agent into bins and find nearest neighbour for all bins.
    """
    bins = np.zeros(num_bins)
    borders = np.linspace(-180, 180, num_bins + 1)
    sight_vectors = [neighbour_pos[:2] - np.array([posX, posY]) for neighbour_pos in neighbour_positions]
    angles = [[angle_between_rad_vec(orientation, sight_vector), sight_vector] for sight_vector in sight_vectors]
    for angle in angles:
        if (np.linalg.norm(angle[1])!=0):
            for i in range(len(borders)-1):
                if angle[0] <= borders[i+1]:
                    bins[i] = max([bins[i], (max_visual_range - np.linalg.norm(angle[1]))/max_visual_range]) 
                    break
    return bins



