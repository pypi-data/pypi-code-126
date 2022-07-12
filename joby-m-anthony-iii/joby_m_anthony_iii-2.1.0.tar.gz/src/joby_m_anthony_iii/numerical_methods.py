#################################
## Preamble
# import necessary modules/tools
# import extension as ex
import inspect
import math
import numpy as np
import pandas as pd
import scipy as sc
import sympy as sp
import sys
from typing import Optional, Tuple, Union
from types import FunctionType
#   #   #   #   #   #   #   #   #

#logging.basicConfig(format = "%(messages)s")
#log = logging.getLogger()

#################################
## Universal Variables/Methods/Classes
# common functions
def _retrieve_name(var):
	"""https://stackoverflow.com/questions/18425225/getting-the-name-of-a-variable-as-a-string
	"""
	callers_local_vars = inspect.currentframe().f_back.f_back.f_locals.items()
	return [var_name for var_name, var_val in callers_local_vars if var_val is var]

def _retrieve_expression(expression):
	expression_str = str(inspect.getsourcelines(expression)[0]).strip("['\\n']").split(" = ")[1]
	return expression_str[expression_str.find(": ")+2:]

def diagonality(
	A: tuple
) -> bool:
	"""Determines if matrix is strictly, diagonally dominant.

	Parameters
	----------
	A : tuple
		Input matrix to be tested.

	Returns
	-------
	is_strict_diagonal_matrix : bool
		Truth value whether matrix is strictly, diagonally dominant.

	Raises
	------
	IndexError
		Matrix of interest must be square.

	Warnings
	--------
	Will print to console either if strictly, diagonally dominant, or if matrix, `A` is not strictly, diagonally dominant which could lead to poor solution of 'Ax = b'.
	"""
	matrix_name, A = _retrieve_name(A), np.array(A)
	if not(np.sum(A.shape) - A.shape[0] == A.shape[0]):
		raise IndexError(f"ERROR! Matrix, '{matrix_name}' must be square!")
	i, diags, long = 0, np.zeros_like(A), np.zeros_like(A)
	while i < len(A):
		j = 0
		while j < len(A):
			aij = A[i][j]
			if i == j: long[i][j] = aij
			else: diags[i][j] = aij
			j += 1
		i += 1
	if np.sum(long) >= np.sum(diags):
		# print(f"Information: Matrix, {matrix_name} is strictly, diagonally dominant.")
		is_strict_diagonal_matrix = True
	else:
		# print(f"Warning! Matrix, {matrix_name} is not strictly, diagonally dominant. Solution may be inaccurate.")
		is_strict_diagonal_matrix = False
	# is_strict_diagonal_matrix = ex.fast_diagonality(A)
	return is_strict_diagonal_matrix

def eigen_values(
	A: tuple
) -> np.ndarray:
	"""Directly finds eigenvalues of matrix by its determinant. Not recommended for large, sparse matrices.

	Parameters
	----------
	A : tuple
		Matrix of interest.

	Returns
	-------
	lambdas : np.ndarray
		Eigenvector containing roots.

	Raises
	------
	IndexError
		Matrix of interest must be square.
	"""
	# See Also
	# --------
	matrix_name, A = _retrieve_name(A), np.array(A)
	# -------------- TODO: Fix this -------------- #
	if not(np.sum(A.shape) - A.shape[0] == A.shape[0]):
		raise IndexError(f"ERROR! Matrix, '{matrix_name}' must be square!")
	sym_r = sp.Symbol("r")
	i, identityA = 0, np.zeros_like(A)
	while i < len(A):
		j = 0
		while j < len(A[0]):
			if i == j: identityA[i][j] = 1
			j += 1
		i += 1
	lambda_identity = identityA*sym_r
	determinant = sp.det(sp.Matrix(A - lambda_identity))
	roots = sp.solve(determinant)
	#roots = ex.fast_eigen_values(A)
	##reals, complexes = roots
	# -------------------------------------------- #
	lambdas = []
	for r in roots:
		r = complex(r)
		if np.imag(r) == 0: r = np.real(r)
		lambdas.append(r)
	#for c in complexes:
	#	if c == 0: lambdas.append(reals[complexes.index(c)])
	#	else: lambdas.append(complex(reals[complexes.index(c)], c))
	return np.array(lambdas)

# preceded by eigen_values

def spectral_radius(
	A: tuple
) -> float:
	"""Finds the spectral radius of matrix.

	Parameters
	----------
	A : tuple
		Matrix of interest.

	Returns
	-------
	rho : float
		Spectral radius.

	Raises
	------
	IndexError
		Matrix of interest must be square.

	See Also
	--------
	EigenValues().qr_algorithm() : Function to find eigenvector of matrix according to QR Algorithm.
	"""
	matrix_name, A = _retrieve_name(A), np.array(A)
	if not(np.sum(A.shape) - A.shape[0] == A.shape[0]):
		raise IndexError(f"ERROR! Matrix, '{matrix_name}' must be square!")
	#rho = np.max(np.abs(eigen_values(A)))
	rho = np.max(np.abs(EigenValues(A).qr_algorithm()["Lambdas"].values[-1]))
	return rho

# preceded by spectral_radius

class norms:
	"""Find the natural norm of a vector or between two vectors.
	"""
	def __init__(
		self,
		x: tuple,
		x0: Optional[tuple]=None
	):
		"""
		Parameters
		----------
		x : tuple
			Newly approximated array.

		x0 : tuple, optional
			Previously approximated array.

		Yields
		------
		self.x : np.ndarray
			Newly approximated array.

		self.x0 : np.ndarray
			Previously approximated array.

		Raises
		------
		IndexError
			If the input vectors are not the same length.
		"""
		self.__vector_name, self.x = _retrieve_name(x), np.array(x)
		if not isinstance(x0, type(None)):
			self.__old_vector_name, self.x0 = _retrieve_name(x0), np.array(x0)
			if not(self.x0.shape[0] == 0 or len(x) == len(x0)):
				raise IndexError(f"ERROR! '{self.__vector_name}' and '{self.__old_vector_name}' must be the same size!")
		else: self.__old_vector_name, self.x0 = "x0", x0

	# @nb.jit(nopython=True)
	def l_infinity(
		self
	) -> float:
		"""Maximum difference between absolute sum of i'th rows.

		Returns
		-------
		norm : float
			Scalar value.

		Yields
		------
		self.norm : float
			Scalar value.

		Notes
		-----
		Best thought as "actual" distance between vectors.

		Also calculates infinity norm of matri(x/ces).

		Examples
		--------
		[x0] = (1, 1, 1)^(t)

		[x] = (1.2001, 0.99991, 0.92538)^(t)

		||x0 - x|| = max{|1 - 1.2001|, |1 - 0.99991|, |1 - 0.92538|}

		||x0 - x|| = 0.2001
		"""
		# evaluate and store norm, ||.||
		vec_name, x = self.__vector_name, self.x
		old_vec_name, x0 = self.__old_vector_name, self.x0
		# initialize loop
		norm_tpl = np.zeros_like(x, dtype=float)
		if isinstance(x0, type(None)):
			if np.sum(x.shape) == x.shape[0]:
				for i in range(x.shape[0]):
					norm_tpl[i] = abs(x[i])
			elif np.sum(x.shape) > x.shape[0]:
				for i in range(x.shape[0]):
					for j in range(x.shape[1]):
						norm_tpl[i] += abs(x[i][j])
		elif len(x) == len(x0):
			if np.sum(x0.shape) == x0.shape[0]:
				for i in range(x0.shape[0]):
					norm_tpl[i] = abs(x[i] - x0[i])
			elif np.sum(x0.shape) > x0.shape[0]:
				if np.sum(x.shape) > x.shape[0]:
					for i in range(x0.shape[0]):
						for j in range(x0.shape[1]):
							norm_tpl[i] += float(abs(x[i][j] - x0[i][j]))
				elif np.sum(x.shape) == np.sum(x0.shape):
					for i in range(x0.shape[0]):
						norm_tpl[i] = abs(x[i] - x0[i])
		else:
			raise IndexError(f"ERROR! {vec_name}, and {old_vec_name} must be the same size!")
		# if no errors, then evaluate norm
		self.norm = norm = np.amax(norm_tpl)
		# if isinstance(self.x0, type(None)):
		# 	self.norm = norm = ex.fast_l_infinity(self.x)
		# else:
		# 	self.norm = norm = ex.fast_l_infinity(self.x, self.x0)
		return norm # return the l_infinity norm

	# @nb.jit(nopython=True)
	def l_two(
		self
	) -> float:
		"""Square root of sum of differences squared along i'th row.

		Returns
		-------
		norm : float
			Scalar value.

		Yields
		------
		self.norm : float
			Scalar value.

		See Also
		--------
		spectral_radius() : Function to find the spectral radius of vector.

		Examples
		--------
		[x0] = (1, 1, 1)^(t)

		[x] = (1.2001, 0.99991, 0.92538)^(t)

		||x0 - x|| = sqrt[ (1 - 1.2001)^2 \
			+ (1 - 0.99991)^2 + (1 - 0.92538)^2 ]

		||x0 - x|| = 0.21356
		"""
		if isinstance(self.x0, type(None)):
			if np.sum(self.x.shape) == self.x.shape[0]:
				discriminant = np.sum(self.x**2)
			elif np.sum(self.x.shape) > self.x.shape[0]:
				discriminant = spectral_radius(np.matmul(self.x.transpose(), self.x))
		else:
			vec = self.x - self.x0
			if np.ndim(vec) == 1:
				discriminant = np.sum(vec**2)
			else:
				discriminant = spectral_radius(np.matmul(vec.transpose(), vec))
		# evaluate and store norm, ||.||
		self.norm = norm = math.sqrt(discriminant)
		return norm # return the l_two norm

# preceded by norms.()l_infinity() and norms().l_two()

def condition_number(
	A: tuple,
	norm_type: Optional[str]="l_two"
) -> float:
	"""Find the condition number of a given matrix and norm type.

	Parameters
	----------
	A : tuple
		Input matrix for analysis.

	norm_type : string, optional
		Selects norm comparison which is 'l_two' by default.

	Returns
	-------
	K : float
		Condition number of matrix, A.

	Raises
	------
	ValueError
		If input `norm_type` is not understood as neither 'l_infinity' nor 'l_two'.

	Warnings
	--------
	Will output evaluation of condition number and show in console.

	See Also
	--------
	norms().l_two() : Method that yields the l_two norm.

	norms().l_infinity() : Method that yields the l_infinity norm.
	"""
	matrix_name, A = _retrieve_name(A), np.array(A)
	BadNormTypeError = lambda norm_type: f"ERROR! Input `norm_type`='{norm_type}' not understood. Please input 'l_infinity' or 'l_two'."
	i, A_inv = 0, np.zeros_like(A)
	while i < len(A):
		j = 0
		while j < len(A):
			aij = A[i][j]
			if aij != 0: A_inv[i][j] = 1/aij
			j += 1
		i += 1
	if norm_type == "l_infinity":
		norm, abnorm = norms(A).l_infinity(), norms(A_inv).l_infinity()
		# norm, abnorm = ex.fast_l_infinity(A), ex.fast_l_infinity
	elif norm_type == "l_two":
		norm, abnorm = norms(A).l_two(), norms(A_inv).l_two()
	else: raise ValueError(BadNormTypeError(norm_type))
	K = norm*abnorm
	#print(f"Information: Condition Number K('{matrix_name}') = {k}")
	return K

def make_array(
	domain: tuple,
	function: FunctionType
	# variable: Optional[str]="x"
) -> np.ndarray:
	"""Maps domain to range.

	Parameters
	----------
	domain : tuple
		Collection if input data.

	function : lambda
		Function that maps the domain to range.

	variable : string, optional
		String representation of variable to respect in function.

	Returns
	-------
	mapped : np.ndarray
		Mapped range from function.

	Warnings
	--------
	Prints to console the input expression, and that the expression was in fact used.

	Notes
	-----
	If the input function happens to already be a NumPy array, then that array will simply be returned without processing.
	"""
	function_name = _retrieve_name(function)
	BadFunctionError = lambda function_name: f"ERROR! '{function_name}' must be a lambda expression or LaTeX formatted equation."
	if isinstance(function, (list, tuple, np.ndarray)):
		mapped = np.array(function)
	else:
		# if isinstance(function, str):
		# 	function_str = ex.fast_parse_latex(function)
		# 	function = lambda x: ex.fast_eval_latex(function_str, {variable: x})
		# else:
		if not isinstance(function, (FunctionType)): raise TypeError(BadFunctionError(function_name))
		domain, mapped = np.array(domain), np.zeros_like(domain)
		for i in range(len(domain)):
			if np.sum(domain.shape) > np.sum(domain.shape[0]):
				for j in range(len(domain[0])):
					mapped[i][j] = (function(domain[i][j]))
			else: mapped[i] = function(domain[i])
	return mapped

def symmetry(
	A: tuple
) -> bool:
	"""Determines boolean truth value whether given matrix is symmetric.

	Parameters
	----------
	A : tuple
		Matrix of interest.

	Returns
	-------
	is_symmetric : bool
		True if symmetric, else False.

	Raises
	------
	IndexError
		Matrix of interest must be square.

	Warnings
	--------
	Console print that A is either symmetric or asymmetric.
	"""
	matrix_name, A = _retrieve_name(A), np.array(A)
	if not(np.sum(A.shape) - A.shape[0] == A.shape[0]):
		raise IndexError(f"ERROR! Matrix, '{matrix_name}' must be square!")
	i, At, is_symmetric = 0, np.transpose(A), False
	for ai in A:
		j = 0
		for aj in ai:
			if aj == At[i][j]: is_symmetric = True
			else:
				is_symmetric = False
				# print(f"Warning! Matrix, {matrix_name} is not symmetric.")
				return is_symmetric
			j += 1
		i += 1
	# if is_symmetric: print(f"Information: Matrix, {matrix_name} is symmetric.")
	# is_symmetric = ex.fast_symmetry(A)
	return is_symmetric

def tridiagonality(
	A: tuple
) -> bool:
	"""Determine boolean truth value whether given matrix is tridiagonal.

	Parameters
	----------
	A : tuple
		Matrix of interest.

	Returns
	-------
	is_tridiagonal : bool
		True if tridiagonal, else False.

	Raises
	------
	IndexError
		Matrix of interest must be square.

	Warnings
	--------
	Prints to console that matrix is either tridiagonal or not.
	"""
	matrix_name, A = _retrieve_name(A), np.array(A)
	if not(np.sum(np.shape(A)) - np.shape(A)[0] == np.shape(A)[0]):
		raise IndexError(f"ERROR! Matrix, '{matrix_name}' must be square!")
	diagonals = np.diagflat(np.diag(A))
	above = np.diagflat(np.diag(A, k=1), k=1)
	below = np.diagflat(np.diag(A, k=-1), k=-1)
	non_A = A - (diagonals + above + below)
	if np.sum(non_A) != 0:
		# print(f"Warning! Matrix, {matrix_name} is not tridiagonal.")
		is_tridiagonal = False
	else:
		# print(f"Information: Matrix, {matrix_name} is tridiagonal.")
		is_tridiagonal = True
	# is_tridiagonal = ex.fast_tridiagonality(A)
	return is_tridiagonal
#   #   #   #   #   #   #   #   #


