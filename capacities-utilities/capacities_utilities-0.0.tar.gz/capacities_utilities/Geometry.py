import numpy as np

class Cube:

	#perturbation vector to move origin so that projections
	#don't always contain the origin (issue with the complex argument on the plane)
	EPSILON = np.empty(4)
	EPSILON.fill(0.5)
	
	#the corners
	c1 = e1-EPSILON
	c2 = e2-EPSILON
	c3 = e3-EPSILON
	c4 = e4-EPSILON
	c5 = e1+e2-EPSILON
	c6 = e1+e3-EPSILON
	c7 = e1+e4-EPSILON
	c8 = e2+e3-EPSILON
	c9 = e2+e4-EPSILON
	c10 = e3+e4-EPSILON
	c11 = e1+e2+e3-EPSILON
	c12 = e1+e2+e4-EPSILON
	c13 = e1+e3+e4-EPSILON
	c14 = e2+e3+e4-EPSILON
	c15 = e1+e2+e3+e4-EPSILON
	c16 = np.array([0.0, 0.0, 0.0, 0.0])-EPSILON
	
	corners = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16]