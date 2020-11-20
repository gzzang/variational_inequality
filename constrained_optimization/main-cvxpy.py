# @Time    : 2020/3/2 13:25
# @Author  : gzzang
# @File    : main-cvxpy
# @Project : constrained_optimization

import cvxpy as cp

x = cp.Variable(10)
objective = cp.Minimize(cp.power(x[0] + x[5], 2) + cp.power(x[1] + x[6], 2) + cp.power(x[2] + x[7], 2)
                        + cp.power(x[3] + x[8], 2) + cp.power(x[4] + x[9], 2))
constraints = [x >= 0]
constraints += [x[0] + x[1] + x[2] - 1.0 == 0,
               x[1] - x[3] - x[4] == 0,
               x[2] + x[4] == 0,
               x[6] - x[8] - x[9] == 0,
               x[5] + x[8] == 0,
               x[7] + x[9] - 2.0 == 0,
               x[0] + x[3] - 1.0 == 0,
               x[5] + x[6] + x[7] - 2.0 == 0,
               ]
prob = cp.Problem(objective, constraints)
result = prob.solve()

print(f'optimal objective value: {objective.value}')
print(f'optimal value: {x.value}')

