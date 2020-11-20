from pymprog import *

p = model('example')
y = p.var('y', 3, int)
p.maximize(2 * y[0] + 3 * y[1] + 2 * y[2], 'master')
r1 = 1 * y[0] + 4 * y[1] + 2 * y[2] <= 8
r2 = 3 * y[0] + 2 * y[1] + 0 * y[2] <= 6
p.solve()
for i in range(3):
    print(y[i].primal)