#################################
## Specific Functions
# --------------------
# eigenvalue solvers
class EigenValues:
	def __init__(
		self,
		A: tuple,
		power: float=-6,
		max_iter: int=100
	):
		"""
		Parameters
		----------
		A : tuple
			Characteristic matrix.

		power : float, optional
			Signed power to which function error must be within.

		max_iter : int, optional
			Maximum iterations for which function may loop.

		Yields
		------
		self.A : tuple
			Input characteristic matrix.

		self.tol : float
			Specified tolerance to which method terminates.

		self.max_iter : int
			Maximum iterations allowed for method.

		self.is_diagonal : bool
			Truth value of whether matrix is diagonal.

		self.is_tridiagonal : bool
			Truth value of whether matrix is tridiagonal.

		Raises
		------
		IndexError
			Matrix of interest must be square.

		ValueError
			If iterations constraint is not an integer.

		Notes
		-----
		Specified tolerance evaluated by `10**power`.

		`norm_type` may be either `'l_infinity'` or `'l_two'` but is 'l_infinity' by default.

		If `self.is_diagonal` is True, then matrix is diagonal. Else, not diagonal.
		"""
		self.__matrix_name = _retrieve_name(A)
		if np.array(A).shape[0] != np.array(A).shape[1]: raise IndexError(f"ERROR! Matrix, {self.__matrix_name} must be square!")
		if max_iter <= 0 or not isinstance(max_iter, (int, float)): raise ValueError(f"ERROR! Maximum iterations, N must be an integer greater than zero. {max_iter} was given and not understood.")
		self.A = A = np.array(A)
		self.tol = float(10**power)
		self.max_iter = int(max_iter)
		self.is_diagonal = diagonality(A)
		self.is_tridiagonal = tridiagonality(A)

	__BadVectorDataError = lambda matrix_name, matrix_size, vector_name, vector_size: "ERROR! {matrix_name} of size {matrix_size} and {vector_name} of size {vector_size} must be the same length!"

	def power_method(
		self,
		x: tuple
	) -> pd.DataFrame:
		"""Approximate the dominant eigenvalue and associated eigenvector of matrix, A given some non-zero vector, x.

		Parameters
		----------
		vector : tuple
			Initial guess for eigenvector.

		Returns
		-------
		pandas.DataFrame : DataFrame
			Summarized dataframe from iterations.

		Yields
		------
		self.vector : np.ndarray
			Initial guess for eigenvector.

		self.iterations : np.ndarray
			Collection of iterations through method.

		self.mu : np.ndarray
			Collection of approximately largest eigenvalue.

		self.lambdas : list
			Collection of approximate eigenvectors.

		self.errors : np.ndarray
			Collection of yielded norms.

		Raises
		------
		IndexError
			If x is not a one-dimensional array.
		"""
		self.__vector_name = _retrieve_name(x)
		if np.sum(np.array(x).shape) - np.array(x).shape[0] > 1: raise IndexError(f"Systems vector, {self.__vector_name} must be one-dimensional array!")
		if len(x) != len(self.A): raise IndexError(EigenValues.__BadVectorDataError(self.__matrix_name, len(self.A), self.__vector_name, len(x)))
		self.x = x = np.array(x)
		mu = [norms(x).l_infinity()]
		x = x/mu[-1]
		k, eigenvectors, errors = 1, [x], [self.tol*10]
		while errors[-1] > self.tol and k <= self.max_iter:
			y = np.matmul(self.A, x)
			for yi in y:
				if abs(yi) == norms(y).l_infinity(): yp = float(yi)
			mu.append(yp)
			eigenvectors.append(y/yp)
			errors.append(norms(x, eigenvectors[-1]).l_infinity())
			x = eigenvectors[-1]; k += 1
		self.iterations = np.arange(k)
		self.mu = np.array(mu)
		#self.lambdas = np.array(eigenvectors)
		self.lambdas = eigenvectors
		self.errors = np.array(errors)
		return pd.DataFrame(data={
			"Iterations": self.iterations,
			"Mu": self.mu,
			"Lambdas":self.lambdas,
			"Errors": self.errors
		})

	def inverse_power_method(
		self,
		x: tuple,
		q: float
	) -> pd.DataFrame:
		"""Approximate eigenvalue closest to target, q and associated eigenvector of matrix, A given some non-zero vector, x.

		Parameters
		----------
		x : tuple
			Initial guess for eigenvector.

		q : float
			Target to which the closest eigenvalue of matrix will be found.

		Returns
		-------
		pandas.DataFrame : DataFrame
			Summarized dataframe from iterations.

		Yields
		------
		self.x : np.ndarray
			Initial guess at eigenvector.

		self.iterations : tuple
			Collection of iterations through method.

		self.mu : tuple
			Collection of approximately largest eigenvalue.

		self.lambdas : list
			Collection of approximate eigenvectors.

		self.errors : tuple
			Collection of yielded norms.

		Raises
		------
		IndexError
			If x is not a one-dimensional array.
		"""
		self.__vector_name = _retrieve_name(x)
		if np.sum(np.array(x).shape) - np.array(x).shape[0] > 1: raise IndexError(f"Systems vector, {self.__vector_name} must be one-dimensional array!")
		if len(x) != len(self.A): raise IndexError(EigenValues.__BadVectorDataError(self.__matrix_name, len(self.A), self.__vector_name, len(x)))
		self.x = x = np.array(x)
		self.q = float(q)
		A = np.linalg.inv(self.A-q*np.identity(len(self.A)))
		mu = [1/norms(x).l_infinity() + q]
		k, eigenvectors, errors = 1, [x], [self.tol*10]
		while errors[-1] > self.tol and k <= self.max_iter:
			y = np.matmul(A, x)
			for yi in y:
				if abs(yi) == norms(y).l_infinity(): yp = float(yi)
			mu.append(1/yp + q)
			eigenvectors.append(y/yp)
			errors.append(norms(x, x0=eigenvectors[-1]).l_infinity())
			x = eigenvectors[-1]; k += 1
		self.iterations = np.arange(k)
		self.mu = np.array(mu)
		#self.lambdas = np.array(eigenvectors)
		self.lambdas = eigenvectors
		self.errors = np.array(errors)
		return pd.DataFrame(data={
			"Iterations": self.iterations,
			"Mu": self.mu,
			"Lambdas": self.lambdas,
			"Errors": self.errors
		})

	def qr_algorithm(self) -> pd.DataFrame:
		"""Approximate dominant eigenvalue and associated eigenvector of matrix, A.

		Source: https://www.youtube.com/watch?v=FAnNBw7d0vg

		Returns
		-------
		pandas.DataFrame : DataFrame
			Summarized dataframe from iterations.

		Yields
		------
		self.iterations : np.ndarray
			Collection of iterations through method.

		self.lambdas : list
			Collection of approximate eigenvectors.

		self.errors : np.ndarray
			Collection of yielded norms.
		"""
		A = self.A
		k, eigenvectors, errors = 1, [np.diag(A)], [self.tol*10]
		while errors[-1] > self.tol and k <= self.max_iter:
			Q = np.zeros_like(A, dtype=float)
			R = np.zeros_like(A, dtype=float)
			QI = []
			for j in range(len(A[0])):
				ai = np.array(np.zeros(len(A)))
				for i in range(len(A)):
					ai[i] = A[i][j]
				ai_perp = 0
				for i in range(j):
					R[i][j] = np.dot(ai, QI[i])
					ai_perp += R[i][j]*QI[i]
				ai -= ai_perp
				R[j][j] = np.sqrt(np.sum(ai**2))
				qi = ai/R[j][j]
				QI.append(qi)
				i = 0
				for q in qi:
					Q[i][j] = q
					i += 1
			A = np.matmul(R, Q)
			eigenvectors.append(np.diag(A))
			err = np.average([norms(np.diag(A, k=-1)).l_infinity(), norms(np.diag(A, k=1)).l_infinity()])
			errors.append(err); k += 1
		self.iterations = np.arange(k)
		#self.lambdas = np.array(eigenvectors)
		self.lambdas = eigenvectors
		self.errors = np.array(errors)
		return pd.DataFrame(data={
			"Iterations": self.iterations,
			"Lambdas": self.lambdas,
			"Errors": self.errors
		})

	def steepest_descent(
		self,
		x: tuple,
		b: tuple
	) -> pd.DataFrame:
		"""Approximate solution vector, x given matrix, A initial guess vector, x, and vector, b.

		Parameters
		----------
		x : tuple
			Initial guess for eigenvector.

		b : tuple
			Vector that is solution to system of equations.

		Returns
		-------
		pandas.DataFrame : DataFrame
			Summarized dataframe from iterations.

		Yields
		------
		self.x : np.ndarray
			Initial guess for eigenvector.

		self.b : np.ndarray
			Vector that is solution to system of equations.

		self.iterations : np.ndarray
			Collection of iterations through method.

		self.lambdas : list
			Collection of approximate eigenvectors.

		self.errors : np.ndarray
			Collection of yielded norms.

		Raises
		------
		IndexError
			If x is not a one-dimensional array.

		IndexError
			If b is not a one-dimensional array.
		"""
		self.__vector_name = _retrieve_name(x)
		if np.sum(np.array(x).shape) - np.array(x).shape[0] > 1: raise IndexError(f"Systems vector, {self.__vector_name} must be one-dimensional array!")
		if len(x) != len(self.A): raise IndexError(EigenValues.__BadVectorDataError(self.__matrix_name, len(self.A), self.__vector_name, len(x)))
		self.x = x = np.array(x)
		self.__solution_name = _retrieve_name(b)
		if np.sum(np.array(b).shape) - np.array(b).shape[0] > 1: raise IndexError(f"Systems vector, {self.__vector_name} must be one-dimensional array!")
		if len(x) != len(self.A): raise IndexError(EigenValues.__BadVectorDataError(self.__matrix_name, len(self.A), self.__solution_name, len(b)))
		self.b = b = np.array(b)
		k, eigenvectors, errors = 1, [x], [self.tol*10]
		while errors[-1] > self.tol and k <= self.max_iter:
			r = b - np.matmul(self.A, x)
			alpha = float(np.matmul(r.T, r)/np.matmul(np.matmul(r.T, self.A), r))
			x1 = x + alpha*r
			eigenvectors.append(x1)
			errors.append(norms(x1, x).l_infinity())
			x = x1; k += 1
		self.iterations = np.array(range(k))
		#self.lambdas = np.array(eigenvectors)
		self.lambdas = eigenvectors
		self.errors = np.array(errors)
		return pd.DataFrame(data={
			"Iterations": self.iterations,
			"Lambdas": self.lambdas,
			"Errors": self.errors
		})

	def conjugate_gradient(
		self,
		x: tuple,
		b: tuple,
		C: Optional[tuple]=None
	):
		"""Approximate solution vector given matrix, A, initial guess vector, x, and vector, b.

		Parameters
		----------
		vector : tuple
			Initial guess for eigenvector.

		solution : tuple
			Vector that is solution to system of equations.

		C : tuple, optional
			Preconditioning matrix.

		Returns
		-------
		pandas.DataFrame : DataFrame
			Summarized dataframe from iterations.

		Yields
		------
		self.vector : np.ndarray
			Initial guess at eigenvector.

		self.solution : np.ndarray
			Input numpy array.

		self.iterations : np.ndarray
			Collection of iterations through method.

		self.lambdas : list
			Collection of approximate eigenvectors.

		self.errors : np.ndarray
			Collection of yielded norms.

		Raises
		------
		IndexError
			If x is not a one-dimensional array.

		IndexError
			If b is not a one-dimensional array.
		"""
		self.__vector_name = _retrieve_name(x)
		if np.sum(np.array(x).shape) - np.array(x).shape[0] > 1: raise IndexError(f"Systems vector, {self.__vector_name} must be one-dimensional array!")
		self.x = x = np.array(x)
		self.__solution_name = _retrieve_name(b)
		if np.sum(np.array(b).shape) - np.array(b).shape[0] > 1: raise IndexError(f"Systems vector, {self.__vector_name} must be one-dimensional array!")
		self.b = b = np.array(b)
		self.C = C
		r0 = b - np.matmul(self.A, x)
		if isinstance(C, type(None)):
			do_precondition = True
			v0 = r0
		else:
			do_precondition = False
			self.C = C = np.array(C)
			Minv = np.linalg.inv(C*np.transpose(C))
			v0 = np.matmul(Minv, r0)
		k, eigenvectors, errors = 1, [x], [self.tol*10]
		while errors[-1] > self.tol and k <= self.max_iter:
			if do_precondition:
				alpha = float(np.matmul(r0.T, r0)/np.matmul(np.matmul(v0.T, self.A), v0))
			else:
				alpha = float(np.matmul(np.matmul(r0.T, Minv), r0)/np.matmul(np.matmul(v0.T, self.A), v0))
			x1 = x + alpha*v0
			eigenvectors.append(x1)
			errors.append(norms(x1, x).l_infinity())
			r1 = r0 - alpha*np.matmul(self.A, v0)
			if do_precondition:
				s1 = float(np.matmul(r1.T, r1)/np.matmul(r0.T, r0))
			else: s1 = float(np.matmul(np.matmul(r1.T, Minv), r1)/np.matmul(np.matmul(r0.T, Minv), r0))
			x, r0 = x1, r1
			if do_precondition: v0 = r1 + s1*v0
			else: v0 = np.matmul(Minv, r1) + s1*v0
			k += 1
		self.iterations = np.array(range(k))
		#self.eigenvectors = np.array(eigenvectors)
		self.lambdas = eigenvectors
		self.errors = np.array(errors)
		return pd.DataFrame(data={
			"Iterations": self.iterations,
			"Lambdas": self.lambdas,
			"Errors": self.errors
		})
# --------------------

