# @Time    : 2020/3/2 13:08
# @Author  : gzzang
# @File    : main-scipy
# @Project : constrained_optimization

import numpy as np
from scipy.optimize import minimize

e = 1e-10
fun = lambda x: (x[0] + x[5])**2 + (x[1] + x[6])**2 + (x[2] + x[7])**2 + (x[3] + x[8])**2 + (x[4] + x[9])**2

cons = (
    # {'type': 'eq', 'fun': lambda x: x[0] + x[1] + x[2] - 1.0},
    {'type': 'eq', 'fun': lambda x: x[1] - x[3] - x[4]},
    {'type': 'eq', 'fun': lambda x: x[0] + x[3] - 1.0},
    {'type': 'eq', 'fun': lambda x: x[2] + x[4]},
    # {'type': 'eq', 'fun': lambda x: x[5] + x[6] + x[7] - 2.0},
    {'type': 'eq', 'fun': lambda x: x[6] - x[8] - x[9]},
    {'type': 'eq', 'fun': lambda x: x[5] + x[8]},
    {'type': 'eq', 'fun': lambda x: x[7] + x[9] - 2.0},
    # 另一种不等式的约束方式避免线性相关
    # {'type': 'ineq', 'fun': lambda x: x[0] + x[1] + x[2] - 1.0 + e},
    # {'type': 'ineq', 'fun': lambda x: x[1] - x[3] - x[4] + e},
    # {'type': 'ineq', 'fun': lambda x: x[0] + x[3] - 1.0 + e},
    # {'type': 'ineq', 'fun': lambda x: x[2] + x[4] + e},
    # {'type': 'ineq', 'fun': lambda x: x[5] + x[6] + x[7] - 2.0 + e},
    # {'type': 'ineq', 'fun': lambda x: x[6] - x[8] - x[9] + e},
    # {'type': 'ineq', 'fun': lambda x: x[5] + x[8] + e},
    # {'type': 'ineq', 'fun': lambda x: x[7] + x[9] - 2.0 + e},
    # {'type': 'ineq', 'fun': lambda x: -(x[0] + x[1] + x[2] - 1.0) + e},
    # {'type': 'ineq', 'fun': lambda x: -(x[1] - x[3] - x[4]) + e},
    # {'type': 'ineq', 'fun': lambda x: -(x[0] + x[3] - 1.0) + e},
    # {'type': 'ineq', 'fun': lambda x: -(x[2] + x[4]) + e},
    # {'type': 'ineq', 'fun': lambda x: -(x[5] + x[6] + x[7] - 2.0) + e},
    # {'type': 'ineq', 'fun': lambda x: -(x[6] - x[8] - x[9]) + e},
    # {'type': 'ineq', 'fun': lambda x: -(x[5] + x[8]) + e},
    # {'type': 'ineq', 'fun': lambda x: -(x[7] + x[9] - 2.0) + e},
)
x0 = np.array((1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0))
res = minimize(fun, x0, bounds=[(0.0, None) for _ in range(10)], constraints=cons, options={'ftol': 1e-9, 'disp': False})

print(f'optimal objective value: {fun(res.x)}')
print(f'optimal value: {res.x}')
