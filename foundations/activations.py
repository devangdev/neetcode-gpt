import numpy as np



class Solution:
    
    def sigmoid(self, z: [np.float64]) -> [np.float64]:
        # z is a 1D NumPy array
        # Formula: 1 / (1 + e^(-z))
        # return np.round(your_answer, 5)
        ans=1/(1+np.exp(-z)) 
        return np.round(ans,5)
        pass

    def relu(self, z: [np.float64]) -> [np.float64]:
        # z is a 1D NumPy array
        # Formula: max(0, z) element-wise
        return np.maximum(0,z)
        pass