# --------------------
# iterative techniques
class SingleVariableIteration:
	"""Given f(x) such that x is in [a, b], find the root of a single-variable, equation within tolerance.
	"""
	def __init__(
		self,
		function: FunctionType,
		a: float,
		b: float,
		power: Optional[float]=-6,
		variable: Optional[str]="x",
		iter_guess: Optional[Union[bool,int]]=True,
		function_slope: Optional[float]=0
	):
		"""
		Parameters
		----------
		function : lambda
			Input function.

		a : float
			Left-hand bound of interval.

		b : float
			Right-hand bound of interval.

		power : float, optional
			Signed, specified power of tolerance until satisfying method.

		variable : string, optional
			Respected variable in derivative. Assumed to be 'x' if not stated.

		iter_guess : bool or integer, optional
			Boolean value of `True` by default. If integer, iterate for that integer.

		function_slope : float, optional
			Absolute maximum slope of function.

		Yields
		------
		self.function : expression
			Input function.

		self.variable : symbol, optional
			Respected variable in derivative. Assumed to be `'x'` if not stated.

		self.a : float
			Left-hand bound of interval.

		self.b : float
			Right-hand bound of interval.

		self.tol : float
			Tolerance to satisfy method.

		self.iter_guess : bool or integer
			Boolean value of `True` by default. If integer, iterate for that integer.

		self.function_slope : float
			Absolute maximum slope of functon. Assumed 0 if not defined.

		Raises
		------
		TypeError
			If input expression cannot be understood as lambda or sympy expression nor as string.

		Notes
		-----
		self.tol evaluated by: `10**power`.
		"""
		self.__function_name = function_name = _retrieve_name(function)
		# if isinstance(function, (str)):
		# 	function_str = ex.fast_parse_latex(function)
		# 	function = lambda x: ex.fast_eval_latex(function_str, {variable: x})
		# 	#print("String expression converted to lambda function.")
		if isinstance(function, (FunctionType)):
			#funcString = str(inspect.getsourcelines(function)[0])
			#funcString = funcString.strip("['\\n']").split(" = ")[1]
			#sym_function_idx = funcString.find(": ")+2
			#sym_function = funcString[sym_function_idx:]
			function_str = "Lambda"
		else: raise TypeError(SingleVariableIteration.__TypeError_Lambda(function_name))
		self.function, self.function_str, self.variable = function, function_str, variable
		self.a, self.b, self.tol = float(a), float(b), float(10**power)
		self.iter_guess, self.function_slope = iter_guess, function_slope

	# __TypeError_String = lambda function_name: f"ERROR! '{function_name}' must be a LaTeX formatted equation of type string."
	__TypeError_Lambda = lambda function_name: f"ERROR! The input function, '{function_name}' must be a lambda expression."
	__MaxIterError = lambda N: f"ERROR! Maximum iterations, N='{N}' must be an integer greater than zero."
	__OppositeSignError_Interval = lambda function_name, f, a, b: f"ERROR! Interval bounds must yield opposite signs in function, '{function_name}':= [f(a={a}) = {f(a)}, f(b={b}) = {f(b)}]"
	__OppositeSignError_Guess = lambda function_name, f, p0, p1: f"ERROR! Interval bounds must yield opposite signs in function, '{function_name}':= [f(p0={p0}) = {f(p0)}, f(p1={p1}) = {f(p1)}]"

	def find_k(
		self
	) -> float:
		"""Find greatest integer for maximum iterations for tolerance.

		Returns
		-------
		k : float
			Maximum possible slope of input function.

		Yields
		------
		self.function_slope : float
			Maximum possible slope of input function.
		"""
		k = self.function_slope
		# determine form of derivative
		# if self.function_str != "Lambda":
		# 	df = lambda x: ex.fast_eval_latex(ex.fast_derive_latex(self.function_str, self.variable), {self.variable: x})
		# else:
		df = sp.lambdify(sp.Symbol(self.variable), sp.diff(self.function(sp.Symbol(self.variable))))
		for alpha in np.linspace(self.a, self.b, int(1e3)):
			if abs(df(alpha)) > k: k = abs(df(alpha))
		self.function_slope = k
		return k

	def max_iterations(
		self,
		method: str,
		p0: Optional[float]=0
	) -> int:
		"""Find greatest integer for maximum iterations within tolerance.

		Parameters
		----------
		method : string
			Selection of iterative method for iterations are needed.

		p0 : float, optional
			Initial guess for function solution. Not needed for 'bisection' method.

		Returns
		-------
		self.max_iter : int
			Maximum number of iterations required for specified tolerance.

		Yields
		------
		self.max_iter : int
			Maximum number of iterations required for specified tolerance.

		Raises
		------
		ValueError
			Prescribed method is not an available option.

		Warnings
		--------
		Informs user the maximum number of iterations for method.

		Notes
		-----
		Will round away from zero to higher integers.

		Examples
		--------
		If `method == 'bisection'` & a=1, b=2, and tol=-3, then:

		`max_iter` >= -log(`tol`/(`b` - `a`))/log(2)

		`max_iter` >= -log((10**(-3)/(2 - 1))/log(2)

		`max_iter` >= 9.96

		`max_iter` = 10

		Else, if a=1, b=2, tol=-3, p0=1.5, nd k=0.9, then:
		`max_iter` >= log(`tol`/max('p0' - `a`, `b` - `p0`))/log(k)

		`max_iter` >= log(10**(-3)/max(1.5 - 1, 2 - 1.5))/log(0.9)

		`max_iter` >= log(10**(-3)/0.5)/log(0.9)

		`max_iter` >= 58.98

		`max_iter` >= 59
		"""
		a, b, k = self.a, self.b, self.function_slope
		p0 = float(p0)
		if method == "bisection":
			self.max_iter = max_iter = math.ceil(-math.log(self.tol/(b - a))/math.log(2))
		elif method in ("fixed_point", "newton_raphson", "secant_method", "false_position"):
			self.max_iter = max_iter = math.ceil(-math.log(self.tol/max(p0 - a, b - p0))/math.log(k))
		else: raise ValueError(f"ERROR! I am sorry. The desired method must be: 'bisection', 'fixed_point', 'newton_raphson', 'secant_method', or 'false_position'.")
		#print(f"Information: With the inputs, I will terminate the technique after so many iterations, N = {max_iter}")
		return self.max_iter

	# next 5 functions preceded by find_k & max_iterations

	def bisection(
		self
	) -> pd.DataFrame:
		"""Root-finding method: f(x) = 0.

		Returns
		-------
		pandas.DataFrame : DataFrame
			Summarized dataframe from iterations.

		Yields
		------
		self.iterations : np.ndarray
			Collection of iterations through method.

		self.approximations : np.ndarray
			Collection of evaluated points, p.

		self.errors : np.ndarray
			Collection of propogated error through method.

		Raises
		------
		ValueError
			If input for desired iterations was assigned not an integer.

		ValueError
			If initial guesses did not evaluate to have opposite signs.

		TypeError
			If input expression cannot be understood as lambda or sympy expression nor as string.

		Warnings
		--------
		Print to console if solution was found, or state that solution did not converge with given guess or prescribed tolerance.

		Notes
		-----
		Relying on the Intermediate Value Theorem, this is a bracketed, root-finding method. Generates a sequence {p_n}^{inf}_{n=1} to approximate a zero of f(x), p and converges by O(1 / (2**N)).

		Examples
		--------
		If  f(x) = x**3 + 4*x**2 = 10

		=>  f(x) = x**3 + 4*x**2 - 10 = 0
		"""
		f, a, b = self.function, self.a, self.b
		# calculate if expression
		if isinstance(f, (FunctionType)):
			# check if f(a) and f(b) are opposite signs
			if f(a)*f(b) < 0:
				if self.iter_guess == True: # if left unassigned, guess
					N = self.max_iterations("bisection")
				elif isinstance(self.iter_guess, (int, float)): # if defined, use
					N = int(self.iter_guess)
				# else, break for bad assignment
				else: raise ValueError(SingleVariableIteration.__MaxIterError(self.iter_guess))
				k, approximations, errors = 1, [f(a)], [1] # initialize
				# exit by whichever condition is TRUE first
				while errors[-1] >= self.tol and k <= N:
					x = (b - a)/2
					p = a + x 				# new value, p
					approximations.append(p)
					if f(a)*f(p) > 0: a = p	# adjust next bounds
					else: b = p
					errors.append(abs(x))	# error of new value, p
					k += 1 	# iterate to k + 1
				#if k <= N: print("Congratulations! Solution found!")
				#else: print("Warning! Solution could not be found with initial guess or tolerance.")
				self.iterations = np.array(range(k))
				self.approximations = np.array(approximations)
				self.errors = np.array(errors)
				return pd.DataFrame(data={
					"Iterations": self.iterations,
					"Approximations": self.approximations,
					"Errors": self.errors
				})
			# abort if f(a) is not opposite f(b)
			else: raise ValueError(SingleVariableIteration.__OppositeSignError_Interval(self.__function_name, f, a, b))
		# abort if not expression
		else: raise TypeError(SingleVariableIteration.__TypeError_Lambda(self.__function_name))

	def false_position(
		self,
		p0: float,
		p1: float
	) -> pd.DataFrame:
		"""Attempt method with initial guesses, p0 and p1 in [a, b].

		Root-finding problem: f(x) = 0. 

		!!! Use function with lowest slope !!!

		Parameters
		----------
		p0 : float
			First initial guess.

		p1 : float
			Second initial guess.

		Returns
		-------
		pandas.DataFrame : DataFrame
			Summarized dataframe from iterations.

		Yields
		------
		self.iterations : np.ndarray
			Collection of iterations through method.

		self.approximations : np.ndarray
			Collection of evaluated points, p.

		self.errors : np.ndarray
			Collection of propogated error through method.

		Raises
		------
		ValueError
			If input for desired iterations was assigned not an integer.

		ValueError
			If initial guesses did not evaluate to have opposite signs.

		TypeError
			If input expression cannot be understood as lambda or sympy expression nor as string.

		Warnings
		--------
		Print to console if solution was found, or state that solution did not converge with given guess or prescribed tolerance.

		Notes
		-----
		Check that |g'(x)| <= (leading coefficient of g'(x)) for all x in [a, b].

		Theorem:
		1) Existence of a fixed-point:
			If g in C[a,b] and g(x) in C[a, b] for all x in [a, b], then function, g has a fixed point in [a, b].

		2) Uniqueness of a fixed point:
			If g'(x) exists on [a, b] and a positive constant, k < 1 exist with {|g'(x)| <= k  |  x in (a, b)}, then there is exactly one fixed-point, p in [a, b].

		Converges by O(linear) if g'(p) != 0, and O(quadratic) if g'(p) = 0 and g''(p) < M, where M = g''(xi) that is the error function.

		Examples 
		--------
		If  g(x) = x**2 - 2

		Then	p = g(p) = p**2 - 2

		=>  p**2 - p - 2 = 0
		"""
		f, a, b = self.function, self.a, self.b
		self.p0, self.p1 = p0, p1 = float(p0), float(p1)
		# calculate if expression
		if isinstance(f, (FunctionType)):
			# check if f(p0) and f(p1) are opposites signs
			if f(p0)*f(p1) < 0:
				if self.iter_guess == True: # if left unassigned, guess
					if self.function_slope == 0: self.find_k()
					N = self.max_iterations("false_position", p0=p0)
				elif isinstance(self.iter_guess, (int, float)): # if defined, use
					N = int(self.iter_guess)
				# else, break for bad assignment
				else: raise ValueError(SingleVariableIteration.__MaxIterError(self.iter_guess))
				k, approximations, errors = 1, [f(a)], [1] # initialize
				# exit by whichever condition is TRUE first
				while errors[-1] >= self.tol and k <= N:
					q0, q1 = f(p0), f(p1)
					p = p1 - q1*(p1 - p0)/(q1 - q0) # new value, p
					approximations.append(p)
					errors.append(abs(p - p0))		# error of new value, p
					if f(p)*q1 < 0: p0 = p1			# adjust next bounds
					p1 = p; k += 1 					# iterate to k + 1
				#if k <= N: print("Congratulations! Solution found!")
				#else: print("Warning! Solution could not be found with initial guess or tolerance.")
				self.iterations = np.array(range(k))
				self.approximations = np.array(approximations)
				self.errors = np.array(errors)
				return pd.DataFrame(data={
					"Iterations": self.iterations,
					"Approximations": self.approximations,
					"Errors": self.errors
				})
			# abort if f(p0) is not opposite f(p1)
			else: raise ValueError(SingleVariableIteration.__OppositeSignError_Guess(self.__function_name, f, p0, p1))
		# abort if not expression
		else: raise TypeError(SingleVariableIteration.__TypeError_Lambda(self.__function_name))

	def fixed_point(
		self,
		p0: float
	) -> pd.DataFrame:
		"""Attempt method with initial guess, p0 in [a, b].

		Root-finding problem: f(x) = 0. 

		!!! Use function with lowest slope !!!

		Parameters
		----------
		p0 : float
			Initial guess.

		Returns
		-------
		pandas.DataFrame : DataFrame
			Summarized dataframe from iterations.

		Yields
		------
		self.iterations : np.ndarray
			Collection of iterations through method.

		self.approximations : np.ndarray
			Collection of evaluated points, p.

		self.errors : np.ndarray
			Collection of propogated error through method.

		Raises
		------
		ValueError
			If input for desired iterations was assigned not an integer.

		ValueError
			If initial guesses did not evaluate to have opposite signs.

		TypeError
			If input expression cannot be understood as lambda or sympy expression nor as string.

		Warnings
		--------
		Print to console if solution was found, or state that solution did not converge with given guess or prescribed tolerance.

		Notes
		-----
		Check that |g'(x)| <= (leading coefficient of g'(x)) for all x in [a, b].

		Theorem:
		1) Existence of a fixed-point:
			If g in C[a, b] and g(x) in C[a, b] for all x in [a, b], then function, g has a fixed point in [a, b].

		2) Uniqueness of a fixed point:
			If g'(x) exists on [a, b] and a positive constant, k < 1 exist with {|g'(x)| <= k  |  x in (a, b)}, then there is exactly one fixed-point, `p` in [a, b].

		Converges by O(linear) if g'(p) != 0, and O(quadratic) if g'(p) = 0 and g''(p) < M, where M = g''(xi) that is the error function.

		Examples 
		--------
		If  g(x) = x**2 - 2

		Then	p = g(p) = p**2 - 2
		
		=>  p**2 - p - 2 = 0
		"""
		f, a, b = self.function, self.a, self.b
		self.p0 = p0 = float(p0)
		# calculate if expression
		if isinstance(f, (FunctionType)):
			if self.iter_guess == True: # if left unassigned, guess
				if self.function_slope == 0: self.find_k()
				N = self.max_iterations("fixed_point", p0=p0)
			elif isinstance(self.iter_guess, (int, float)): # if defined, use
				N = int(self.iter_guess)
			# else, break for bad assignment
			else: raise ValueError(SingleVariableIteration.__MaxIterError(self.iter_guess))
			k, approximations, errors = 1, [f((a+b)/2)], [1] # initialize
			# exit by whichever condition is TRUE first
			while errors[-1] >= self.tol and k <= N:
				p = f(p0)						# new value, p
				approximations.append(p)
				errors.append(abs((p - p0)/p0))	# error of new value, p
				p0 = p; k += 1 					# iterate to k + 1
			#if k <= N: print("Congratulations! Solution found!")
			#else: print("Warning! Solution could not be found with initial guess or tolerance.")
			self.iterations = np.array(range(k))
			self.approximations = np.array(approximations)
			self.errors = np.array(errors)
			return pd.DataFrame(data={
				"Iterations": self.iterations,
				"Approximations": self.approximations,
				"Errors": self.errors
			})
		# abort if not expression
		else: raise TypeError(SingleVariableIteration.__TypeError_Lambda(self.__function_name))

	def newton_raphson(
		self,
		p0: float
	)  -> pd.DataFrame:
		"""Attempt method with initial guess, p0 in [a, b].

		Root-finding problem: f(x) = 0. 

		!!! Use function with lowest slope !!!

		Parameters
		----------
		p0 : float
			Initial guess.

		Returns
		-------
		pandas.DataFrame : DataFrame
			Summarized dataframe from iterations.

		Yields
		------
		self.iterations : np.ndarray
			Collection of iterations through method.

		self.approximations : np.ndarray
			Collection of evaluated points, p.

		self.errors : np.ndarray
			Collection of propogated error through method.

		Raises
		------
		ValueError
			If input for desired iterations was assigned not an integer.

		ValueError
			If initial guesses did not evaluate to have opposite signs.

		TypeError
			If input expression cannot be understood as lambda or sympy expression nor as string.

		Warnings
		--------
		Print to console if solution was found, or state that solution did not converge with given guess or prescribed tolerance.

		Notes
		-----
		f'(x) != 0.

		Not root-bracketed.

		Initial guess must be close to real solution; else, will converge to different root or oscillate (if symmetric).

		Check that |g'(x)| <= (leading coefficient of g'(x)) for all x in [a, b].

		Technique based on first Taylor polynomial expansion of f about p0 and evaluated at x = p. |p - p0| is assumed small; therefore, 2nd order Taylor term, the error, is small.

		Newton-Raphson has quickest convergence rate.

		This method can be viewed as fixed-point iteration.

		Theorem:
		1) Existence of a fixed-point:
			If g in C[a, b] and g(x) in C[a, b] for all x in [a, b], then function, g has a fixed point in [a, b].

		2) Uniqueness of a fixed point:
			If g'(x) exists on [a, b] and a positive constant, `k` < 1 exist with {|g'(x)| <= k  |  x in (a, b)}, then there is exactly one fixed-point, `p` in [a, b].

		Converges by O(linear) if g'(p) != 0, and O(quadratic) if g'(p) = 0 and g''(p) < M, where M = g''(xi) that is the error function.

		Examples 
		--------
		If  g(x) = x**2 - 2

		Then	p = g(p) = p**2 - 2

		=>  p**2 - p - 2 = 0
		"""
		f, a, b = self.function, self.a, self.b
		self.p0 = p0 = float(p0)
		# calculate if expression
		if isinstance(f, (FunctionType)):
			# determine form of derivative
			# if self.function_str != "Lambda":
			# 	df_str = ex.fast_derive_latex(self.function_str, self.variable)
			# 	df = lambda x: ex.fast_eval_latex(df_str, {self.variable: x})
			# else: df = sp.lambdify(sp.Symbol(self.variable), sp.diff(self.function(sp.Symbol(self.variable))))
			df = sp.lambdify(sp.Symbol(self.variable), sp.diff(self.function(sp.Symbol(self.variable))))
			if self.iter_guess == True: # if left unassigned, guess
				if self.function_slope == 0: self.find_k()
				N = self.max_iterations("newton_raphson", p0=p0)
			elif isinstance(self.iter_guess, (int, float)): # if defined, use
				N = int(self.iter_guess)
			# else, break for bad assignment
			else: raise ValueError(SingleVariableIteration.__MaxIterError(self.iter_guess))
			k, approximations, errors = 1, [f(a)], [1] # initialize
			# exit by whichever condition is TRUE first
			while errors[-1] >= self.tol and k <= N:
				fp0 = f(p0)
				dfp0 = df(p0)
				p = p0 - (fp0/dfp0)			# new value, p
				approximations.append(p)
				errors.append(abs(p - p0)) 	# error of new value, p
				p0 = p; k += 1				# iterate to k + 1
			#if k <= N: print("Congratulations! Solution found!")
			#else: print("Warning! Solution could not be found with initial guess or tolerance.")
			self.iterations = np.array(range(k))
			self.approximations = np.array(approximations)
			self.errors = np.array(errors)
			return pd.DataFrame(data={
				"Iterations": self.iterations,
				"Approximations": self.approximations,
				"Errors": self.errors
			})
		# abort if not expression
		else: raise TypeError(SingleVariableIteration.__TypeError_Lambda(self.__function_name))

	def secant_method(
		self,
		p0: float,
		p1: float
	) -> pd.DataFrame:
		"""Attempt method with initial guesses, p0 and p1 in [a, b].
		
		Root-finding problem: f(x) = 0. 

		!!! Use function with lowest slope !!!

		Parameters
		----------
		p0 : float
			First initial guess.

		p1 : float
			Second initial guess.

		Returns
		-------
		pandas.DataFrame : DataFrame
			Summarized dataframe from iterations.

		Yields
		------
		self.iterations : np.ndarray
			Collection of iterations through method.

		self.approximations : np.ndarray
			Collection of evaluated points, p.

		self.errors : np.ndarray
			Collection of propogated error through method.

		Raises
		------
		ValueError
			If input for desired iterations was assigned not an integer.

		ValueError
			If initial guesses did not evaluate to have opposite signs.

		TypeError
			If input expression cannot be understood as lambda or sympy expression nor as string.

		Warnings
		--------
		Print to console if solution was found, or state that solution did not converge with given guess or prescribed tolerance.

		Notes
		-----
		Not root-bracketed.

		Bypasses need to calculate derivative (as in Newton-Raphson).

		Check that |g'(x)| <= (leading coefficient of g'(x)) for all x in [a, b].

		Theorem:
		1) Existence of a fixed-point:
			If g in C[a, b] and g(x) in C[a, b] for all x in [a, b], then function, g has a fixed point in [a, b].

		2) Uniqueness of a fixed point:
			If g'(x) exists on [a, b] and a positive constant, `k` < 1 exist with {|g'(x)| <= k  |  x in (a, b)}, then there is exactly one fixed-point, `p` in [a, b].

		Converges by O(linear) if g'(p) != 0, and O(quadratic) if g'(p) = 0 and g''(p) < M, where M = g''(xi) that is the error function.

		Examples 
		--------
		If  g(x) = x**2 - 2

		Then	p = g(p) = p**2 - 2

		=>  p**2 - p - 2 = 0
		"""
		f, a, b = self.function, self.a, self.b
		self.p0, self.p1 = p0, p1 = float(p0), float(p1)
		# calculate if expression
		if isinstance(f, (FunctionType)):
			# check if f(p0) and f(p1) are opposite signs
			if f(p0)*f(p1) < 0:
				if self.iter_guess == True: # if left unassigned, guess
					if self.function_slope == 0: self.find_k()
					N = self.max_iterations("secant_method", p0=p0)
				elif isinstance(self.iter_guess, (int, float)): # if defined, use
					N = int(self.iter_guess)
				# else, break for bad assignment
				else: raise ValueError(SingleVariableIteration.__MaxIterError(self.iter_guess))
				k, approximations, errors = 1, [f(a)], [1] # initialize
				# exit by whichever condition is TRUE first
				while errors[-1] >= self.tol and k <= N:
					q0, q1 = f(p0), f(p1)
					p = p1 - q1*(p1 - p0)/(q1 - q0)	# new value, p
					approximations.append(p)
					errors.append(abs(p - p0))		# error of new value
					p0, p1 = p1, p; k += 1 			# iterate to k + 1
				#if k <= N: print("Congratulations! Solution found!")
				#else: print("Warning! Solution could not be found with initial guess or tolerance.")
				self.iterations = np.array(range(k))
				self.approximations = np.array(approximations)
				self.errors = np.array(errors)
				return pd.DataFrame(data={
					"Iterations": self.iterations,
					"Approximations": self.approximations,
					"Errors": self.errors
				})
			# abort if f(p0) is not opposite f(p1)
			else: raise ValueError(SingleVariableIteration.__OppositeSignError_Guess(self.__function_name, f, p0, p1))
		# abort if not expression
		else: raise TypeError(SingleVariableIteration.__TypeError_Lambda(self.__function_name))

