# @Time    : 2020/3/18 22:22
# @Author  : gzzang
# @File    : main_matrix
# @Project : quadratic_programming

import gurobipy as gp
from gurobipy import GRB

import numpy as np

m = gp.Model("qp2")
x = m.addMVar(shape=3, lb=0, ub=1.0, name='x')

mat = np.array([[1, 0.5, 0], [0.5, 1, 0.5], [0, 0.5, 1]])

vec = np.array([2, 0, 0])

con_mat = np.array([[1, 2, 3], [1, 1, 0]])
con_vec = np.array([4, 1])

m.addConstr(con_mat @ x >= con_vec)
obj = x @ mat @ x + vec @ x
m.setObjective(obj, GRB.MINIMIZE)
m.optimize()


for v in m.getVars():
    print('%s %g' % (v.varName, v.x))

print('Obj: %g' % obj.getValue())

x.vType = GRB.INTEGER

m.optimize()

for v in m.getVars():
    print('%s %g' % (v.varName, v.x))

print('Obj: %g' % obj.getValue())
