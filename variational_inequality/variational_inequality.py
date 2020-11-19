# @Time    : 2020/5/1 11:23
# @Author  : gzzang
# @File    : main
# @Project : variational_inequality


import pdb

import numpy as np
import cvxpy as cp
import gurobipy as gp
from gurobipy import GRB
import time

gp.setParam('OutputFlag', 0)
np.set_printoptions(precision=2, suppress=True)


def cal_unconstrained_mp(parameter_vector, is_display=False):
    variable_number = parameter_vector.shape[0]
    x = cp.Variable(variable_number)
    mp_func = lambda x_ar: sum((x_ar - parameter_vector) ** 2 / 2)

    objective = cp.Minimize(mp_func(x))
    constraints = []
    prob = cp.Problem(objective, constraints)
    result = prob.solve()
    if is_display:
        print(f'optimal objective value: {objective.value}')
        print(f'optimal value: {x.value}')
    return x.value


def cal_unconstrained_vi(parameter_vector, is_display=False):
    variable_number = parameter_vector.shape[0]
    initial_value = np.zeros(variable_number)
    tolerance = 1e-10
    iteration_number = 5000
    termination_bool = False
    optimum_bool = False
    iteration_index = 0
    while not (termination_bool or optimum_bool):
        if iteration_index == 0:
            current_value = initial_value
            gap = 1
        else:
            matrix_h = np.eye(variable_number)
            rho = 0.1
            matrix_quadratic = matrix_h / 2
            vector_quadratic = rho * current_func_value.reshape([1, variable_number]) - matrix_h @ current_value

            m = gp.Model()
            var = m.addMVar(shape=(variable_number,), lb=-GRB.INFINITY)
            m.setObjective(var @ matrix_quadratic @ var + vector_quadratic @ var, GRB.MINIMIZE)
            m.optimize()
            new_value = var.x

            gap = np.linalg.norm(x=new_value - current_value, ord=2)
            if gap < tolerance:
                optimum_bool = True
            elif iteration_index == iteration_number:
                termination_bool = True

            current_value = new_value

        vi_func = lambda x_ar: x_ar - parameter_vector
        current_func_value = vi_func(current_value)

        iteration_index += 1
    if is_display:
        print('--------')
        print(f'iteration_index:{iteration_index}')
        print(f'gap:{gap}')
        print(f'current_route_time:{current_func_value}')
        print(f'current_route_flow:{current_value}')
        print('--------')
    return current_value


def cal_constrained_mp(parameter_vector, parameter_value, is_display=False):
    variable_number = parameter_vector.shape[0]
    x = cp.Variable(variable_number)
    mp_func = lambda x_ar: sum((x_ar - parameter_vector) ** 2 / 2)

    objective = cp.Minimize(mp_func(x))
    constraints = [x >= 0]
    constraints += [sum(x) == parameter_value]
    prob = cp.Problem(objective, constraints)
    result = prob.solve()
    if is_display:
        print(f'optimal objective value: {objective.value}')
        print(f'optimal value: {x.value}')
    return x.value


def cal_constrained_vi(parameter_vector, parameter_value, is_display=False):
    variable_number = parameter_vector.shape[0]
    initial_value = np.zeros(variable_number)
    tolerance = 1e-10
    iteration_number = 5000
    termination_bool = False
    optimum_bool = False
    iteration_index = 0
    while not (termination_bool or optimum_bool):
        if iteration_index == 0:
            current_value = initial_value
            gap = 1
        else:
            matrix_h = np.eye(variable_number)
            rho = 0.1
            matrix_quadratic = matrix_h / 2
            vector_quadratic = rho * current_func_value.reshape([1, variable_number]) - matrix_h @ current_value

            m = gp.Model()
            var = m.addMVar(shape=(variable_number,))
            m.addConstr(np.ones(variable_number) @ var == parameter_value)
            m.setObjective(var @ matrix_quadratic @ var + vector_quadratic @ var, GRB.MINIMIZE)
            m.optimize()
            new_value = var.x

            gap = np.linalg.norm(x=new_value - current_value, ord=2)
            if gap < tolerance:
                optimum_bool = True
            elif iteration_index == iteration_number:
                termination_bool = True

            current_value = new_value

        vi_func = lambda x_ar: x_ar - parameter_vector
        current_func_value = vi_func(current_value)

        iteration_index += 1
    if is_display:
        print('--------')
        print(f'iteration_index:{iteration_index}')
        print(f'gap:{gap}')
        print(f'current_route_time:{current_func_value}')
        print(f'current_route_flow:{current_value}')
        print('--------')
    return current_value


a = np.array((1, 2, 0, 3))
b = 5

start_unconstrained_mp = time.time()
print(cal_unconstrained_mp(a, is_display=False))
end_unconstrained_mp = time.time()

start_unconstrained_vi = time.time()
print(cal_unconstrained_vi(a, is_display=False))
end_unconstrained_vi = time.time()

start_constrained_mp = time.time()
print(cal_constrained_mp(a, b, is_display=False))
end_constrained_mp = time.time()

start_constrained_vi = time.time()
print(cal_constrained_vi(a, b, is_display=False))
end_constrained_vi = time.time()


print(f'unconstrained_mp:{end_unconstrained_mp - start_unconstrained_mp}')
print(f'unconstrained_vi:{end_unconstrained_vi - start_unconstrained_vi}')
print(f'constrained_mp:{end_constrained_mp - start_constrained_mp}')
print(f'constrained_vi:{end_constrained_vi - start_constrained_vi}')
