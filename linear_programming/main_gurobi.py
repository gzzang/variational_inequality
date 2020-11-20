from gurobipy import *

try:

    # Create a new model
    m = Model("mip1")

    # Create variables
    x1 = m.addVar(lb=0, name="x1")
    x2 = m.addVar(lb=0, name="x2")
    x3 = m.addVar(lb=0, name="x3")

    # Set objective
    m.setObjective(2 * x1 + 3 * x2 + 2 * x3, GRB.MAXIMIZE)

    # Add constraint
    m.addConstr(x1 + 4 * x2 + 2 * x3 <= 8, "c0")

    # Add constraint
    m.addConstr(3 * x1 + 2 * x2 <= 6, "c1")

    m.optimize()

    for v in m.getVars():
        print(v.varName, v.x)

    print('Obj:', m.objVal)

except GurobiError:
    print('Error reported')
