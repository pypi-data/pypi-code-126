#!/usr/bin/env python
# Created by "Thieu" at 18:00, 06/07/2022 ----------%                                                                               
#       Email: nguyenthieu2102@gmail.com            %                                                    
#       Github: https://github.com/thieu1995        %                         
# --------------------------------------------------%

from opfunu.cec.cec2014 import unconstraint2

## CEC-2014 (3 ways to use depend on your purpose)

import numpy as np
from opfunu.cec.cec2014.function import F1, F2, F29
from opfunu.cec.cec2014.unconstraint2 import Model as MD2
from opfunu.cec.cec2014.unconstraint import Model as MD
from mealpy.human_based.TLO import BaseTLO
from mealpy.human_based.QSA import ImprovedQSA
from mealpy.physics_based.EFO import BaseEFO

problem_dict1 = {
   "fit_func": F29,
    "lb": [-100,]*50,
    "ub": [100,]*50,
    "minmax": "min",
}

epoch = 1000
pop_size = 50
model = BaseTLO(problem_dict1, epoch, pop_size)
best_position, best_fitness = model.solve()
print(f"Solution: {best_position}, Fitness: {best_fitness}")


# temp1 = BaseSpaSA(func, problem_size=10, domain_range=(-100, 100), log=True, epoch=epoch, pop_size=50)
# temp1._train__()
#
# temp2 = BaseEFO(func, problem_size=10, domain_range=(-100, 100), log=True, epoch=epoch, pop_size=50)
# temp2._train__()
#
# temp2 = ImprovedQSA(func, problem_size=10, domain_range=(-100, 100), log=True, epoch=epoch, pop_size=50)
# temp2._train__()



problem_size = 10
solution = np.random.uniform(0, 1, problem_size)

print(F29(solution))             # Function style

# func = MD(problem_size)         # Object style solve different problems with different functions
# print(func.F1(solution))
# print(func.F2(solution))
#
# obj = MD2(solution)             # Object style solve same problem with every functions
# print(obj.F1())
# print(obj.F2())