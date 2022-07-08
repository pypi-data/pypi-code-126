import liblip as ll
import sys
import math
import random

# Trace function
def trace( str):
    print( '######')
    print( "## ", str)
    print( '######')
    
# test function, here just a product of sin(2x)sin(2y),...
def fun2( dat, dim):
    s = 1.0
    for j in range( dim): s *= math.sin( 2 * dat[j])
    return s

# generate data randomly
def generate_random_data( dim, npts):
    x, XData, YData = ll.init( dim, npts)
    for i in range( npts):
        for j in range( dim):
            x[j] = random.random() * 3.0
            XData[i * dim + j] = x[j]
        YData[i] = fun2( x, dim)
    return x, XData, YData

###
# Initial test    
# ###  
def initial_test():
    trace( 'initial test: start')
    dim = 3
    npts = 1500
    lip_const = 10.0
    K2 = 100
           
    x, XData, YData = generate_random_data( dim, npts)

    ll.STCSetLipschitz( lip_const)
    ll.STCBuildLipInterpolant( dim, npts, XData, YData)

    err2 = 0
    err = 0
    for k in range( K2):
        for j in range( dim): x[j] = random.random() * 3.0 # randomly choose a test point
        w = ll.STCValue( x)
        w1 = fun2( x, dim) # the true function
        w = abs( w - w1) # compute the error
        if( err < w): err = w
        err2 += w * w    
    err2 = math.sqrt( err2 / K2) # average error RMSE
    print( "Interpolation max error: ",err)
    print( "Average error: ", err2)
    trace( 'initial test: end')

###
# example of usage of SLipInt class
###
def test_slip_int():
    trace( 'example of usage of SLipInt class: start')

    dim=4        # the dimension and size of the data set
    npts=1000
    LipConst=4
    x, XData, YData = generate_random_data( dim, npts)

    for j in range( dim): x[j]=random.random() * 3.0 # some random x
    # calculate the value
    index = [0] * npts
    w = ll.LipIntValue( dim,npts,x,XData, YData,LipConst,index)

    # estimate Lipschitz constant
    ll.LipIntComputeLipschitz(dim,npts,XData, YData)
    # uses the computed Lipschitz constant
    w = ll.LipIntValue(dim,npts,x,XData, YData,LipConst,index)
    print( "w: ", w)
    # the same using local Lipschitz constants  
    ll.LipIntComputeLocalLipschitz(dim,npts,XData, YData)
    # calculate the value
    w = ll.LipIntValueLocal(dim,npts,x,XData, YData)
    print( "w: ", w)
    trace( 'example of usage of SLipInt class: end')

###
# example of usage of SLipInt class for monotone interpolation
###
def test_slip_int_for_monotone_interpolation():
    trace( 'example of usage of SLipInt class for monotone interpolation: start')
    dim=4       # the dimension and size of the data set
    npts=1000
    LipConst=4
    x, XData, YData = generate_random_data( dim, npts)    
    Region = [1.5] * dim
    # function monotone incr. wrt first variable
    # function monotone decr. wrt first variable
    # unrestricted wrt other variables
    Cons = [0, -1, 0 ,0]

    # calculate the value
    w = ll.LipIntValueCons(dim,npts,Cons,x,XData, YData,LipConst, None)
    print( "w: ", w)
    # assume monotonicity for x<<Region only
    w = ll.LipIntValueConsLeftRegion(dim,npts,Cons,x,XData, YData, LipConst, Region, None)
    print( "w: ", w)
    ll.LipIntComputeLocalLipschitz(dim,npts,XData, YData)
    w = ll.LipIntValueLocalCons(dim,npts,Cons,x,XData, YData)
    print( "w: ", w)
    w = ll.LipIntValueLocalConsLeftRegion(dim,npts,Cons,x,XData, YData,Region)
    print( "w: ", w)
    trace( 'example of usage of SLipInt class for monotone interpolation: end')

###
# example of usage of SLipInt class with extra bounds
###
def test_slip_int_with_extra_bounds():
    trace( 'example of usage of SLipInt class with extra bounds: start')
    dim=4        # the dimension and size of the data set
    npts=1000
    LipConst=4

    # arrays to store the data
    x, XData, YData = generate_random_data( dim, npts)   
    # calculate the value
    w = ll.LipIntValue(dim,npts,x,XData, YData, LipConst, None)
    print( "w: ", w)
    # estimate Lipschitz constant
    ll.LipIntComputeLipschitz(dim,npts,XData, YData)
    # uses the computed Lipschitz constant
    w = ll.LipIntValue(dim,npts,x,XData, YData, LipConst, None)
    print( "w: ", w)
    trace( 'example of usage of SLipInt class with extra bounds: end')