class MultiVariableIteration:
	"""Find the solution to a system of equations.
	"""
	def __init__(
		self,
		A: tuple,
		x: tuple,
		b: tuple,
		power: Optional[float]=-6,
		max_iter: Optional[int]=100,
		norm_type: Optional[str]="l_infinity"
	):
		"""
		Parameters
		----------
		A : tuple
			Either input functions or matrix of characteristic values.

		x : tuple
			Either collection of symbols or initial guesses for system of equations.

		b : tuple
			Input vector.

		power : float, optional
			Signed, specified power of tolerance until satisfying method.

		max_iter : int, optional
			Number of iterations.

		norm_type : string, optional
			String representation of desired norm function. `'l_infinity'` by default.

		Yields
		------
		self.A : np.ndarray
			Either input functions or matrix of characteristic values.

		self.x : np.ndarray
			Either collection of symbols or initial guesses for system of equations.

		self.b : np.ndarray
			Input vector.

		self.tol : float
			Specified tolerance to which method terminates.

		self.max_iter : int
			Maximum iterations allowed for method.

		self.norm_type : string
			String representation of desired norm function.

		self.is_diagonal : bool
			Truth value of whether matrix is diagonal.

		self.is_symmetric : bool
			Truth value of whether matrix is symmetric.

		self.is_tridiagonal : bool
			Truth value of whether matrix is tridiagonal.

		self.eigen_values : np.ndarray
			Eigenvalues of characteristic matrix, A.

		self.spectral_radius : float
			Spectral radius of characteristic matrix, A.

		self.condition_number : float
			Condition number of characteristic matrix, A. 

		Raises
		------
		TypeError
			Not all elements in matrix of interest (if one-dimensional) are lambda expressions.

		IndexError
			Matrix of interest must be square.

		IndexError
			If x0 is not a one-dimensional array.

		IndexError
			If b is not a one-dimensional array.

		ValueError
			If iterations constraint is not an integer.

		ValueError
			If desired norm method was neither `'l_infinity'` nor `'l_two'`.

		Warnings
		--------
		Not recommended to use eigen_values() to find eigenvalues of characteristic matrix, A; therefore, if desiring quick calculations, do not use if matrix, A is a large, sparse matrix.

		See Also
		--------
		diagonality() : Determines if matrix, A is strictly, diagonally dominant.

		symmetry() : Dtermines if matrix, A is symmetric.

		tridiagonality() : Determines if matrix, A is tridiagonal.

		EigenValues().conjugate_gradient() : Function to find eigenvalues of matrix, A given initial vector, x and solution vector, b..

		spectral_radius() : Function to find the spectral radius of characteristic matrix, A.

		condition_number() : Finds the condition number of matrix, A.

		Notes
		-----
		Specified tolerance evaluated by: `10**power`.

		norm_type may be either `'l_infinity'` or `'l_two'`. Is 'l_infinity' by default.
		"""
		A, x, b = np.array(A), np.array(x), np.array(b)
		self.__matrix_name = _retrieve_name(A)
		self.__vector_name = _retrieve_name(x)
		self.__solution_name = _retrieve_name(b)
		BadMatrixError = lambda matrix_name: f"ERROR! Matrix, '{matrix_name}' must be square matrix of floats or one-dimensional array of lambda expressions!"
		BadVectorError = lambda vector_name: f"ERROR! Systems vector, '{vector_name}' must be one-dimensional array!"
		BadSystemError = f"ERROR! Systems of equations are not all same length!"
		BadMaxIterError = lambda N: f"ERROR! Maximum iterations, N='{N}' must be an integer greater than zero."
		BadNormTypeError = lambda norm_type: f"ERROR! Desired norm type, '{norm_type}' was not understood. Please choose 'l_infinity' or 'l_two'."
		if np.ndim(A) == 1:
			for a in A:
				if not isinstance(a, FunctionType):
					raise TypeError(BadMatrixError(self.__matrix_name))
		else:
			if np.sum(np.array(A).shape[0]) != np.array(A).shape[1]: raise IndexError(BadMatrixError(self.__matrix_name))
			self.is_diagonal = diagonality(A)
			self.is_symmetric = symmetry(A)
			self.is_tridiagonal = tridiagonality(A)
			self.eigen_values = EigenValues(A, power=power).conjugate_gradient(x, b)
			self.spectral_radius = spectral_radius(A)
			self.condition_number = condition_number(A, norm_type)
		if np.sum(np.array(x).shape) - np.array(x).shape[0] > 1: raise IndexError(BadVectorError(self.__vector_name))
		if np.sum(np.array(b).shape) - np.array(b).shape[0] > 1: raise IndexError(BadVectorError(self.__solution_name))
		if len(A) != len(x) or len(A) != len(b) or len(x) != len(b): raise IndexError(BadSystemError)
		if max_iter <= 0 or not isinstance(max_iter, (int, float)): ValueError(BadMaxIterError(max_iter))
		if norm_type != "l_infinity" and norm_type != "l_two": raise ValueError(BadNormTypeError(norm_type))
		self.A = np.array(A)
		self.x = np.reshape(x, (len(x), 1))
		self.b = np.reshape(b, (len(b), 1))
		self.tol = float(10**power)
		self.max_iter = int(max_iter)
		self.norm_type = norm_type

	__NoSolutionWarning = lambda N, tol: f"Warning! Solution could not be found with initial guess, {N} or tolerance, {tol}."
	__SolutionInformation = "Congratulations! Solution found!"

	def __find_xk(
		self,
		x: np.ndarray
	) -> np.ndarray:
		return np.matmul(self.T, x) + self.c

	def find_omega(
		self,
		omega: Optional[float]=0
	) -> float:
		"""Given the characteristic matrix and solution vector, determine if prescribed omega is the optimum choice.

		Parameters
		----------
		omega : float, optional
			Relaxation parameter.

		Returns
		-------
		omega : float
			The omega used for Successive Relaxation method.

		Yields
		------
		self.user_omega : float
			Supplied/default omega.

		self.is_tridiagonal : bool
			Truth value of whether matrix, A is tridiagonal.

		self.best_omega : float
			If found, is the optimum choice of omega.

		Warnings
		--------
		If 0 < omega < 2, then method will converge regardless of choice for x0. Will inform user that matrix, A is not tridiagonal, but will proceed with calculation all the same. If matrix, A is poorly defined and not found to be positive definite, then user is informed but calculation proceeds. If an optimal omega cannot be found, then `self.best_omega` assigned from supplied/default omega.

		See Also
		--------
		tridiagonality() : Determines if matrix, A is tridiagonal or not.

		spectral_radius() : Uses the spectral radius of Gauss-Seidel's T-matrix to calculate omega.

		Notes
		-----
		Unless specified, omega will be 0 and chosen, if possible.
		"""
		self.user_omega = omega
		xn, xt = self.x, self.x.transpose()
		y = np.matmul(np.matmul(xt, self.A), xn)
		if y[0] > 0: state = True
		else: state = False
		if self.is_symmetric and state: theorem_6_22 = True
		else: theorem_6_22 = False
		i, theorem_6_25 = 1, True
		while i <= len(self.A) and theorem_6_25 == True:
			# Ai = self.A[:i,:i]
			# if ex.fast_determinant(Ai) > 0: theorem_6_25 = True
			Ai = sp.Matrix(self.A[:i,:i])
			if sp.det(Ai) > 0: theorem_6_25 = True
			else : theorem_6_25 = False
			i += 1
		if theorem_6_22 or theorem_6_25:
			#if 0 < omega and omega < 2:
			#	print("According to Ostrowski-Reich's Theorem, the successive relaxation technique will converge.")
			if self.is_tridiagonal:
				D = np.diagflat(np.diag(self.A))
				L = np.diagflat(np.diag(self.A, k=-1), k=-1)
				U = np.diagflat(np.diag(self.A, k=1), k=1)
				DL, DL_inv = D - L, np.zeros_like(D - L)
				for i in range(len(DL_inv)):
					for j in range(len(DL_inv[0])):
						if DL[i][j] != 0: DL_inv[i][j] = 1/(DL[i][j])
				Tg = DL_inv*U
				omega = 2 / (1 + math.sqrt(1 - spectral_radius(Tg)))
				#print(f"I believe {omega} would be the best choice.")
			#else:
			#	print(f"Warning! Matrix, {self.matrix_name} is not tridiagonal.")
			#	print(f"Assigning supplied omega, {omega} as `self.best_omega`.")
		#else:
		#	print(f"Warning! Matrix, {self.matrix_name} is not positive definite.")
		#	print(f"Assigning supplied omega, {omega} as `self.best_omega`.")
		self.best_omega = omega
		return omega

	def gauss_seidel(
		self
	) -> pd.DataFrame:
		"""Given A*x = b, use `self.norm_type` to find x via the Gauss-Seidel Method.

		Returns
		-------
		pandas.DataFrame : DataFrame
			Summarized dataframe from iterations.

		Yields
		-------
		self.iterations : np.ndarray
			Running collection of iterations through method.

		self.approximations : list
			Finally evaluated solution.

		self.errors : np.ndarray
			Aggregate of yielded norms.

		Warnings
		--------
		Prints to console whether or not a solution was found within the specified tolerance with the supplied, initial guess.

		See Also
		--------
		norms().l_infinity() : Will find the l_infinity norm between x0 and xi.

		norms().l_two() : Will find the l_two norm between x0 and xi.

		Notes
		-----
		gauss_seidel():
			[x]_(k) = ( (D - L)^(-1) * U ) * [x]_(k - 1) + ( (D - L)^(-1) )*[b]
		"""
		x = self.x
		# A = np.zeros((N, N))
		# np.fill_diagonal(A, ai)
		# A = A + np.diagflat(bi, 1)
		# A = A + np.diagflat(ci, -1)
		# x0 = np.zeros(N)
		# b = np.array(di)
		# A1, A2 = np.zeros((n, n)), np.zeros((n, n))
		# np.fill_diagonal(A1, np.diagonal(A))
		# A1 = A1 - np.tril(A, k=-1)
		# i = 0
		# while i < n:
		# 	j = 0
		# 	while j <= i:
		# 		a1ij = A1[i][j]
		# 		if a1ij != 0:
		# 			A2[i][j] = 1/a1ij
		# 		j += 1
		# 	i += 1
		# self.T = np.matmul(A2, np.triu(A, k=1))
		# self.c = np.matmul(A2, b)
		k, n, approximations, errors = 1, len(x), [x], [self.tol*10]
		while errors[-1] > self.tol and k <= self.max_iter:
			xi = np.zeros_like(x)
			for i in range(n):
				y1 = y2 = 0
				for j in range(i): y1 += float(self.A[i][j]*xi[j])
				for j in range(i+1, n): y2 += float(self.A[i][j]*x[j])
				xi[i] = float((-y1 - y2 + self.b[i])/self.A[i][i])
			# xi = self.__find_xk(x0)
			if self.norm_type == "l_infinity":
				norm = norms(xi, x).l_infinity()
			elif self.norm_type == "l_two":
				norm = norms(xi, x).l_two()
			approximations.append(xi)
			errors.append(norm)
			x = xi; k += 1 # iterate to k + 1
		#if k <= self.max_iter: print(MultiVariableIteration.__SolutionInformation())
		#else: print(MultiVariableIteration.__NoSolutionWarning(self.max_iter, self.tol)
		## m, n = len(approximations[0]), len(approximations)
		## j, x = 0, np.zeros((m,n))
		## while j < n:
		## 	i = 0
		## 	while i < m:
		## 		x[i][j] = float(approximations[j][i])
		## 		i += 1
		## 	j += 1
		self.iterations = np.arange(k)
		#self.approximations = np.array(approximations)
		self.approximations = approximations
		self.errors = np.array(errors)
		return pd.DataFrame(data={
			"Iterations": self.iterations,
			"Approximations": self.approximations,
			"Errors": self.errors
		})

	def jacobi(
		self
	) -> pd.DataFrame:
		"""Given A*x = b, use `self.norm_type` to find x via the Jacobi Method.

		Returns
		-------
		pandas.DataFrame : DataFrame
			Summarized dataframe from iterations.

		Yields
		-------
		self.iterations : np.ndarray
			Collection of iterations through method.

		self.approximations : list
			Collection of approximated, iterative solutions.

		self.errors : np.ndarray
			Collection of yielded norms.

		Warnings
		--------
		Prints to console whether or not a solution was found within the specified tolerance with the supplied, initial guess.

		See Also
		--------
		norms().l_infinity() : Will find the l_infinity norm between x0 and xi.

		norms().l_two() : Will find the l_2 norm between x0 and xi.

		Notes
		-----
		jacobi():
			[x]_(k) = ( D^(-1)*(L + U) ) * [x]_(k - 1) + ( D^(-1) ) * [b]
		"""
		x = self.x
		k, n, approximations, errors = 1, len(x), [x], [self.tol*10]
		while errors[-1] > self.tol and k <= self.max_iter:
			xi = np.zeros_like(x)
			for i in range(n):
				y = 0
				for j in range(n):
					if j != i: y += float(self.A[i][j]*x[j])
				xi[i] = float((-y + self.b[i])/self.A[i][i])
			if self.norm_type == "l_infinity":
				norm = norms(xi, x).l_infinity()
			elif self.norm_type == "l_two":
				norm = norms(xi, x).l_two()
			approximations.append(xi)
			errors.append(norm)
			x = xi; k += 1 # iterate to k + 1
		#if k <= self.max_iter: print(MultiVariableIteration.__SolutionInformation())
		#else: print(MultiVariableIteration.__NoSolutionWarning(self.max_iter, self.tol)
		## m, n = len(approximations[0]), len(approximations)
		## X_matrix, j = np.zeros((m,n)), 0
		## while j < n:
		## 	i = 0
		## 	while i < m:
		## 		X_matrix[i][j] = float(approximations[j][i])
		## 		i += 1
		## 	j += 1
		self.iterations = np.arange(k)
		self.approximations = approximations
		#print(np.shape(self.approximations))
		self.errors = np.array(errors)
		return pd.DataFrame(data={
			"Iterations": self.iterations,
			"Approximations": self.approximations,
			"Errors": self.errors
		})

	def newton_raphson(
		self,
		variables: Tuple[str]
	) -> pd.DataFrame:
		"""Employ the Newton-Raphson Method to find solution of non-linear systems of equations within tolerance.

		Root-finding problem: f(x) = 0.

		Parameters
		----------
		variables : tuple
			Collection of string representations of symbols to respect in derivations.

		Yields
		-------
		self.iterations : np.ndarray
			Collection of iterations through method.

		self.approximations : tuple
			Collection of approximated, iterative solutions.

		self.errors : np.ndarray
			Collection of yielded norms.

		Raises
		------
		TypeError
			If an element of `variables` is not of type string.

		Notes
		-----
		Modified form of `MultiVariableIteration()` to analyze a one-dimensional array of non-linear system of equations. Each element should be a lambda expression wherein each variable is represented.

		Examples 
		--------
		If `A = [lambda x1, x2, x3: 3*x1 - sympy.cos(x2*x3) - 1/2, lambda x1, x2, x3: x1**2 - 81*(x2 + 0.1)**2 + sympy.sin(x3) + 1.06, lambda x1, x2, x3: sympy.exp(-x1*x2) + 20*x3 + (10*math.pi - 3)/3]`, `x` = (0.1, 0.1, -0.1), `b` = (0, 0, 0)
		, and `variables` = ("x1", "x2", "x3"), then this method should yield a final approximation of (0.5, 0., -0.52359877).
		"""
		def jacobian_form(g):
			n = len(g)
			jacMatrix = np.zeros((n, n), dtype=FunctionType)
			for i in range(n):
				for j in range(n):
					jacMatrix[i][j] = sp.lambdify(variables, sp.diff(g[i], variables[j]))
			return jacMatrix
		functions, f, x, b = [], [], self.x, self.b
		for var in variables:
			if isinstance(var, str): continue
			else: raise TypeError(f"'{var}' must be of type string.")
		variables = [sp.symbols(var) for var in variables]
		k = 0
		for a in self.A:
			f.append(sp.lambdify(variables, a(*variables) - float(b[k])))
			functions.append(a(*variables) - float(b[k]))
			k += 1
		jacobian = jacobian_form(functions)
		k, n, approximations, errors = 1, len(x), [x], [self.tol*10]
		while errors[-1] >= self.tol and k <= self.max_iter:
			J = np.zeros_like(jacobian, dtype=float)
			for i in range(len(jacobian[0])):
				for j in range(len(jacobian)):
					J[i][j] = jacobian[i][j](*x)
			g = np.zeros_like(x)
			for i in range(n): 
				g[i] = f[i](*(x.reshape((1, n))[0]))
			# y0 = np.linalg.solve(J, -g)
			y0 = EigenValues(J).conjugate_gradient(x, -g)["Lambdas"].values[-1]
			# y0 = MultiVariableIteration(J, xk, -g).gauss_seidel()["Approximations"].values[-1]
			xk = x + y0
			if self.norm_type == "l_two":
				norm = norms(xk, x).l_two()
			elif self.norm_type == "l_infinity":
				norm = norms(xk, x).l_infinity()
			errors.append(norm)
			approximations.append(xk.reshape((1, n))[0])
			x = xk; k += 1
		self.iterations = np.arange(k)
		self.approximations = approximations
		self.errors = np.array(errors)
		return pd.DataFrame(data={
			"Iterations": self.iterations,
			"Approximations": self.approximations,
			"Errors": self.errors
		})

	def successive_relaxation(
		self,
		omega: Optional[Union[None,float]]=None
	) -> pd.DataFrame:
		"""Given A*x = b, use `self.norm_type` to find vector, x via the Successive Relaxtion Method. Is Successive Over-Relaxation if omega > 1, Successive Under-Relaxation if omega < 1, and is Gauss-Seidel if omega = 1.

		Parameters
		----------
		omega : None or float, optional
			Relaxation parameter.

		Returns
		-------
		pandas.DataFrame : DataFrame
			Summarized dataframe from iterations.

		Yields
		-------
		self.iterations : np.ndarray
			Collection of iterations through method.

		self.approximations : list
			Collection of approximated, iterative solutions.

		self.errors : np.ndarray
			Collection of yielded norms.

		Warnings
		--------
		Prints to console optimal choice of omega, regardless of assignment, and whether or not a solution was found within the specified tolerance with the supplied, initial guess.

		See Also
		--------
		norms().l_infinity() : Will find the l_infinity norm between x0 and xi.

		norms().l_two() : Will find the l_2 norm between x0 and xi.

		find_omega() : Will analyze system of equation to find an optimal omega, if possible, and inform user.

		gauss_seidel() : Technique is Gauss-Seidel's modified by omega.

		Notes
		-----
		gauss_seidel():
			[x]_(k) = ( (D - L)^(-1) * U ) * [x]_(k - 1) + ( (D - L)^(-1) )*[b]

		successive_relaxation():
			[x]_(k) = ( (D - wL)^(-1) * ((1 - w)*D + w*U) ) * [x]_(k - 1) + w*( (D - w*L)^(-1) )*[b]

		omega will be analyzed independent of assigned value which will be used if not specified in assignment.
		"""
		BadOmegaError = lambda omega: f"ERROR! Either a positive omega greater than zero was not given (w = {omega}), or I could not choose one."
		if omega == None:
			try: w = self.user_omega
			except AttributeError:
				try: w = self.best_omega
				except AttributeError:
					# w = super().find_omega(A, x0)
					w = self.find_omega()
			#		print(f"Warning! Omega was not given; therefore, I attempted to choose one, {w}.")
			#	else: print(f"Warning! Using `self.best_omega` = {w}.")
			#else: print(f"Warning! Using `self.user_omega` = {w}.")
			if w <= 0: raise ValueError(BadOmegaError(w))
		elif omega != None and isinstance(omega, (int, float)) and omega > 0:
			# omega = find_omega(A, x0, w)
			w = self.find_omega(omega=omega)
			#print(f"Warning! omega = {omega} given. Which is not optimum: {w}")
			#w = omega
		else: raise ValueError(BadOmegaError(omega))
		x = self.x
		k, n, approximations, errors = 1, len(x), [x], [self.tol*10]
		while errors[-1] > self.tol and k <= self.max_iter:
			xi = np.zeros_like(x)
			# xgs = super().gauss_seidel(x0)
			xgs = self.gauss_seidel()["Approximations"].values[-1]
			for i in range(n):
				xi[i] = float((1 - w)*x[i] + w*xgs[i])
			if self.norm_type == "l_infinity":
				norm = norms(xi, x).l_infinity()
			elif self.norm_type == "l_two":
				norm = norms(xi, x).l_two()
			approximations.append(xi)
			errors.append(norm)
			x = xi; k += 1 # iterate to k + 1
		#if k <= self.max_iter: print(MultiVariableIteration.__SolutionInformation())
		#else: print(MultiVariableIteration.__NoSolutionWarning(self.max_iter, self.tol)
		## m, n = len(approximations[0]), len(approximations)
		## X_matrix, j = np.zeros((m,n)), 0
		## while j < n:
		## 	i = 0
		## 	while i < m:
		## 		X_matrix[i][j] = float(approximations[j][i])
		## 		i += 1
		## 	j += 1
		self.iterations = np.arange(k)
		#self.approximations = np.array(approximations)
		self.approximations = approximations
		self.errors = np.array(errors)
		return pd.DataFrame(data={
			"Iterations": self.iterations,
			"Approximations": self.approximations,
			"Errors": self.errors
		})
