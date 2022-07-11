import numpy as np

class Quaternion:
	#takes two 1 by 4 numpy arrays as vectors in R^4 and multiplies them as quaternions
	def qmultiply(x,y):
		z0 = x[0]*y[0]-x[1]*y[1]-x[2]*y[2]-x[3]*y[3]
		z1 = x[0]*y[1]+y[0]*x[1]+x[2]*y[3]-y[2]*x[3]
		z2 = x[0]*y[2]+y[0]*x[2]+x[3]*y[1]-y[3]*x[1]
		z3 = x[0]*y[3]+y[0]*x[3]+x[1]*y[2]-y[1]*x[2]
		return np.array([z0,z1,z2,z3])
	
	#given two unit quaternions p and q, this instantiates an element of SO(4) as pxq
	def rotation(p,q):
		return lambda x : qmultiply(p, qmultiply(x, q))
