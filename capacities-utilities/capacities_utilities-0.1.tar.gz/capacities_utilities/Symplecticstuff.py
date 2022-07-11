import numpy as np
from .Quaternionstuff import Quaternion

class Symplectic:
	#obtains the third element of a numpy array
	def getThird(arr):
		return arr[2]
	
	#removing elements of one list from another
	def subtraction(list1, list2):
		temp1 = []
		for i in range(0,len(list1)):
			belongs = 0
			for j in range(0,len(list2)):
				if (list1[i]==list2[j]).all():
					belongs = 1
			if belongs != 1:
				temp1.append(list1[i])
		return temp1
	
	#checks to see if all elements in a list have the same sign
	def same_sign(x):
		geq = np.all(np.greater_equal(np.array(x),np.zeros(len(x))))
		leq = np.all(np.less_equal(np.array(x), np.zeros(len(x))))
		if geq == 0 and leq == 0:
			return 0
		else:
			return 1
	#a function that takes a list of arrays and gets symplectic area of convex polygon
	def symp_area(points):
		sum = 0
		for i in range(1, len(points)-1):
			sum+=0.5*omega(points[i]-points[0], points[i+1]-points[0])
		return sum
	
	#takes 2d arrays and makes a linear map in standard form
	def myFunc(x, y):
		return lambda z: (y[0]-x[0])*(z[1]-y[1])-(y[1]-x[1])*(z[0]-y[0])
	
	# the function described above
	# WORKS ON A LIST OF POINTS IN A PLANE!!!!! NOT ANY POINTS IN R^4
	
	# (did some work to show that you can use the changed coordinates instead)
	# (that is, if you have points of the form av+bJ0v+cK0v+dL0v in the v-J(v)  )
	# (plane, we can do the computation in R^2 on the vectors np.array([a, b]))
	
	def convexify(list):
		
		bad_points = []
		
		for i in range(0,len(list)):
			compare = []
			for j in range(0,len(list)):
				if (list[i]==list[j]).all():
					pass
				else:
					line = myFunc(list[i],list[j])
					vals = []
					for k in range(0,len(list)):
						vals.append(line(list[k]))
					compare.append(same_sign(vals))
			if sum(compare)==0:
				bad_points.append(list[i])
		
		temp = subtraction(list, bad_points)
		
		keyed = []
		for z in temp:
			keyed.append(np.array([z[0], z[1], np.angle(complex(z[0], z[1]))]))
		
		keyed.sort(key=getThird)
	
		temp = []
	
		for z in keyed:
			temp.append(np.array([z[0], z[1]]))
		return temp

	#symplectic/quaternionic structure

	#J_0 definition (left multiplication by i)
	J0 = Quaternion.rotation(Geometry.e2, Geometry.e1)
	
	#K_0 definition (left multiplication by j)
	K0 = Quaternion.rotation(Geometry.e3, Geometry.e1)
	
	#L_0 definition (left multiplication by k)
	L0 = Quaternion.rotation(Geometry.e4, Geometry.e1)
	
	#symplectic form on R^4
	def omega(u,v):
		return np.dot(u, J0(v))
	
	#symplectic form on R^2
	def omega_2(u,v):
		return u[1]*v[0]-u[0]*v[1]
	
	#function that computes the symplectic area of the shadow of a convex polytope from corners
	def symp_area(points):
		sum = 0
		for i in range(1, len(points)-1):
			sum+=0.5*omega(points[i]-points[0], points[i+1]-points[0])
		return sum
	
	#same function but for R^2
	def symp_area_2(points):
		sum = 0
		for i in range(1, len(points)-1):
			sum+=0.5*omega_2(points[i]-points[0], points[i+1]-points[0])
		return sum
	
	#given unit vector v, returns basis {v, Iv, Jv, Kv}
	def symp_basis(v):
		M = np.array([v, J0(v), K0(v), L0(v)])
		return np.matrix.transpose(M)
	
	#gets the v and J(v) coordinates for a vector x
	def get_coordinates(v):
		return lambda x : np.array([np.dot(x, v), np.dot(x, J0(v))])