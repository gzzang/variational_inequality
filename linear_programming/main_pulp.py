import pulp

z = [2, 3, 2]
a = [[1, 4, 2], [3, 2, 0]]
b = [8, 6]
m = pulp.LpProblem(sense=pulp.LpMaximize)
x = [pulp.LpVariable(f'x{i}', lowBound=0) for i in [1, 2, 3]]
m += pulp.lpDot(z, x)
for i in range(len(a)):
    m += (pulp.lpDot(a[i], x) <= b[i])
m.solve()

print(f'目标：{pulp.value(m.objective)}')
print(f'变量：{[pulp.value(var) for var in x]}')
