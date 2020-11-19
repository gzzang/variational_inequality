# @Time    : 2020/4/10 21:42
# @Author  : gzzang
# @File    : MyProblem
# @Project : genetic_algorithm

import numpy as np
import geatpy as ea


class MyProblem(ea.Problem):  # 继承Problem父类
    def __init__(self):
        name = 'MyProblem'  # 初始化name（函数名称，可以随意设置）
        M = 1  # 初始化M（目标维数）
        maxormins = [1]  # 初始化maxormins（目标最小最大化标记列表，1：最小化该目标；-1：最大化该目标）
        Dim = 6  # 初始化Dim（决策变量维数）
        varTypes = [1, 1, 1, 1, 1, 1]  # 初始化varTypes（决策变量的类型，元素为0表示对应的变量是连续的；1表示是离散的）
        lb = [1] * Dim  # 决策变量下界
        ub = [7] * Dim  # 决策变量上界
        lbin = [1] * Dim  # 决策变量下边界（0表示不包含该变量的下边界，1表示包含）
        ubin = [1] * Dim  # 决策变量上边界（0表示不包含该变量的上边界，1表示包含）
        # 调用父类构造方法完成实例化
        ea.Problem.__init__(self, name, M, maxormins, Dim, varTypes, lb, ub, lbin, ubin)

    def aimFunc(self, pop):  # 目标函数
        X = pop.Phen  # 得到决策变量矩阵
        x1 = X[:, [0]]
        x2 = X[:, [1]]
        x3 = X[:, [2]]
        x4 = X[:, [3]]
        x5 = X[:, [4]]
        x6 = X[:, [5]]
        pop.ObjV = (x1 - 1.5) * (x1 - 1.5) + (x2 - 3) * (x2 - 3) + (x3 - 4) * (x3 - 4) + (x4 - 4) * (x4 - 4) + (
                    x5 - 2) * (x5 - 2) + (x6 - 7) * (x6 - 7)  # 计算目标函数值，赋值给pop种群对象的ObjV属性
