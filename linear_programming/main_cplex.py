import cplex

my_prob = cplex.Cplex()

my_prob.objective.set_sense(my_prob.objective.sense.maximize)

my_obj = [2.0, 3.0, 2.0]
my_lb = [0.0, 0.0, 0.0]
my_ub = [cplex.infinity, cplex.infinity, cplex.infinity]
my_ctype = "CCC"
my_colnames = ["x1", "x2", "x3"]
my_prob.variables.add(obj=my_obj, lb=my_lb, ub=my_ub, types=my_ctype, names=my_colnames)

rows = [[["x1", "x2", "x3"], [1.0, 4.0, 2.0]], [["x1", "x2"], [3.0, 2.0]]]
my_sense = "LL"
my_rhs = [8.0, 6.0]
my_rownames = ["r1", "r2"]
my_prob.linear_constraints.add(lin_expr=rows, senses=my_sense, rhs=my_rhs, names=my_rownames)
my_prob.solve()

slack = my_prob.solution.get_linear_slacks()
x = my_prob.solution.get_values()

print("Solution value  = ", my_prob.solution.get_objective_value())
print('slack:')
print(slack)
print('x: ')
print(x)

print()