# --------------------

# --------------------
# interpolations
class cubic_spline:
	"""Construct interpolating spline polynomials between points of data set.
	"""
	def __init__(
		self,
		domain: tuple,
		function: tuple,
		variable: Optional[str]="x"
	):
		"""Given a domain and range, construct a spline polynomial within interval by some condition.

		Parameters
		----------
		domain : tuple
			Input domain.

		function : tuple
			Desired/Found range of interest.

		variable : string
			Respected variable in derivative of equation. Assumed to be `'x'` if not stated.

		Raises
		------
		BadDomainError : string
			If `domain` is not a one-dimensional array.

		BadFunctionError : string
			If `function` is not an expression or function and is not an one-dimensional array.

		BadDataError : string
			If `domain` and `function` are of unequal length.

		See Also
		--------
		make_array() : Translates input expression to array from given `domain`.

		endpoint() : Relies on another technique to find derivatives at endpoints if not explicitly provided by data, `fp` nor an expression.

		midpoint() : Finds the derivatives at points within the bounds of the endpoints.

		Notes
		-----
		Method uses many, low-ordered polynomials to fit larger data sets. This minimizes computational load, which conversely greatly increases for larger data sets that yield high-ordered polynomials.

		General form: 
			Sj(x) = aj + bj(x - xj) + cj(x - xj)^2 + dj(x - xj)^3

		Clamped splines fit the constructed polynomial to the given data and its der
		ivatives at either endpoint.

		If selected `condition` is `'natural'`, then `fp = 0`, because derivative is assumed to be straight line outside of data set.

		Definitions of cubic spline conditions:
			a) S(x) is a cubic polynomial, Sj(x) on sub-interval [x_(j), x_(j + 1)] for each j = 0, 1, ..., n - 1;

			b) Sj(x_(j)) = f(x_(j)) and Sj(x_(j + 1)) = f(x_(j + 1)) for each j = 0, 1, ..., n - 1;

			c) S_(j + 1)(x_(j + 1)) = Sj(x_(j + 1)) for each j = 0, 1, ..., n - 2;

			d) S_(j + 1)'(x_(j + 1)) = Sj'(x_(j + 1)) for each j = 0, 1, ..., n - 2;

			e) One of the following conditions is satisfied:
				1) S''(x0) = S''(xn) = 0				->  `'natural'`
			
				2) S'(x0) = f'(x0) and S'(xn) = f'(xn)  ->  `'clamped'`
		"""
		self.__domain_name, self.__function_name = _retrieve_name(domain), _retrieve_name(function)
		self.domain = X = np.array(domain)
		if np.sum(X.shape) > X.shape[0]: raise ValueError(cubic_spline.__BadDomainError(self.__domain_name))
		# if isinstance(function, (str)):
		# 	self.function_str = function_str = ex.fast_parse_latex(function)
		# 	self.function = function = lambda x: ex.fast_eval_latex(function_str, {variable: x})
		# 	self.mapped = make_array(X, function)
		# 	#print("String expression converted to lambda function.")
		# #elif isinstance(function, (FunctionType)):
		# #	self.function_str = function_str = _retrieve_expression(function)
		# #	self.function = function = lambda x: ex.fast_eval_latex(function_str, {variable: x})
		# #	self.g = make_array(X, function)
		if isinstance(function, (list, tuple, np.ndarray)):
			self.mapped = self.function = function = np.array(function)
		else: raise TypeError(cubic_spline.__BadFunctionError(self.__function_name))
		if np.sum(self.domain.shape) != np.sum(self.mapped.shape) or self.domain.shape[0] != self.mapped.shape[0]:
			raise IndexError(cubic_spline.__BadDataError(self.__domain_name, self.__function_name))
		self.variable = variable
	
	__BadDomainError = lambda domain_name: f"ERROR! Input domain, '{domain_name}' was neither an n x 1 nor a 1 x n array."
	__BadFunctionError = lambda function_name: f"ERROR! Input range, '{function_name}' was neither function of type string nor an one-dimensional array."
	__BadDataError = lambda domain_name, function_name: f"ERROR! Arrays '{domain_name}' and '{function_name}' must be of equal length."

	def clamped(
		self,
		function_derivative: Optional[tuple]=None
	) -> Tuple[np.ndarray, Tuple[FunctionType]]:
		"""The bookend polynomials will have the same slope entering and exiting the interval as the respective derivative.

		Parameters
		----------
		function_derivative : tuple, optional
			Derivative at each point in `function`.

		Returns
		-------
		Y : np.ndarray
			Finally evaluated solutions.

		splines : list
			Aggregate of lambda expressions for each spline on each interval.

		Raises
		------
		BadDerivativeError : string
			If `fp` is not an expression or function and is not an one-dimensional array.

		BadDataError : string
			If domain, function, and `fp` are not the same length.

		MissingDerivativeError : string
			Output message that derivative data or expression is missing.

		See Also
		--------
		midpoint() : Calculates derivative of points within data set.
		
		endpoint() : Calculates derivatives at either end of data set.

		Notes
		-----
		`fp` will be calculated if not specified.
		"""
		def algorithm(g, gp):
			Y, YP = np.array(g), np.array(gp)
			# STEP 1:   build list, h_i
			H = np.zeros(n)
			for i in range(n):
				H[i] = X[i+1] - X[i]
			# STEP 2:   define alpha list endpoints
			A, AP, ALPHA = Y, YP, np.zeros(m)
			ALPHA[0] = 3*(A[1] - A[0])/H[0] - 3*AP[0]
			ALPHA[n] = 3*AP[n] - 3*(A[n] - A[n-1])/H[n-1]
			# STEP 3:   build list, alpha_i
			for i in range(1, n):
				ALPHA[i] = 3/H[i]*(A[i+1] - A[i]) - 3/H[i-1]*(A[i] - A[i-1])
			# Algorithm 6.7 to solve tridiagonal
			# STEP 4:   define l, mu, and z first points
			L, MU, Z, C = np.zeros(m), np.zeros(m), np.zeros(m), np.zeros(m)
			L[0], MU[0] = 2*H[0], 0.5
			Z[0] = ALPHA[0]/L[0]
			# STEP 5:   build lists l, mu, and z
			for i in range(1, n):
				L[i] = 2*(X[i+1] - X[i-1]) - H[i-1]*MU[i-1]
				MU[i] = H[i]/L[i]
				Z[i] = (ALPHA[i] - H[i-1]*Z[i-1])/L[i]
			# STEP 6:   define l, z, and c endpoints
			L[n] = H[n-1]*(2-MU[i-1])
			Z[n] = (ALPHA[n] - H[n-1]*Z[n-1])/L[n]
			C[n] = Z[n]
			# STEP 7:   build lists c, b, and d
			B, D = np.zeros(n), np.zeros(n)
			for i in range(1, n+1):
				j = n-i
				C[j] = Z[j] - MU[j]*C[j+1]
				B[j] = (A[j+1] - A[j])/H[j] - H[j]*(C[j+1] + 2*C[j])/3
				D[j] = (C[j+1] - C[j])/(3*H[j])
			return Y, A, B, C, D
		try: self.__function_derivative_name = _retrieve_name(function_derivative)
		except IndexError: self.__function_derivative_name = "fp"
		BadDerivativeError = lambda fp_name: f"ERROR! Derivative range, '{fp_name}' was neither function nor expression and not an one-dimensional array."
		BadDataError = lambda domain_name, function_name, fp_name: f"ERROR! Arrays '{domain_name}', '{function_name}', and '{fp_name}' must be of equal length."
		MissingDerivativeError = lambda fp_name: f"ERROR! Missing derivative data or expression assignment for '{fp_name}'."
		f, X, g, variable = self.function, self.domain, self.mapped, self.variable
		if not isinstance(function_derivative, type(None)):
			# if isinstance(function_derivative, (FunctionType)): gp = make_array(X, function_derivative)
			# else:
			function_derivative = np.array(function_derivative)
			if np.sum(function_derivative.shape) > function_derivative.shape[0]: raise ValueError(BadDerivativeError(self.__function_derivative_name))
			elif len(X) != len(function_derivative): raise ValueError(BadDataError(self.__domain_name, self.__function_name, self.__function_derivative_name))
			else: gp = function_derivative
		else:
			# if isinstance(f, (str, FunctionType)):
			# 	##f = sp.lambdify(variable, sym_function)
			# 	##fp = sp.diff(sym_function)
			# 	#fp = sp.lambdify(self.variable, sp.diff(self.function_str, self.variable))
			# 	#gp = make_array(X, fp)
			# 	gp = make_array(X, ex.fast_derive_latex(self.function_str, variable))
			# #if isinstance(f, (FunctionType)):
			# #	f = _retrieve_expression(f)
			# #	f = make_array(X, f)
			# #elif isinstance(f, (str)):
			# #	gp = make_array(X, ex.fast_derive_latex(self.function_str, variable))
			# elif isinstance(g, np.ndarray):
			if isinstance(f, (list, tuple, np.ndarray)):
				if len(X) >= 3: point_type="three"
				elif len(X) >= 5: point_type="five"
				obj = Derivative(X, f, X[1]-X[0], point_type=point_type, variable=variable)
				gp = [obj.endpoint(0)]
				for i in range(1, len(X) - 1): gp.append(obj.midpoint(i))
				gp.append(obj.endpoint(-1))
				gp = np.array(gp)
			else: raise ValueError(MissingDerivativeError(self.__function_derivative_name))
		m, n = len(X), len(X) - 1
		Y, A, B, C, D = algorithm(g, gp)
		splines, splines_str = [], []
		# ltx_expression = r"aj + bj*(x - xj) + cj*(x - xj)^{2} + dj*(x - xj)^{3}"
		for j in range(n):
			xj, aj, bj, cj, dj = X[j], A[j], B[j], C[j], D[j]
			# ltx_dict = {
			# 	"aj": aj,
			# 	"bj": bj,
			# 	"cj": cj,
			# 	"dj": dj,
			# 	"xj": xj
			# }
			# parsed_string = ex.fast_parse_latex(ltx_expression, ltx_dict)
			# splines_str.append(parsed_string)
			# sj = lambda x: ex.fast_eval_latex(parsed_string, {variable: x})
			sj = sp.lambdify(sp.Symbol(variable), aj + bj*(sp.Symbol(variable) - xj) + cj*(sp.Symbol(variable) - xj)**2 + dj*(sp.Symbol(variable) - xj)**3)
			splines.append(sj)
		return Y, splines

	def natural(
		self
	) -> Tuple[np.ndarray, Tuple[FunctionType]]:
		"""The endpoint derivatives entering and exiting the interval are assumed to be 1.

		Returns
		-------
		Y : np.ndarray
			Finally evaluated solutions.

		splines : list
			Aggregate of lambda expressions for each spline on each interval.
		"""
		def algorithm(g):
			Y = g
			# STEP 1:   build list, h_i
			H = np.zeros(n)
			for i in range(n):
				H[i] = X[i+1] - X[i]
			# STEP 2:   build list, alpha_i
			A, ALPHA = Y, np.zeros(m)
			for i in range(1, n):
				ALPHA[i] = 3/H[i]*(A[i+1] - A[i]) - 3/H[i-1]*(A[i] - A[i-1])
			# Algorithm 6.7 to solve tridiagonal
			# STEP 3:   define l, mu, and z first points
			L, MU, Z, C = np.zeros(m), np.zeros(m), np.zeros(m), np.zeros(m)
			L[0], MU[0], Z[0] = 1, 0, 0
			# STEP 4:   build lists l, mu, and z
			for i in range(1, n):
				L[i] = 2*(X[i+1] - X[i-1]) - H[i-1]*MU[i-1]
				MU[i] = H[i]/L[i]
				Z[i] = (ALPHA[i] - H[i-1]*Z[i-1])/L[i]
			# STEP 5:   define l, z, and c endpoints
			L[n], Z[n], C[n] = 1, 0, 0
			# STEP 6:   build lists c, b, and d
			B, D = np.zeros(n), np.zeros(n)
			for i in range(1, n+1):
				j = n-i
				C[j] = Z[j] - MU[j]*C[j+1]
				B[j] = (A[j+1] - A[j])/H[j] - H[j]*(C[j+1] + 2*C[j])/3
				D[j] = (C[j+1] - C[j])/(3*H[j])
			return Y, A, B, C, D
		X, g, variable = self.domain, self.mapped, self.variable
		m, n = len(X), len(X) - 1
		Y, A, B, C, D = algorithm(g)
		splines, splines_str = [], []
		# ltx_expression = r"aj + bj*(x - xj) + cj*(x - xj)**2 + dj*(x - xj)**3"
		for j in range(n):
			xj, aj, bj, cj, dj = X[j], A[j], B[j], C[j], D[j]
			# ltx_dict = {
			# 	"aj": aj,
			# 	"bj": bj,
			# 	"cj": cj,
			# 	"dj": dj,
			# 	"xj": xj
			# }
			# parsed_string = ex.fast_parse_latex(ltx_expression, ltx_dict)
			# splines_str.append(parsed_string)
			# #sj = lambda x: ex.fast_eval_latex(parsed_string, {variable: x})
			sj = sp.lambdify(sp.Symbol(variable), aj + bj*(sp.Symbol(variable) - xj) + cj*(sp.Symbol(variable) - xj)**2 + dj*(sp.Symbol(variable) - xj)**3)
			splines.append(sj)
		return Y, splines

def hermite(
	domain: tuple,
	function: tuple,
	variable: Optional[str]="x",
	function_derivative: Optional[tuple]=None
) -> FunctionType:
	"""Given a domain and range, construct a Hermetic polynomial.

	Parameters
	----------
	domain : tuple
		Input domain.

	function : tuple
		Desired/Found range of interest.

	variable : string
		Respected variable in derivative of equation. Assumed to be `'x'` if not stated.

	function_derivative : tuple, optional
		Derivative at each point in `function`.

	Returns
	-------
	polynomial : lambda
		Lambdified Hermetic polynomial.

	Raises
	------
	BadDomainError : string
		If `domain` is not a one-dimensional array.

	BadFunctionError : string
		If `function` is not a one-dimensional array.

	BadDataError : string
		If `domain` and `function` are of unequal length.

	BadFunctionDerivativeError : string
		If `function_derivative` is not an expression or function and is not an one-dimensional array.

	BadFunctionDerivativeDataError : string
		If `domain`, `function`, or `function_derivative` are of unequal lengths.

	MissingDerivativeError : string
		If `function_derivative` is not given and `function` is not an expression, then missing derivative data or expression.

	Warns
	-----
	MadePolyInformation : string
		Displays the string form of the equation.

	See Also
	--------
	make_array() : Prints string that expression was used to make array.

	Notes
	-----
	`function_derivative` calculated if not specified.

	Slow computation time for larger data sets.

	Oscullating curve incorporates Taylor and Lagrangian polynomials to kiss the data and match each data point's derivatives. Which fits the curve to the shape of the data and its trend.
	"""
	domain_name, function_name, function_derivative_name = _retrieve_name(domain), _retrieve_name(function), _retrieve_name(function_derivative)
	domain, function = np.array(domain), np.array(function)
	BadDomainError = lambda domain_name: f"ERROR! Input domain, '{domain_name}' was neither an n x 1 nor a 1 x n array."
	BadFunctionError = lambda function_name: f"ERROR! Input range, '{function_name}' was neither an n x 1 nor a 1 x n array or LaTeX string expression."
	BadDataError = lambda domain_name, function_name: f"ERROR! Arrays '{domain_name}' and '{function_name}' must be of equal length."
	BadFunctionDerivativeError = lambda function_derivative_name: "ERROR! Input function derivative range, 'function_derivative_name}'was neither function nor expression and not an one-dimensional array."
	BadFunctionDerivativeDataError = lambda domain_name, function_name, function_derivative_name: f"ERROR! Arrays '{domain_name}', '{function_name}', and '{function_derivative_name}' must be of equal length."
	MissingDerivativeError = lambda function_derivative_name: "ERROR! Missing derivative data or expression assignment for 'function_derivative_name}'"
	MadePolyInformation = lambda polynomial_str: f"Information: I have found your requested polynomial! P = {polynomial_str}"
	if np.sum(domain.shape) > domain.shape[0]: raise ValueError(BadDomainError(domain_name))
	# if isinstance(function, (str, FunctionType)):
	# 	# if isinstance(function, str):
	# 	# 	function_str = ex.fast_parse_latex(function)
	# 	# 	function = lambda x: ex.fast_eval_latex(function_str, {variable: x})
	# 	g = make_array(domain, function)
	if isinstance(function, (list, tuple, np.ndarray)):
		if np.sum(np.array(function).shape) > np.array(function).shape[0]: raise ValueError(BadFunctionError(function_name))
		if len(domain) != len(function): raise ValueError(BadDataError(domain_name, function_name))
		g = np.array(function)
	else: raise ValueError("Unknown input.")
	if isinstance(function_derivative, type(None)):
		# if isinstance(function, FunctionType):
		# 	# if isinstance(function, str):
		# 	# 	fp_str = ex.fast_derive_latex(ex.fast_parse_latex(function), variable)
		# 	# 	fp = lambda x: ex.fast_eval_latex(fp_str, {variable: x})
		# 	# elif isinstance(function, FunctionType):
		# 	# fp = sp.lambdify(sp.Symbol(variable), sp.diff(function(sp.Symbol(variable))))
		# 	# else:
		# 	#print("Warning! " + missing_FP)
		# 	if len(domain) >= 3: point_type="three"
		# 	elif len(domain) >= 5: point_type="five"
		# 	#fp = [endpoint(domain, g, domain[1]-domain[0], "left", point_type)]
		# 	#for i in range(1, len(domain) - 1):
		# 	#	fp.append(midpoint(domain, g, domain[i]-domain[i-1], i, point_type))
		# 	#fp.append(endpoint(domain, g, domain[-2]-domain[-1], "right", point_type))
		# 	obj = Derivative(domain, g, domain[1]-domain[0], point_type=point_type, variable=variable)
		# 	fp = [obj.endpoint(0)]
		# 	for i in range(1, len(domain) - 1):
		# 		fp.append(obj.midpoint(i))
		# 	fp.append(obj.endpoint(-1))
		# 	gp = make_array(domain, fp)
		# else:
		if isinstance(g, (list, tuple, np.ndarray)):
			if np.sum(g.shape) > np.sum(g.shape[0]): raise ValueError(BadFunctionDerivativeError(function_derivative_name))
			if len(domain) != len(g): raise ValueError(BadFunctionDerivativeDataError(domain_name, function_name, function_derivative_name))
			if len(domain) >= 3: point_type="three"
			elif len(domain) >= 5: point_type="five"
			obj = Derivative(domain, g, domain[1]-domain[0], point_type=point_type, variable=variable)
			fp = [obj.endpoint(0)]
			for i in range(1, len(domain) - 1):
				fp.append(obj.midpoint(i))
			fp.append(obj.endpoint(-1))
			gp = np.array(fp)
		else: raise(TypeError("Uknown input."))
	elif not isinstance(function_derivative, type(None)):
		# if isinstance(function_derivative,(str, FunctionType)):
		# 	if isinstance(function_derivative, str):
		# 		function_derivative_str = ex.fast_parse_latex(function_derivative)
		# 		function_derivative = lambda x: ex.fast_eval_latex(function_derivative_str, {variable: x})
		# 	gp = make_array(domain, function_derivative)
		if isinstance(function_derivative, (list, tuple, np.ndarray)):
			if np.sum(function_derivative.shape) > np.sum(function_derivative.shape[0]): raise ValueError(BadFunctionDerivativeError(function_derivative_name))
			if len(domain) != len(function_derivative): raise ValueError(BadFunctionDerivativeDataError(domain_name, function_name, function_derivative_name))
			gp = np.array(function_derivative)
		else: raise ValueError(MissingDerivativeError(function_derivative_name))
	else: raise ValueError(MissingDerivativeError(function_derivative_name))
	m, n = 2*len(domain)+1, len(domain)
	Q, Z = np.zeros((m,m)), np.zeros(m)
	for i in range(n):
		Z[2*i], Z[2*i + 1] = domain[i], domain[i]
		Q[2*i][0], Q[2*i + 1][0] = g[i], g[i]
		Q[2*i + 1][1] = gp[i]
		if i != 0: Q[2*i][1] = (Q[2*i][0] - Q[2*i - 1][0]) \
			/ (Z[2*i] - Z[2*i - 1])
	for i in range(2, m):
		for j in range(2, i + 1):
			Q[i][j] = (Q[i][j - 1] - Q[i - 1][j - 1]) / (Z[i] - Z[i - j])
	# i, y, terms = 0, 1, []
	# while i < n:
	# 	j, xi = 2*i, (sp.Symbol(variable) - domain[i])
	# 	qjj, qj1 = Q[j][j], Q[j + 1][j + 1]
	# 	terms.append(qjj*y)
	# 	y = y*xi
	# 	terms.append(qj1*y)
	# 	y = y*xi
	# 	i += 1
	# polynomial = sp.lambdify(sp.Symbol(variable), sp.simplify(sum(terms)))
	polynomial, terms = 0, 1
	for i in range(n):
		j = 2*i
		polynomial += Q[j][j]*terms
		j = 2*i + 1
		terms *= sp.Symbol(variable) - domain[i]
		polynomial += Q[j][j]*terms
		terms *= sp.Symbol(variable) - domain[i]
	polynomial = sp.lambdify(sp.Symbol(variable), sp.simplify(polynomial))
	# polynomial_str, terms = f"0", "1"
	# for i in range(n):
	# 	j = 2*i
	# 	polynomial_str += f"+({Q[j][j]}*{terms})"
	# 	j = 2*i + 1
	# 	terms = f"({terms})*({variable} - {domain[i]})"
	# 	polynomial_str += f"+({Q[j][j]}*{terms})"
	# 	terms = f"({terms})*({variable} - {domain[i]})"
	# polynomial = lambda x: ex.fast_eval_latex(polynomial_str, {variable: x})
	# polynomial = sp.lambdify(sp.Symbol(variable), sp.simplify(sp.sympify(polynomial_str)))
	#print("Congratulations! ", made_poly + str(polynomial(sp.Symbol(variable))))
	return polynomial