###
# example of usage of STCInterpolant class
###
def test_STCInterpolant():
    trace( 'example of usage of STCInterpolant class: start')
    dim=4             # the dimension and size of the data set
    npts=1000

    # arrays to store the data
    x, XData, YData = generate_random_data( dim, npts)  
    # supply the data and eliminate repeated values
    ll.LipIntSetData(dim,npts, XData,YData,1)
    LipConst = ll.LipIntDetermineLipschitz()
    ll.LipIntSetConstants()  # supply Lipschitz constant
    ll.LipIntConstruct()     # construct the interpolant
    x1 = [0] * 10  # reserve space for at least dim+1 components
    w=ll.LipIntValueDim(dim,x1) # calculate the value
    print( "w: ", w)
    # alternatively, pre-compute the slack variable
    s = 0
    for j in range( 0, dim): s += x1[j]
    x1[dim] = 1.0-s
    w=ll.LipIntValueDim(dim+1,x1)         # calculate the value
    print( "w: ", w)
    w=ll.LipIntValueExplicitDim(dim+1,x1) # same using explicit method
    print( "w: ", w)
    ll.LipIntFreeMemory()  # destroys the interpolant
    trace( 'example of usage of STCInterpolant class: end')


###
# example of usage of STCInterpolant class
###
def test_STCInterpolantClass():
    trace( 'example of usage of STCInterpolant class: start')
    # dim=4             # the dimension and size of the data set
    # npts=1000
    # arrays to store the data
    dim = 4
    npts = 1000
    x, XData, YData = generate_random_data( dim, npts)  
    LipInt = []
    for i in range( 0, 10):
        print( "-- Instance: ", i, " dm: ", dim, " npts: ", npts)
        # supply the data and eliminate repeated values
        LipInt.append( ll.STCInterpolant())
        LipInt[i].SetData(dim,npts, XData,YData,1)
        LipConst = LipInt[i].DetermineLipschitz()
        LipInt[i].SetConstants()  # supply Lipschitz constant
        LipInt[i].Construct()     # construct the interpolant
        x1 = [0] * 10  # reserve space for at least dim+1 components
        w = LipInt[i].ValueDim(dim,x1) # calculate the value
        print( "w: ", w)
        # alternatively, pre-compute the slack variable
        s = 0
        for j in range( 0, dim): s += x1[j]
        x1[dim] = 1.0-s
        w =LipInt[i].ValueDim(dim+1,x1)         # calculate the value
        print( "w: ", w)
        w = LipInt[i].ValueExplicitDim(dim+1,x1) # same using explicit method
        print( "w: ", w)
        LipInt[i].FreeMemory()  # destroys the interpolant
    trace( 'example of usage of STCInterpolant class: end')



###
# example using procedural interface
###
def test_procedural_interface():
    trace( 'using using procedural interface: start')
    dim=4             # the dimension and the data set
    npts=1000

    # arrays to store the data
    LipConst = 10.0
    # arrays to store the data
    x, XData, YData = generate_random_data( dim, npts)

    # compute the Lipschitz constant in max-norm
    ll.LipIntInfComputeLipschitz( dim, npts, XData, YData)
    # calculate the value
    w=ll.LipIntInfValue( dim, npts,x,XData, YData, LipConst, None)
    print( "w: ", w)
    # the same in Euclidean norm, but using local Lipschitz values
    ll.LipIntComputeLocalLipschitz( dim, npts, XData, YData)
    # calculate the value
    w=ll.LipIntValueLocal( dim, npts,x,XData, YData)
    print( "w: ", w)
    # now using fast method and simplicial distance
    ll.STCSetLipschitz( LipConst)  # supply Lipschitz constant
    # suppy the data
    ll.STCBuildLipInterpolant( dim, npts, XData, YData)
    w=ll.STCValue( x) # calculate the value
    print( "w: ", w)
    trace( 'using using procedural interface: end')


