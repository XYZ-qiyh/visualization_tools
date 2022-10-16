import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.interpolate import make_interp_spline
# ref_link: https://www.geeksforgeeks.org/how-to-plot-a-smooth-curve-in-matplotlib/


if __name__ == "__main__":
    depth_values = np.array([778.44104, 781.4538,  784.4666,  787.4794,  790.4922,  793.50494, 796.51776, 799.5305])
    cost = np.array([8.576469,  2.8681326, 8.20096,   3.2029765, 5.3233943, 2.0880067, 3.2086258, 2.1498036])
    print(len(depth_values))
    print(len(cost))    
    
    def gauss_function(x, mean, c):
        return np.exp(-1*(x-mean)**2/(2*c*c))
    
    prior_depth = 789.6
    c = 2*2*4
    k = 10
    modulating_value = k * (1 - gauss_function(depth_values, prior_depth, c))
    cost_modulated = cost * modulating_value
    cost_modulated = np.clip(cost_modulated, 0, 10)
    
    #plt.plot(depth_values, cost)
    #plt.plot(depth_values, modulating_value)
    #plt.plot(depth_values, cost_modulated)
    
    
    depth_values_new = np.linspace(depth_values.min(), depth_values.max(), 80)
    cost_model = make_interp_spline(depth_values, cost)
    cost_new = cost_model(depth_values_new)
    
    modulating_model = make_interp_spline(depth_values, modulating_value)
    modulating_value_new = modulating_model(depth_values_new)
    
    
    cost_modulated_new = cost_new * modulating_value_new
    cost_modulated_new = np.clip(cost_modulated_new, 0, 10)
    
    plt.plot(depth_values_new, cost_new, color = "blue", linestyle="dotted", label = "Before modulating")
    plt.plot(depth_values_new, modulating_value_new, color = "black", label = "Gaussian modulation function")
    plt.plot(depth_values_new, cost_modulated_new, color = "red", linestyle="dashed", label = "After modulating")
    plt.axvline(x=prior_depth, color = "brown", ls='dashdot', label='Prior depth')
    
    plt.xlabel('depth hypothesis')
    plt.ylabel('photometric cost')
    
    plt.legend()
    plt.grid()
    
    plt.savefig("gauss_modulate.png", bbox_inches='tight', pad_inches=0.05, dpi=300)
    plt.show()
