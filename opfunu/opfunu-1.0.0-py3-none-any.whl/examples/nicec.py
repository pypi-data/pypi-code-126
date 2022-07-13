#!/usr/bin/env python
# Created by "Thieu" at 10:44, 09/07/2022 ----------%                                                                               
#       Email: nguyenthieu2102@gmail.com            %                                                    
#       Github: https://github.com/thieu1995        %                         
# --------------------------------------------------%

from opfunu.cec_based import F12010
import opfunu

t1 = opfunu.get_functions_by_classname("f12014")
print(t1)
print(len(t1))


#
# from opfunu.cec_based.cec2017 import F292017
#
# import numpy as np
# from mealpy.human_based.TLO import BaseTLO
# from mealpy.human_based.QSA import ImprovedQSA
# from mealpy.physics_based.EFO import BaseEFO
#
# ndim = 30
# f18 = F292017(ndim, f_bias=0)
#
# problem_dict1 = {
#     "fit_func": f18.evaluate,
#     "lb": f18.lb.tolist(),
#     "ub": f18.ub.tolist(),
#     "minmax": "min",
# }
#
# epoch = 1000
# pop_size = 50
# model = BaseTLO(problem_dict1, epoch, pop_size)
# best_position, best_fitness = model.solve()
# print(f"Solution: {best_position}, Fitness: {best_fitness}")
#
#
# # temp1 = BaseSpaSA(func, problem_size=10, domain_range=(-100, 100), log=True, epoch=epoch, pop_size=50)
# # temp1._train__()
# #
# # temp2 = BaseEFO(func, problem_size=10, domain_range=(-100, 100), log=True, epoch=epoch, pop_size=50)
# # temp2._train__()
# #
# # temp2 = ImprovedQSA(func, problem_size=10, domain_range=(-100, 100), log=True, epoch=epoch, pop_size=50)
# # temp2._train__()
#