def lagrange(
	domain: tuple,
	function: tuple,
	variable: Optional[str]="x"
) -> Tuple[FunctionType, np.ndarray]:
	"""Given a domain and range, construct a Lagrangian polynomial.

	Parameters
	----------
	domain : tuple
		Input domain.

	function : tuple
		Desired/Found range of interest.

	variable : string
		Respected variable in derivative of equation. Assumed to be `'x'` if not stated.

	Returns
	-------
	polynomial : lambda
		Lambdified Lagrangian polynomial.

	errors : np.ndarray
		Propogation of bounding error through construction.

	Raises
	------
	BadDomainError : string
		If `domain` is not a one-dimensional array.

	BadFunctionError : string
		If `function` is not a one-dimensional array.

	BadDataError : string
		If `domain` and `function` are of unequal length.

	Warns
	-----
	MadePolyInformation : string
		Displays the string form of the equation.

	See Also
	--------
	make_array() : Prints string that expression was used to make array.

	Notes
	--------
	Polynomial will quickly begin to oscillate for larger data sets.

	Finds a polynomial of degree n-1.

	Polynomial is of the following form:
	P(x) = f(x0)L_(n,0)(x) + ... + f(xn)L_(n,n)(x), where

	L_(n,k) = prod_(i=0, i!=k)^(n) (x - xi)/(xk - xi)

	Examples
	--------
	A Lagrange polynomial between (2,4) and (5,1) would be found as follows:
	L_(0)(x) = (x - 5)/(2 - 5) = -(x - 5)/3

	L_(1)(x) = (x - 2)/(5 - 2) = (x - 2)/3

	=>  P(x)	= (4)*(-(x - 5)/3) + (1)*((x - 2)/3)
				= -x + 6
	"""
	def term(xk, yk, x):
		num, den, L_k = [], [], []
		for xl in domain:
			if xl != xk:
				num.append(x-xl)
				den.append(xk-xl)
		L_k = np.divide(np.prod(num), np.prod(den))
		return L_k * yk
	def error(n, xi, x):
		roots, g, xi_error = [], [], []
		for i in range(n+1):
			root = domain[i]
			roots.append(x - root)
			g = np.prod(roots)
			for k in range(n+1):
				xi = sp.simplify(sp.diff(xi))
			dxi = np.abs(xi.evalf(subs={x: root})/(math.factorial(k)))
			xi_error.append(np.abs(dxi))
			xi_err = np.max(xi_error)
			g_prime = sp.diff(g)
			r = sp.solve(g_prime)
			if i == 0:
				r = g_prime
				gx = g.evalf(subs={x: r})
			elif i == 1:
				gx = g.evalf(subs={x: r[0]})
			else:
				R = []
				for s in r:
					if not isinstance(s, complex):
						R.append(g.evalf(subs={x: s}))
				gx = np.amax(np.abs(R))
		return np.abs(xi_err*gx)
	domain_name, function_name = _retrieve_name(domain), _retrieve_name(function)
	domain, function = np.array(domain), np.array(function)
	BadDomainError = lambda domain_name: f"ERROR! Input domain, '{domain_name}' was neither an n x 1 nor a 1 x n array."
	BadFunctionError = lambda function_name: f"ERROR! Input range, '{function_name}' was neither an n x 1 nor a 1 x n array or LaTeX string expression."
	BadDataError = lambda domain_name, function_name: f"ERROR! Arrays '{domain_name}' and '{function_name}' must be of equal length."
	MadePolyInformation = lambda polynomial_str: f"Information: I have found your requested polynomial! P = {polynomial_str}"
	if np.sum(domain.shape) > np.sum(domain.shape[0]): raise ValueError(BadDomainError(domain_name))
	# if isinstance(function, (str, FunctionType)):
	# 	function = make_array(domain, function)
	if isinstance(function, (list, tuple, np.ndarray)):
		if np.sum(function.shape) > np.sum(function.shape[0]): raise ValueError(BadFunctionError(function_name))
		elif len(domain) != len(function): raise ValueError(BadDataError(domain_name, function_name))
	else: raise TypeError(BadFunctionError(function_name))
	k, terms, errors = 0, [], np.zeros(len(domain))
	for xk in domain:
		terms.append(term(xk, function[k], sp.Symbol(variable)))
		errors[k] = error(k, sp.simplify(sum(terms)), sp.Symbol(variable))
		k += 1
	polynomial = sp.lambdify(sp.Symbol(variable), sp.simplify(sum(terms)))
	#print(MadePolyInformation(str(polynomial)))
	return polynomial, errors

class least_squares:
	"""Interpolate across all points in data set to minimize error according to rule of fit.
	"""
	def __init__(
		self,
		domain: tuple,
		function: tuple
	):
		"""Given a domain and range, construct some polynomial.

		Parameters
		----------
		domain : tuple
			Input domain.

		function : tuple
			Range of interest.

		Raises
		------
		BadDomainError : string
			If `domain` is not a one-dimensional array.

		BadFunctionError : string
			If `function` is not a one-dimensional array.

		BadDataError : string
			If `domain` and `function` are of unequal length.
		"""
		self.__domain_name, self.__function_name = _retrieve_name(domain), _retrieve_name(function)
		BadDomainError = lambda domain_name: f"ERROR! Input domain, '{domain_name}' was neither an n x 1 nor a 1 x n array."
		BadFunctionError = lambda function_name: f"ERROR! Input range, '{function_name}' was neither an n x 1 nor a 1 x n array."
		BadDataError = lambda domain_name, function_name: f"Arrays '{domain_name}' and '{function_name}' must be of equal length."
		domain, function = np.array(domain), np.array(function)
		if np.sum(domain.shape) > np.sum(domain.shape[0]): raise ValueError(BadDomainError(self.__domain_name))
		if np.sum(function.shape) > np.sum(function.shape[0]): raise ValueError(BadFunctionError(self.__function_name))
		if len(domain) != len(function): raise ValueError(BadDataError(self.__domain_name, self.__function_name))
		self.domain, self.function = domain, function

	__MadePolynomialInformation = lambda polynomial_str: f"Information: I have found your requested polynomial! P = {polynomial_str}"

	def linear(
		self,
		degree: int,
		variable: Optional[str]="x"
	) -> Tuple[FunctionType, float]:
		"""Construct a polynomial of some degree.

		Parameters
		----------
		degree : int
			Degree of polynomial.

		Returns
		-------
		polynomial : lambda
			Lambdified linear least square polynomial.

		error : float
			Total error.

		Raises
		------
		BadDegreeError : string
			If prescribed `degree` is not an integer or is zero.

		See Also
		--------
		MultiVariableIteration().gauss_seidel() : Utilize the Gauss-Seidel method to solve small system of equations.
		"""
		BadDegreeError = lambda n: f"ERROR! Degree of polynomial, n='{n}' must be integer and greater than zero."
		if not isinstance(degree,(int)) or degree <= 0: raise ValueError(BadDegreeError(degree))
		X, Y = self.domain, self.function
		m = len(X)
		A, x = np.zeros((degree+1, degree+1)), np.ones((degree+1,1))
		b = np.zeros_like(x)
		for i in range(degree+1):
			for j in range(degree+1):
				for k in range(m):
					A[i][j] += (X[k])**(i + j)
			for j in range(m):
				b[i] += Y[j]*(X[j]**(i))
		# x = np.linalg.solve(A, b)
		x = EigenValues(A).conjugate_gradient(x, b)["Lambdas"].values[-1]
		# x = MultiVariableIteration(A, x, b).gauss_seidel()["Approximations"].values[-1]
		polynomial = 0
		for i in range(len(x)): polynomial += x[i]*(sp.Symbol(variable)**i)
		polynomial = sp.lambdify(sp.Symbol(variable), sp.simplify(polynomial))
		# polynomial_str = "0"
		# for i in range(len(x)): polynomial_str += f"+{x[i]}(({variable})^({i}))"
		# polynomial_str = ex.fast_parse_latex(polynomial_str)
		# polynomial = lambda x: ex.fast_eval_latex(polynomial_str, {variable: x})
		#print(least_squares.__MadePolynomialInformation(polynomial_str))
		error = 0
		for i in range(len(x)):
			error += float(Y[i] - polynomial(x[i]))**2
		return polynomial, error

	def power(
		self
	) -> Tuple[float, float, FunctionType]:
		"""Given a domain and range, yield the coefficients for an equation of the form `y = A*(x^B)`.

		Returns
		-------
		a : float
			Leading coefficient.

		b : float
			Exponent.

		expression : lambda
			Lambda expression of curve-fit with calculated leading coefficient, `a` and exponent, `b`.

		"""
		X, Y = self.domain, self.function
		q1, q2, q3, q4 = [], [], [], []
		for i in range(len(X)):
			q1.append(math.log(X[i])*math.log(Y[i]))
			q2.append(math.log(X[i]))
			q3.append(math.log(Y[i]))
			q4.append(math.log(X[i])**2)
		num = len(X)*np.sum(q1) - np.sum(q2)*np.sum(q3)
		den = len(X)*np.sum(q4) - (np.sum(q2))**2
		b = num/den
		a = math.exp((np.sum(q3) - b*np.sum(q2))/len(X))
		expression = lambda x: a*(x**b)
		# expression = lambda x: ex.fast_eval_latex(f"{a}*x^{b}", {"x": x})
		return a, b, expression

def linear_interpolation(
	x0: float,
	y0: float,
	x1: float,
	y1: float,
	x: float
) -> float:
	"""y = y0 + (x - x0)*(y1 - y0)/(x1 - x0)
	"""
	return y0 + (x - x0)*(y1 - y0)/(x1 - x0)

def newton_difference(
	domain: tuple,
	function: Union[tuple,FunctionType],
	center_point: float,
	variable: Optional[str]="x",
	direction: Optional[str]="auto"
) -> FunctionType:
	"""Given a domain and range, construct some polynomial by Newton's Divided Difference.

	Parameters
	----------
	domain : tuple
		Input domain.

	function : tuple or lambda
		Desired/Found range of interest.

	center_point : float
		Point about which polynomial is evaluated.

	direction : string
		`'forward'` or `'backward'` construction. Will be chosen automatically if not specified.

	Returns
	-------
	polynomial : lambda
		Lambdified constructed polynomial.

	Raises
	------
	BadDomainError : string
		If `domain` is not a one-dimensional array.

	BadFunctionError : string
		If `function` is not a one-dimensional array.

	BadDataError : string
		If `domain` and `function` are of unequal length.

	BadDirectionError : string
		If `direction` is neither `'forward'` nor `'backward'`.

	Warns
	-----
	MadePolynomialInformation : string
		Displays the string form of the equation.

	See Also
	--------
	make_array() : Prints string that expression was used to make array.

	Notes
	-----
	Direction will be chosen if not specified.

	Polynomials best made with even spacing in `domain`; although, this is not completely necessary.
	"""
	domain_name, function_name = _retrieve_name(domain), _retrieve_name(function)
	BadDomainError = lambda domain_name: f"ERROR! Input domain, '{domain_name}' was neither an n x 1 nor a 1 x n array."
	BadFunctionError = lambda function_name: f"ERROR! Input function, '{function_name}' was neither an n x 1 nor a 1 x n array."
	BadDataError = lambda domain_name, function_name: f"ERROR! Arrays '{domain_name}' and '{function_name}' must be of equal length."
	BadDirectionError = lambda direction: f"ERROR! Supplied direction ('{direction}') was not understood. Please specify 'forward' or 'backward', or let me choose."
	MadePolynomialInformation = lambda polynomial_str: f"Information: I have found your requested polynomial! P = {polynomial_str}"
	domain, center_point = np.array(domain), float(center_point)
	if isinstance(function, FunctionType):
		# if isinstance(function, str):
		# 	function_str = ex.fast_parse_latex(function)
		# 	function = lambda x: ex.fast_eval_latex(function_str, {variable: x})
		# #print("String expression converted to lambda function.")
		function = make_array(domain, function)
	elif isinstance(function, (list, tuple, np.ndarray)):
		function = np.array(function)
	if np.sum(domain.shape) > domain.shape[0]: raise ValueError(BadDomainError(domain_name))
	if np.sum(function.shape) > function.shape[0]: raise ValueError(BadFunctionError(function_name))
	if len(domain) != len(function): raise ValueError(BadDataError(domain_name, function_name))
	if direction == "auto":
		if center_point <= np.median(domain): direction = "forward"
		else: direction = "backward"
	elif direction != "forward" and direction != "backward": raise ValueError(BadDirectionError(direction))
	fterm = lambda fxn, i, j: (fxn[i][j] - fxn[i-1][j])/(fxn[i][0] - fxn[i-j][0])
	m, n = len(domain), len(domain) + 1
	fxn, coeff = np.zeros((m,n)), []
	m, n = m - 1, n - 1	 # change m and n from length to index
	fxn[:,0], fxn[:,1] = domain, function
	for j in range(1, m):
		for i in range(1, m):
			fk = fterm(fxn, i, j)
			fxn[i][j+1] = fk
			if direction == "forward" and i == j:
				coeff.append(fk)
			elif direction == "backward" and i == m - 1:
				coeff.append(fk)
	# polynomial, terms = [], []
	# for c in coeff:
	# 	terms.append(sp.Symbol(variable) - domain[coeff.index(c)])
	# 	polynomial.append(c*np.prod(terms))
	# if direction == "forward": polynomial = sp.simplify(sum(polynomial) + function[0])
	# elif direction == "backward": polynomial = sp.simplify(sum(polynomial) + function[m])
	polynomial, terms = 0, 1
	for c in coeff:
		terms *= sp.Symbol(variable) - domain[coeff.index(c)]
		polynomial += c*np.prod(terms)
	if direction == "forward": polynomial = sp.simplify(polynomial + function[0])
	elif direction == "backward": polynomial = sp.simplify(polynomial + function[m])
	#print(MadePolynomialInformation(polynomial_str))
	polynomial = sp.lambdify(sp.Symbol(variable), polynomial)
	# for c in coeff:
	# 	term_str += f"(x - {domain[coeff.index(c)]})"
	# 	polynomial_str += f"+{c}*{term_str}"
	# if direction == "forward": polynomial_str += f"+{function[0]}"
	# elif direction == "backward": polynomial_str += f"+{function[m]}"
	# #print(MadePolynomialInformation(polynomial_str))
	# polynomial = lambda x: ex.fast_eval_latex(polynomial_str, {variable: x})
	return polynomial
# --------------------

