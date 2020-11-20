# matrix form

from gurobipy import *
import numpy as np

try:

    # Create a new model
    m = Model("mip1")

    # Create variables
    x = m.addMVar(shape=3, lb=0, name="x")

    obj_vec = np.array([2, 3, 2])
    # Set objective
    m.setObjective(obj_vec @ x, GRB.MAXIMIZE)

    con_mat = np.array([[1, 4, 2], [3, 2, 0]])
    con_vec = np.array([8, 6])

    # Add constraint
    m.addConstr(con_mat @ x <= con_vec, "c")

    m.optimize()

    for v in m.getVars():
        print(v.varName, v.x)

    print('Obj:', m.objVal)

except GurobiError:
    print('Error reported')