###
# example using procedural interface class
###
def test_procedural_interface_class():
    trace( 'using using procedural interface: start')
    dim=4             # the dimension and the data set
    npts=1000

    # arrays to store the data
    LipConst = 10.0
    # arrays to store the data
    x, XData, YData = generate_random_data( dim, npts)

    # compute the Lipschitz constant in max-norm
    ll.LipIntInfComputeLipschitz( dim, npts, XData, YData)
    # calculate the value
    w=ll.LipIntInfValue( dim, npts,x,XData, YData, LipConst, None)
    print( "w: ", w)
    # the same in Euclidean norm, but using local Lipschitz values
    ll.LipIntComputeLocalLipschitz( dim, npts, XData, YData)
    # calculate the value
    w=ll.LipIntValueLocal( dim, npts,x,XData, YData)
    print( "w: ", w)
    # now using fast method and simplicial distance
    ll.STCSetLipschitz( LipConst)  # supply Lipschitz constant
    # suppy the data
    ll.STCBuildLipInterpolant( dim, npts, XData, YData)
    w=ll.STCValue( x) # calculate the value
    print( "w: ", w)
    trace( 'using using procedural interface: end')


###
# example for smoothing
###
def test_smoothing():
    trace( 'example for smoothing: start')
    dim=4        # the dimension and size of the data set
    npts=200
    LipConst=4.0
   
    # arrays to store the data
    x, XData, YData = generate_random_data( dim, npts)
    TData = [0.0] * npts
    for i in range( 0, npts): 
        YData[i] = fun2( x, dim)+ 0.1 * ( random.random() - 1)  # noisy function values
    ll.LipIntSmoothLipschitz(dim, npts,XData,YData,TData,LipConst, None, None, None, None, None, None)
    # other possibilities:
    #  ll.LipInt.SmoothLipschitzCons(dim, npts,Cons, XData,YData,TData,LipConst)
    #  ll.LipInt.SmoothLipschitzW(dim, npts,XData,YData,TData,LipConst,W)
    #  ll.LipInt.ComputeLipschitzCV(dim, npts,XData,YData,TData)
    #  etc...
   
    # calculate the approximation at x
    w = ll.LipIntValue(dim,npts,x,XData, TData, LipConst, None)
    print( "w: ", w)
    # prepare data for the fast method using simplicial distance
    ll.LipIntInfSmoothLipschitzSimp(dim, npts,XData,YData,TData,LipConst)
    ll.STCLipIntSetData(dim,npts, XData,TData)
    ll.STCLipIntSetConstants(LipConst)  # supply Lipschitz constant
    ll.STCLipIntConstruct()     # construct the interpolant
    x1 = [0.0] * 10  # reserve space for at least dim+1 components
    for j in range( 0, dim): x1[j] = random.random() * 3.0 # some random x
    w = ll.STCLipIntValue(dim,x1) # calculate the value
    print( "w: ", w)
    trace( 'example for smoothing: end')

###
# example of usage of STCInterpolant class and smoothened data
###
def test_STCInterpolant_smoothened_data():
    trace( 'example of usage of STCInterpolant class and smoothened data: start')
    dim=3             # the dimension and size of the data set
    npts=1000
    LipConst=2.5
    # arrays to store the data
    x, XData, YData = generate_random_data( dim, npts)
    TData = [0.0] * npts

    # smoothen the data
    ll.LipIntInfSmoothLipschitzSimp(dim,npts,XData,YData,TData,LipConst)
    # supply the smoothened data (TData, not YData)
    # ll.LipIntSetData(dim,npts, XData,TData,0)
    ll.LipIntSetConstants(LipConst)  # supply Lipschitz constant
    ll.LipIntConstruct()          # construct the interpolant
    x = [0.0] * 10  # reserve space for at least dim+1 components
    for j in range( 0, dim): random.random() * 3.0 # some random x
    w = ll.LipIntValue(dim,x1) # calculate the value
    print( "w: ", w)
    # alternatively, pre-compute the slack variable
    s = 0
    for j in range( 0, dim): s += x1[j] 
    x[dim] = 1.0 - s
    w = ll.LipIntValue(dim+1,x1)         # calculate the value
    print( "w: ", w)
    ll.LipIntFreeMemory()  # destroys the interpolant
    trace( 'example of usage of STCInterpolant class and smoothened data: end')

###
# Main test program
###
print( "-- test wrapper start --")
# initial_test() 
# test_slip_int()
# test_slip_int_for_monotone_interpolation()
# test_slip_int_with_extra_bounds()
# test_STCInterpolant()
# test_STCInterpolantClass()
test_procedural_interface()
# test_smoothing()
# test_STCInterpolant_smoothened_data()


print( "-- test wrapper end --")