# --------------------
# numerical differentiation and integration
class Derivative:
	def __init__(
		self,
		domain: tuple,
		function: Union[tuple,FunctionType],
		h: float,
		point_type: Optional[str]="three",
		variable: Optional[str]="x"
	):
		"""Find the derivative at an endpoint of data set.

		Parameters
		----------
		domain : tuple
			Domain of collected data.

		function : tuple or lambda
			Range of collected data.

		h : float
			Step-size through interval.

		which_point : int
			Dictates whether evaluated point is left or right most data point.

		point_type : string, optional
			Determines if 3 or 5 pt. method is used. 3 pt. is selected by default.

		Raises
		------
		BadDomainError : IndexError
			If `domain` is not a one-dimensional array.

		BadFunctionError : ValueError
			If `function` is not an expression.

		BadDataError : IndexError
			If `domain` and `function` are of unequal length.

		See Also
		--------
		make_array() : Prints string that expression was used to make array.

		Notes
		-----
		5 point is more accurate than 3 point; however, round-off error increases.
		"""
		self.__domain_name, self.__function_name = _retrieve_name(domain), _retrieve_name(function)
		BadDomainError = lambda domain_name: f"ERROR! Input domain, '{domain_name}' was neither an n x 1 nor a 1 x n array."
		BadFunctionError = lambda function_name: f"ERROR! Input function, '{function_name}' was neither an n x 1 nor a 1 x n array."
		BadDataError = lambda domain_name, function_name: f"ERROR! Arrays '{domain_name}' and '{function_name}' must be of equal length."
		BadTypeError = lambda type: f"ERROR! I am sorry. The selected type, '{type}' was not understood. Please select: 'three', 'five', or '2nd_derivative'."
		if isinstance(function, FunctionType):
			# if isinstance(function, str):
			# 	self.function_str = function_str = ex.fast_parse_latex(function)
			# 	function = lambda x: ex.fast_eval_latex(function_str, {variable: x})
			# else: self.function_str = function_str = "Lambda"
			self.function = make_array(domain, function)
		elif isinstance(function, (list, tuple, np.ndarray)):
			if np.sum(np.array(domain).shape) > np.array(domain).shape[0]: raise ValueError(BadDomainError(self.__domain_name))
			if np.sum(np.array(function).shape) > np.array(function).shape[0]: raise ValueError(BadFunctionError(self.__function_name))
			if len(domain) != len(function): raise ValueError(BadDataError(self.__domain_name, self.__function_name))
			self.function = np.array(function)
		else: raise ValueError("Uknown input.")
		self.step_size = h = float(h)
		if point_type != "three" \
			and point_type != "five" \
				and point_type != "2nd_derivative": raise ValueError(BadTypeError(point_type))
		else: self.point_type = point_type
		self.variable = variable
		
	__BadPointError = lambda index: f"ERROR! Index, '{index}' must be an integer."

	def endpoint(
		self,
		point: int
	) -> float:
		"""Find the derivative of a bookend point at either end of a dataset.
		Returns
		-------
		derivative : float
			Evaluated derivative at point.
		"""
		if not isinstance(point,int): raise ValueError(Derivative.__BadPointError(point))
		else: i = point
		derivative = 0
		if i == 0:
			if self.point_type == "three":
				derivative = (-3*self.function[i] + 4*self.function[i+1] - self.function[i+2])/(2*self.step_size)
			if self.point_type == "five":
				derivative = (-25*self.function[i] + 48*self.function[i+1] \
					- 36*self.function[i+2] + 16*self.function[i+3] \
						- 3*self.function[i+4])/(12*self.step_size)
		elif i == -1 or i == len(self.domain)-1:
			if self.point_type == "three":
				derivative = (-3*self.function[i] + 4*self.function[i-1] - self.function[i-2])/(2*self.step_size)
			if self.point_type == "five":
				derivative = (-25*self.function[i] + 48*self.function[i-1] \
					- 36*self.function[i-2] + 16*self.function[i-3] \
						- 3*self.function[i-4])/(12*self.step_size)
		return derivative

	def midpoint(
		self,
		point: int
	) -> float:
		"""Find the derivative of some point within a dataset.
		Returns
		-------
		derivative : float
			Evaluated derivative at point.
		"""
		if not isinstance(point,int): raise ValueError(Derivative.__BadPointError(point))
		else: i = point
		derivative = 0
		if self.point_type == "three":
			derivative = (self.function[i+1] - self.function[i-1])/(2*self.step_size)
		elif self.point_type == "five":
			derivative = (self.function[i-2] - 8*self.function[i-1] \
				+ 8*self.function[i+1] - self.function[i+2])/(12*self.step_size)
		elif self.point_type == "2nd_derivative":
			derivative = (self.function[i-1] - 2*self.function[i] + self.function[i+1])/(self.step_size**2)
		return derivative

class integrate:
	"""Find the numeric integral.
	"""
	def __init__(
		self,
		function: Union[tuple,FunctionType],
		domain: Optional[tuple]=None,
		a: Optional[float]=0,
		b: Optional[float]=0,
		h: Optional[float]=0,
		variable: Optional[str]="x",
		scheme: Optional[str]="open"
	):
		"""Find the integral of a function within some interval, using Simpson's Rule.

		Parameters
		----------
		function : tuple or lambda
			Polynomial equation that defines graphical curve.

		domain : tuple
			Domain over which `function` is evaluated.

		a : float
			Left-hand bound of interval.

		b : float
			Right-hand bound of interval.

		h : float
			Step-size through interval.

		Raises
		------
		BadDomainError : string
			If `domain` is not a one-dimensional array.

		BadFunctionError : string
			If `function` is not an expression.

		Notes
		-----
		`domain = None` if not a list nor one-dimensional array.

		Unless specified and if `domain` is defined, `a` and `b` will be the minimum and maximum, respectively, of `X`.
		"""
		self.__domain_name, self.__function_name = _retrieve_name(domain), _retrieve_name(function)
		BadDomainError = lambda domain_name: f"ERROR! Input domain, '{domain_name}' was neither an n x 1 nor a 1 x n array."
		BadFunctionError = lambda function_name: f"ERROR! Input range, '{function_name}' must be expression, not list or tuple."
		if isinstance(domain, type(None)):
			domain = np.arange(a, b+h, h)
		elif np.sum(np.array(domain).shape) > np.sum(np.array(domain).shape[0]):
			raise ValueError(BadDomainError(self.__domain_name))
		else: raise ValueError(BadDomainError(self.__domain_name))
		if isinstance(function, (list, tuple, np.ndarray)):
			function = np.array(function)
		elif isinstance(function, FunctionType):
			# if isinstance(function, str):
			# 	self.function_str = function_str = ex.fast_parse_latex(function)
			# 	function = lambda x: ex.fast_eval_latex(function_str, {variable: x})
			self.function = function = make_array(domain, function)
			#print("String expression converted to lambda function.")
		#elif not isinstance(function,(FunctionType, sp.Expr)):
		#	if np.sum(domain.shape) > np.sum(domain.shape[0]): raise ValueError("ERROR! " + bad_X)
		#	else: raise ValueError("ERROR! " + bad_f)
		else: raise ValueError(BadFunctionError(self.__function_name))
		self.domain = np.array(domain)
		self.variable = variable
		if a == 0: a = domain[0]
		if b == 0: b = domain[-1]
		if h == 0: h = domain[1]-domain[0]
		self.a, self.b, self.h = float(a), float(b), float(h)
		self.scheme = scheme

	def simpson(
		self
	) -> Tuple[np.ndarray, np.ndarray, float]:
		"""Theorem:
		Let f be in C4[a,b], n be even, h = (b-a)/n, and xj = a + jh for j = 0, 1, ..., n. There exists a mu in (a,b) for which the quadrature for n sub-intervals can be written with its error term as:
		int_(a)^(b)f(x)dx = h[f(a) + 2*[sum_(j=1)^(n/2 - 1){f(x_(2j))}] + 4*[sum_(j=1)^(n/2){f(x_(2j-1))}] + f(b)]/3 - (b-a)*(h^4)f''''(mu)/180.

		Where: (b-a)*(h^4)f''''(mu)/180 -> O(h^4)

		Returns
		-------
		X : np.ndarray
			Domain used to calculate numeric integral.

		Y : np.ndarray
			Range used to calculate numeric integral.

		F : float
			Numeric integral.
		"""
		f, X = self.function, self.domain
		a, b, h = self.a, self.b, self.h
		if self.scheme == "open":
			n = math.ceil((b-a)/h)
			XJ1, XJ2, XJ, = [], [], [a]
			YJ1, YJ2, YJ, = [], [], [f(a) if not isinstance(f, np.ndarray) else f[0]]
			for j in range(1, int(n/2)):
				XJ1.append(a + 2*j*h)
				YJ1.append(f(XJ1[-1]) if not isinstance(f, np.ndarray) else f[2*j])
			z1 = np.sum(YJ1)
			for j in range(1, int(n/2+1)):
				XJ2.append(a + (2*j - 1)*h)
				YJ2.append(f(XJ2[-1]) if not isinstance(f, np.ndarray) else f[2*j-1])
			z2 = np.sum(YJ2)
			for k in range(np.array(XJ1).shape[0]):
				XJ.append(XJ2[k]); YJ.append(YJ2[k])
				XJ.append(XJ1[k]); YJ.append(YJ1[k])
			XJ.append(XJ2[k]); YJ.append(YJ2[k])
			XJ.append(b)
			YJ.append(f(b) if not isinstance(f, np.ndarray) else f[-1])
			X = XJ; Y = YJ
			if not isinstance(f, np.ndarray): F = h/3*(f(a) + 2*z1 + 4*z2 + f(b))
			else: F = h/3*(f[0] + 2*z1 + 4*z2 + f[-1])
		elif self.scheme == "closed":
			if not isinstance(f, np.ndarray): Y = make_array(X, f)
			else: Y = f
			F = 3*h/8*(Y[0] + 3*(np.sum(Y[1:-1])) + Y[-1])
		return X, Y, F

	def trapezoidal(
		self
	) -> Tuple[np.ndarray, np.ndarray, float]:
		"""Theorem:
		Let f be in C2[a,b], h = (b-a)/n, and xj = a + jh for j = 0, 1, ..., n. There exists a mu in (a,b) for which the quadrature for n sub-intervals can be written with its error term as:
		int_(a)^(b)f(x)dx = h[f(a) + 2*[sum_(j=1)^(n - 1){f(xj)}] + f(b)]/2 - (b-a)*(h^2)f''(mu)/12.

		Where: (b-a)*(h^2)f''(mu)/12 -> O(h^2)

		Returns
		-------
		X : np.ndarray
			Domain used to calculate numeric integral.

		Y : np.ndarray
			Range used to calculate numeric integral.

		F : float
			Numeric integral.
		"""
		f, X = self.function, self.domain
		a, b, h = self.a, self.b, self.h
		if self.scheme == "open":
			XJ, YJ = [a], [f(a) if not isinstance(f, np.ndarray) else f[0]]
			n = math.ceil((b-a)/h)
			for j in range(1, n):
				XJ.append(a + j*h)
				YJ.append(f(XJ[-1]) if not isinstance(f, np.ndarray) else f[j])
			z = np.sum(YJ[1:])
			XJ.append(b);
			YJ.append(f(b) if not isinstance(f, np.ndarray) else f[-1])
			X = XJ; Y = YJ
			if not isinstance(f, np.ndarray): F = h/2*(f(a) + 2*z + f(b))
			else: F = h/2*(Y[0] + 2*z + Y[-1])
		elif self.scheme == "closed":
			if not isinstance(f, np.ndarray):
				Y = make_array(X, f)
				if a < X[0]: Y[0] = f(a)
				if b > X[-1]: Y[-1] = f(b)
			else: Y = f
			F = h/2*(Y[0] + Y[-1])
		return X, Y, F

def gaussian_legendre(function, a, b):
	return sc.integrate.quad(function, a, b)

def richard_extrapolation(
	function: Union[FunctionType,tuple],
	center_point: float,
	h: float,
	order: int,
	direction: Optional[str]="auto",
	variable: Optional[str]="x",
	domain: Optional[tuple]=None,
) -> FunctionType:
	"""Results in higher-accuracy of derivative at point in function with lower-order formulas to minimize round-off error and increase O(h) of truncation error.

	Parameters
	----------
	function : lambda or tuple
		Polynomial over which derivative must be calculated.

	center_point : float
		Point about which extrapolation centers

	h : float
		Step-size through interval.

	order : int
		Order for rate of convergence.

	direction : string
		`'forward'` or `'backward'` construction.

	Returns
	-------
	polynomial : lambda
		Lambdified constructed polynomial.

	polynomial(x0) : float
		Evaluation of `polynomial` at `center_point`.

	Raises
	------
	BadExpressionError : string
		If `function` is not an expression.

	BadOrderError : string
		`order` must be an integer and non-zero.

	BadDirectionError : string
		If `direction` is neither `'forward'` nor `'backward'`.

	See Also
	--------
	newton_difference() : Newton Difference method to build extrapolation for function's derivative and order of error.
	"""
	function_name = _retrieve_name(function)
	BadExpressionError = lambda function_name: f"ERROR! Function, '{function_name}' must be a lambda expression."
	BadOrderError = lambda order: f"ERROR! Order, n='{order}' must be an integer greater than zero."
	BadDirectionError = lambda direction: f"ERROR! Supplied direction ('{direction}') was not understood. Please specify 'forward' or 'backward'."
	BadDataError = lambda domain_name, function_name: f"ERROR! Arrays '{domain_name}' and '{function_name}' must be of equal length."
	if not isinstance(order, int): raise TypeError(BadOrderError(order))
	if direction != "auto" and direction != "forward" and direction != "backward": raise ValueError(BadDirectionError(direction))
	if isinstance(function, FunctionType):
		# if isinstance(function, str):
		# 	function_str = ex.fast_derive_latex(ex.fast_parse_latex(function), variable)
		# 	function = lambda x: ex.fast_eval_latex(function_str, {variable: x})
		center_point, h = float(center_point), float(h)
		X, FX = [], []
		for i in range(order+1):
			dx = h / (2**order) * (2**i)
			X.append(center_point + dx)
			FX.append(function(center_point + dx))
	#elif isinstance(function,(FunctionType, sp.Expr)):
	#	sym_function = sp.N(sp.sympify(function(variable)))
	#	function = sp.lambdify(variable, sym_function)
	#	print(f"Information: Input expression, {sym_function} used.")
	#elif isinstance(function, (list, tuple, np.ndarray)):
	#	if np.sum(np.array(domain).shape) != 0 and len(domain) == len(function):
	#		X, FX = np.array(domain), np.array(function)
	#	else: raise ValueError(BadDataError(_retrieve_name(domain), function_name))
	else:
		raise TypeError(BadExpressionError(function_name))
	return newton_difference(X, FX, center_point, variable=variable, direction=direction)
# --------------------

# --------------------
# differential equations
class __ode(object):
	"""Assign common attributes to objects.
	"""
	def __init__(
		self,
		function: Tuple[FunctionType],
		a: float,
		b: float,
		alpha: float,
		variables: Optional[Tuple[str]]=("t", "y"),
		steps: Optional[int]=100
	):
		"""
		Parameters
		----------
		function : lambda
			Time derivative of function to approximate.

		a : float
			Initial time.

		b : float
			Final time.

		alpha : float
			Initial value at a.

		variables : tuple, optional
			Collection of symbolic or string variables to respect in function.

		steps : int or float, optional
			Maximum number of time steps to discretize domain.

		Yields
		------
		self.function : expression
			Time derivative of function to approximate.

		self.a : float
			Initial time.

		self.b : float
			Final time.

		self.alpha : float
			Initial value at a.

		self.variables : tuple, optional
			Collection of symbolic or string variables to respect in function.

		self.steps : int or float, optional
			Maximum number of time steps to discretize domain.

		Raises
		------
		ValueError
			If time steps constraint is not an integer.

		TypeError
			If input expression cannot be understood as lambda or sympy expression nor as string.

		Notes
		-----
		Make sure the independent variable is the first element of `variables`!
		"""
		if steps <= 0 or not isinstance(steps, (int, float)): raise ValueError(f"ERROR! Number of time steps, N must be an integer greater than zero. {steps} was given and not understood.")
		if np.sum(np.array(function).shape) > 0:
			F, F_str = [], []
			for f in function:
				# if isinstance(f, str):
				# 	#g = lambda x: eval(f)
				# 	#f = sp.lambdify(*variables, g(*variables))
				# 	function_str = ex.fast_parse_latex(f)
				# 	F_str.append(function_str)
				# 	f = lambda t, y: ex.fast_eval_latex(function_str, {"t": t, "y": y})
				# 	#print("String expression converted to lambda function.")
				# elif isinstance(f, FunctionType):
				# 	F_str.append("Lambda")
				# else: raise TypeError("Unknown input.")
				if isinstance(f, FunctionType): F.append(f)
			function = F
			# function_str = F_str
		else:
			# if isinstance(function, str):
			# 	#g = lambda x: eval(function)
			# 	#function = sp.lambdify(*variables, g(*variables))\
			# 	function_str = ex.fast_parse_latex(function)
			# 	function = lambda t, y: ex.fast_eval_latex(function_str, {"t": t, "y": y})
			# 	#print("String expression converted to lambda function.")
			# elif isinstance(function, FunctionType):
			# 	#sym_function = sp.N(sp.sympify(function(*variables)))
			# 	#function = sp.lambdify(variables, sym_function)
			# 	#print(f"Information: Input expression, {sym_function} used.")
			# 	function_str = "Lambda"
			# else: raise TypeError("Unknown input.")
			if not isinstance(function, FunctionType): raise TypeError("Unknown input.")
		self.function = function
		# self.function_str = function_str
		self.a, self.b = a, b
		self.step_size = float((b - a)/(steps + 1))
		self.alpha = alpha
		self.variables = variables
		self.steps = int(steps + 1)

