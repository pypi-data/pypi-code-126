m = pyddm.Model(dt=.0001, dx=.0001)
#t=time.time(); _=m.solve_numerical_cn(); print(time.time()-t)
#t=time.time(); _=m.solve_numerical_implicit(); print(time.time()-t)
t=time.time(); _=m.solve_numerical_c(); print(time.time()-t)
