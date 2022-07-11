import numpy as np

class Der:
	#std basis of R^4
	e1 = np.array([1.0,0.0,0.0,0.0])
	e2 = np.array([0.0,1.0,0.0,0.0])
	e3 = np.array([0.0,0.0,1.0,0.0])
	e4 = np.array([0.0,0.0,0.0,1.0])
	
	# some utilities to get a hessian matrix/partial derivatives numerically
	EPSILON_0 = .000000000001
	
	def pd1(A):
		return lambda x : (A(x+EPSILON_0*e1)-A(x-EPSILON_0*e1))/(2*EPSILON_0)
	
	def pd2(A):
		return lambda x : (A(x+EPSILON_0*e2)-A(x-EPSILON_0*e2))/(2*EPSILON_0)
	
	def pd3(A):
		return lambda x : (A(x+EPSILON_0*e3)-A(x-EPSILON_0*e3))/(2*EPSILON_0)
	
	def pd4(A):
		return lambda x : (A(x+EPSILON_0*e4)-A(x-EPSILON_0*e4))/(2*EPSILON_0)
	
	def D(f, x):
		return np.array([pd1(f)(x), pd2(f)(x), pd3(f)(x), pd4(f)(x)])
	
	def H(f, x):
		row1 = np.array([pd1(pd1(f))(x), pd1(pd2(f))(x), pd1(pd3(f))(x), pd1(pd4(f))(x)])
		row2 = np.array([pd2(pd1(f))(x), pd2(pd2(f))(x), pd2(pd3(f))(x), pd2(pd4(f))(x)])
		row3 = np.array([pd3(pd1(f))(x), pd3(pd2(f))(x), pd3(pd3(f))(x), pd3(pd4(f))(x)])
		row4 = np.array([pd4(pd1(f))(x), pd4(pd2(f))(x), pd4(pd3(f))(x), pd4(pd4(f))(x)])
		hessian = np.array([row1, row2, row3, row4])
		return hessian
	
	#returning lambda functions to reduce number of arguments assuming we can pass a map f
	def hessian(f):
		return lambda x : H(f,x)
	
	def der(f):
		return lambda x : D(f,x)