class ivp(__ode):
	"""Class containing Initial Value Problem methods.
	"""
	def __init__(
		self,
		function: Tuple[FunctionType],
		a: float,
		b: float,
		alpha: float,
		variables: Optional[Tuple[str]]=("t", "y"),
		steps: Optional[int]=100
	) -> pd.DataFrame:
		"""
		Parameters
		----------
		function : expression
			Time derivative of function to approximate.

		a : float
			Initial time.

		b : float
			Final time.

		alpha : float
			Initial value at a.

		variables : tuple, optional
			Collection of symbolic or string variables to respect in function.

		steps : int or float, optional
			Maximum number of time steps to discretize domain.

		Attributes
		----------
		forward_euler()

		improved_euler()

		backward_euler()

		crank_nicholson()

		runge_kutta()

		Yields
		------
		self.function : expression
			Time derivative of function to approximate.

		self.a : float
			Initial time.

		self.b : float
			Final time.

		self.alpha : float
			Initial value at a.

		self.variables : tuple, optional
			Collection of symbolic or string variables to respect in function.

		self.steps : int or float, optional
			Maximum number of time steps to discretize domain.

		Raises
		------
		ValueError
			If time steps constraint is not an integer.

		TypeError
			If input expression cannot be understood as lambda or sympy expression nor as string.

		Notes
		-----
		Make sure the independent variable is the first element of `variables`!
		"""
		super().__init__(function, a, b, alpha, variables=variables, steps=steps)

	def forward_euler(self) -> pd.DataFrame:
		"""March forward through time to approximate Initial Value Problem differential equation between endpoints a and b.

		Returns
		-------
		pandas.Dataframe() : DataFrame
			Dataframe of method iterations and time domains, range of approximations for input function, and iterative increments.

		Yields
		------
		self.step_size : float
			Domain step size.

		self.iterations : np.ndarray
			Collection of steps through method.

		self.domain : np.ndarray
			Discretized domain between endpoints a and b for so many steps.

		self.range : np.ndarray
			Range mapped from method through discretized domain between endpoints a and b for so many steps.

		self.increments : np.ndarray
			Collection of increments between steps.

		Raises
		------
		TypeError
			If input expression cannot be understood as lambda or sympy expression nor as string.
		"""
		h, t, w0 = self.step_size, self.a, self.alpha
		Y, increments = [w0], [0]
		for i in range(1, self.steps):
			t = self.a + i*h
			w = w0 + h*self.function(t, w0)
			Y.append(w)
			increments.append(w - w0)
			w0 = w
		self.iterations = np.arange(self.steps)
		self.domain = np.linspace(self.a, t+h, self.steps)
		self.range = np.array(Y)
		self.increments = np.array(increments)
		return pd.DataFrame(data={
			"Iterations": self.iterations,
			"Domain": self.domain,
			"Range": self.range,
			"Increments": self.increments
		})

	def improved_euler(self) -> pd.DataFrame:
		"""Approximate solution of Initial Value Problem differential equation given initial time, initial value, and final time.

		Returns
		-------
		pandas.Dataframe() : dataframe
			Dataframe of method iterations and time domains, range of approximations for input function, and iterative increments.

		Yields
		------
		self.step_size : float
			Domain step size.

		self.iterations : tuple
			Collection of steps through method.

		self.domain : tuple
			Discretized domain between endpoints a and b for so many steps.

		self.range : tuple
			Range mapped from method through discretized domain between endpoints a and b for so many steps.

		self.increments : tuple
			Collection of increments between steps.

		Raises
		------
		TypeError
			If input expression cannot be understood as lambda or sympy expression nor as string.

		See Also
		--------
		runge_kutta()

		Notes
		-----
		Is 2nd-Order Runge-Kutta method where endpoint a = b = 0.5 and lambda = 1.
		"""
		h, t, w0 = self.step_size, self.a, self.alpha
		ea, eb, lam = 1/2, 1/2, 1
		Y, increments = [w0], [0]
		for i in range(1, self.steps):
			t = self.a + i*h
			w = w0 + h*(ea*self.function(t, w0) + eb*self.function(t + lam*h, w0 + lam*h*self.function(t, w0)))
			Y.append(w)
			increments.append(abs(w - w0))
			w0 = w
		self.iterations = np.arange(self.steps)
		self.domain = np.linspace(self.a, t+h, self.steps)
		self.range = np.array(Y)
		self.increments = np.array(increments)
		return pd.DataFrame(data={
			"Iterations": self.iterations,
			"Domain": self.domain,
			"Range": self.range,
			"Increments": self.increments
		})

	def backward_euler(self) -> pd.DataFrame:
		"""Use information at next time step to approximate Initial Value Problem differential equation between endpoints a and b.

		Returns
		-------
		pandas.Dataframe() : dataframe
			Dataframe of method iterations and time domains, range of approximations for input function, and iterative increments.

		Yields
		------
		self.step_size : float
			Domain step size.

		self.iterations : tuple
			Collection of steps through method.

		self.domain : tuple
			Discretized domain between endpoints a and b for so many steps.

		self.range : tuple
			Range mapped from method through discretized domain between endpoints a and b for so many steps.

		self.increments : tuple
			Collection of increments between steps.

		Raises
		------
		TypeError
			If input expression cannot be understood as lambda or sympy expression nor as string.

		See Also
		--------
		SingleVariableIteration.newton_raphson()
		"""
		h, t, w0 = self.step_size, self.a, self.alpha
		Y, increments = [w0], [0]
		for i in range(1, self.steps):
			t = self.a + i*h
			# w = w0 + h*function(t + h, w0 + h*function(t, w0))
			w = lambda x: x - (w0 + h*self.function(t + h, x))
			#w = "x - (w0 + h*" + self.function_str + ")"
			#sys.stdout =  open(os.devnull, "w")
			obj = SingleVariableIteration(w, t, t+h, iter_guess=100)
			w = obj.newton_raphson(w0)["Approximations"].values[-1]
			#sys.stdout = sys.__stdout__
			Y.append(w)
			increments.append(abs(w - w0))
			# t, w0 = a + i*h, w
			w0 = w
		self.iterations = np.arange(self.steps)
		self.domain = np.linspace(self.a, t+h, self.steps)
		self.range = np.array(Y)
		self.increments = np.array(increments)
		return pd.DataFrame(data={
			"Iterations": self.iterations,
			"Domain": self.domain,
			"Range": self.range,
			"Increments": self.increments
		})

	def runge_kutta(self) -> pd.DataFrame:
		"""Approximate solution of initial value problem.

		Returns
		-------
		pandas.Dataframe() : dataframe
			Dataframe of method iterations and time domains, range of approximations for input function, and iterative increments.

		Yields
		------
		self.step_size : float
			Domain step size.

		self.iterations : tuple
			Collection of steps through method.

		self.domain : tuple
			Discretized domain between endpoints a and b for so many steps.

		self.range : tuple
			Range mapped from method through discretized domain between endpoints a and b for so many steps.

		self.increments : tuple
			Collection of increments between steps.

		Raises
		------
		TypeError
			If input expression cannot be understood as lambda or sympy expression nor as string.
		"""
		h, t, w0 = self.step_size, self.a, self.alpha
		Y, increments = [w0], [0]
		for i in range(1, self.steps):
			t = self.a + i*h
			k1 = h*self.function(t, w0)
			k2 = h*self.function(t + h/2, w0 + k1/2)
			k3 = h*self.function(t + h/2, w0 + k2/2)
			k4 = h*self.function(t + h, w0 + k3)
			w = w0 + (k1 + 2*k2 + 2*k3 + k4) / 6
			Y.append(w)
			increments.append(w - w0)
			w0 = w
		self.iterations = np.arange(self.steps)
		self.domain = np.linspace(self.a, t+h, self.steps)
		self.range = np.array(Y)
		self.increments = np.array(increments)
		return pd.DataFrame(data={
			"Iterations": self.iterations,
			"Domain": self.domain,
			"Range": self.range,
			"Increments": self.increments
		})

	def trapezoidal(
		self,
		power: float=-6,
		max_iter: int=100
	) -> pd.DataFrame:
		"""Use information at next time step to approximate Initial Value Problem differential equation between endpoints a and b.

		Parameters
		----------
		power : int or float, optional
			Signed power to which function error must be within.

		max_iter : int, optional
			Maximum iterations for Newton-Raphson loop.

		Returns
		-------
		pandas.Dataframe() : dataframe
			Dataframe of method iterations and time domains, range of approximations for input function, and iterative increments.

		Yields
		------
		self.step_size : float
			Domain step size.

		self.iterations : tuple
			Collection of steps through method.

		self.domain : tuple
			Discretized domain between endpoints a and b for so many steps.

		self.range : tuple
			Range mapped from method through discretized domain between endpoints a and b for so many steps.

		self.increments : tuple
			Collection of increments between steps.

		Raises
		------
		TypeError
			If input expression cannot be understood as lambda or sympy expression nor as string.
		"""
		h, t, w0 = self.step_size, self.a, self.alpha
		self.tol = 10**power
		variables = [sp.symbols(v) for v in self.variables]
		fpy = sp.lambdify(variables, sp.diff(self.function(*variables), variables[0]))
		Y, increments = [w0], [0]
		for i in range(1, self.steps):
			t = self.a + i*h
			k1 = w0 + h*self.function(t, w0)/2
			j, wj0, do_calc = 1, k1, True
			while do_calc:
				wj1 = wj0 - (wj0 - h/2*self.function(t + h, wj0) - k1)/(\
					1 - h/2*fpy(t + h, wj0))
				if abs(wj1 - wj0) <= self.tol:
					w, do_calc = wj1, False
				else:
					wj0 = wj1; j += 1
					if j >= max_iter: do_calc = False
			# f = lambda x: x - h/2*self.function(t + h, x) - k1
			# obj = SingleVariableIteration(f, self.a, self.b, power, variable="t", iter_guess=max_iter)
			# w = obj.newton_raphson(k1)["Approximations"].values[-1]
			Y.append(w)
			increments.append(abs(w - w0))
			w0 = w
		self.iterations = np.arange(self.steps)
		self.domain = np.linspace(self.a, t+h, self.steps)
		self.range = np.array(Y)
		self.increments = np.array(increments)
		return pd.DataFrame(data={
			"Iterations": self.iterations,
			"Domain": self.domain,
			"Range": self.range,
			"Increments": self.increments
		})

class bvp(__ode):
	"""Class containing Boundary Value Problem methods.
	"""
	def __init__(
		self,
		function: Tuple[FunctionType],
		a: float,
		b: float,
		alpha: float,
		beta: float,
		variables: Optional[Tuple[str]]=("x", "y", "yp"),
		steps: int=100
	) -> pd.DataFrame:
		"""
		Parameters
		----------
		function : lambda
			Time derivative of function to approximate.

		a : float
			Initial time.

		b : float
			Final time.

		alpha : float
			Initial value at a.

		beta : float
			Initial value at b.

		variables : tuple, optional
			Collection of symbolic or string variables to respect in function.

		steps : int or float, optional
			Maximum number of time steps to discretize domain.

		Attributes
		----------
		linear_shooting_method()

		finite_difference_method()

		Yields
		------
		self.function : expression
			Time derivative of function to approximate.

		self.a : float
			Initial time.

		self.b : float
			Final time.

		self.alpha : float
			Initial value at a.

		self.beta : float
			Initial value at b.

		self.variables : tuple, optional
			Collection of symbolic or string variables to respect in function.

		self.steps : int or float, optional
			Maximum number of time steps to discretize domain.

		Raises
		------
		ValueError
			If time steps constraint is not an integer.

		TypeError
			If input expression cannot be understood as lambda or sympy expression nor as string.

		Notes
		-----
		Make sure the independent variable is the first element of `variables`!
		"""
		super().__init__(function, a, b, alpha, variables=variables, steps=steps)
		self.beta = beta

	def linear_shooting_method(self):
		"""Solve a Boundary Value Problem differential equation with 2 Initial Value Problem differential equations.

		Returns
		-------
		pandas.Dataframe() : DataFrame
			Dataframe of method iterations and time domains, range of approximations for input function, and iterative increments.

		Yields
		------
		self.step_size : float
			Domain step size.

		self.iterations : tuple
			Collection of steps through method.

		self.domain : tuple
			Discretized domain between endpoints a and b for so many steps.

		self.range : tuple
			Range mapped from method through discretized domain between endpoints a and b for so many steps.

		self.derivatives : tuple
			Collection of derivatives at each step.

		Raises
		------
		TypeError
			If input expression cannot be understood as lambda or sympy expression nor as string.
		"""
		h, alpha, beta = self.step_size, self.alpha, self.beta
		u1, u2, v1, v2 = [alpha], [0], [0], [1]
		p, q, r, ypp = self.function
		for i in range(self.steps):
			t = self.a + i*h
			k11 = h*u2[i]
			k12 = h*(p(t)*u2[i] + q(t)*u1[i] + r(t))
			k21 = h*(u2[i] + k12/2)
			k22 = h*(p(t + h/2)*(u2[i] + k12/2) + q(t + h/2)*(u1[i] + k11/2) + r(t + h/2))
			k31 = h*(u2[i] + k22/2)
			k32 = h*(p(t + h/2)*(u2[i] + k22/2) + q(t + h/2)*(u1[i] + k21/2) + r(t + h/2))
			k41 = h*(u2[i] + k32)
			k42 = h*(p(t + h)*(u2[i] + k32) + q(t + h)*(u1[i] + k31) + r(t + h))
			u1.append(u1[i] + (k11 + 2*k21 + 2*k31 + k41)/6)
			u2.append(u2[i] + (k12 + 2*k22 + 2*k32 + k42)/6)
			###############################
			k11 = h*v2[i]
			k12 = h*(p(t)*v2[i] + q(t)*v1[i])
			k21 = h*(v2[i] + k12/2)
			k22 = h*(p(t + h/2)*(v2[i] + k12/2) + q(t + h/2)*(v1[i] + k11/2))
			k31 = h*(v2[i] + k22/2)
			k32 = h*(p(t + h/2)*(v2[i] + k22/2) + q(t + h/2)*(v1[i] + k21/2))
			k41 = h*(v2[i] + k32)
			k42 = h*(p(t + h)*(v2[i] + k32) + q(t + h)*(v1[i] + k31))
			v1.append(v1[i] + (k11 + 2*k21 + 2*k31 + k41)/6)
			v2.append(v2[i] + (k12 + 2*k22 + 2*k32 + k42)/6)
		w1, w2 = [alpha], [(beta - u1[-1])/v1[-1]]
		for i in range(1, self.steps+1):
			w1.append(u1[i] + w2[0]*v1[i])
			w2.append(u2[i] + w2[0]*v2[i])
			t = self.a + i*h
		self.iterations = np.arange(self.steps+1)
		self.domain = np.linspace(self.a, self.b, self.steps+1)
		self.range = np.array(w1)
		self.derivatives = np.array(w2)
		return pd.DataFrame(data={
			"Iterations": self.iterations,
			"Domain": self.domain,
			"Range": self.range,
			"Derivatives": self.derivatives
		})

	def finite_difference_method(
		self,
		solver_method="gauss_seidel"
	) -> Tuple[pd.DataFrame,pd.DataFrame]:
		"""Solve a Boundary Value Problem differential equation with 2 Initial Value Problem differential equations.

		Parameters
		----------
		solver_method : str, optional
			Unless specified, system of equations will be solved by the 'gauss_seidel' method.

		Returns
		-------
		pandas.Dataframe() : DataFrame
			Dataframe of method iterations and time domains, range of approximations for input function, and iterative increments.

		pandas.Dataframe() : DataFrame
			Dataframe of cumulative errors through the required number of iterations according to `solver_method`.

		Yields
		------
		self.step_size : float
			Domain step size.

		self.iterations : tuple
			Collection of steps through method.

		self.domain : tuple
			Discretized domain between endpoints a and b for so many steps.

		self.range : tuple
			Range mapped from method through discretized domain between endpoints a and b for so many steps.

		self.derivatives : tuple
			Collection of derivatives at each step.

		Raises
		------
		TypeError
			If input expression cannot be understood as lambda or sympy expression nor as string.

		ValueError
			Prescribed method is not an available option.

		See Also
		--------
		MultiVariableIteration.gauss_seidel()

		MultiVariableIteration.successive_relaxation()

		MultiVariableIteration.jacobi()
		"""
		h, alpha, beta = self.step_size, self.alpha, self.beta
		ai, bi, ci, di = [], [], [], []
		p, q, r, ypp = self.function
		t = self.a + h
		ai.append(2 + (h**2)*q(t))
		bi.append(-1 + (h/2)*p(t))
		di.append(-(h**2)*r(t) + (1 + (h/2)*p(t))*alpha)
		for i in range(2, self.steps):
			t = self.a + i*h
			ai.append(2 + (h**2)*q(t))
			bi.append(-1 + (h/2)*p(t))
			ci.append(-1 - (h/2)*p(t))
			di.append(-(h**2)*r(t))
		t = self.b - h
		ai.append(2 + (h**2)*q(t))
		ci.append(-1 - (h/2)*p(t))
		di.append(-(h**2)*r(t) + (1 - (h/2)*p(t))*beta)
		#A = np.zeros((self.steps, self.steps))
		#np.fill_diagonal(A, ai)
		A = np.diagflat(ai)
		A = A + np.diagflat(bi, 1)
		t = A + np.diagflat(ci, -1)
		x = np.zeros(self.steps)
		c = np.array(di)
		obj = MultiVariableIteration(A, x, c, max_iter=1000)
		if solver_method == "gauss_seidel":
			obj.gauss_seidel()
		elif solver_method == "successive_relaxation":
			obj.successive_relaxation()
		elif solver_method == "jacobi":
			obj.jacobi()
		else: raise ValueError("ERROR! The desired method must be: 'gauss_seidel', 'successive_relaxation', or 'jacobi'.")
		approximations = obj.approximations[-1]
		approximations = np.insert(approximations, 0, alpha)
		approximations = np.append(approximations, beta)
		# return pd.DataFrame(data={"Iterations": range(len(np.linspace(a, b, N+2))), "Domain": np.linspace(a, b, N+2), "Range": approximations}), foo.iterations, foo.errors
		self.iterations = np.arange(self.steps+2)
		self.domain = np.linspace(self.a, self.b, self.steps+2)
		self.range = np.array(approximations)
		return pd.DataFrame(data={
			"Iterations": self.iterations,
			"Domain": self.domain,
			"Range": self.range
		}), pd.DataFrame(data={
			"Iterations": obj.iterations,
			"Errors": obj.errors
		})
# --------------------
#   #   #   #   #   #   #   #   #


#################################
## Test
# test compile of module.
class test:					 # test class
	def test():				 # test function
		"""Was the module loaded correctly?

		Raises
		------
		success : string
			Prints a message of successful function call.
		"""
		success = "Test complete."
		sys.exit(success)
#   #   #   #   #   #   #   #   #


#################################
## End of Code
# test.test()	 # "Test complete."
#   #   #   #   #   #   #   #   #