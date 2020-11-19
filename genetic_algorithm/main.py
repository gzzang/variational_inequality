# @Time    : 2020/4/10 21:41
# @Author  : gzzang
# @File    : main
# @Project : genetic_algorithm

import numpy as np
import geatpy as ea
from MyProblem import MyProblem  # 导入自定义问题接口

if __name__ == '__main__':
    """================================实例化问题对象==========================="""
    problem = MyProblem()  # 生成问题对象
    """==================================种群设置==============================="""
    NIND = 40  # 种群规模
    # 创建区域描述器，变量用RI编码
    Encodings = 'RI'
    Field = ea.crtfld(Encodings, problem.varTypes, problem.ranges, problem.borders)
    population = ea.Population(Encodings, Field, NIND)  # 实例化种群对象（此时种群还没被初始化，仅仅是完成种群对象的实例化）
    """================================算法参数设置============================="""
    myAlgorithm = ea.soea_SGA_templet(problem, population)  # 实例化一个算法模板对象
    myAlgorithm.MAXGEN = 25  # 最大进化代数
    """===========================调用算法模板进行种群进化======================="""
    [population, obj_trace, var_trace] = myAlgorithm.run()  # 执行算法模板
    population.save()  # 把最后一代种群的信息保存到文件中
    # 输出结果
    best_gen = np.argmin(problem.maxormins * obj_trace[:, 1])  # 记录最优种群个体是在哪一代
    best_ObjV = obj_trace[best_gen, 1]
    print('最优的目标函数值为：%s' % (best_ObjV))
    print('最优的控制变量值为：')
    for i in range(var_trace.shape[1]):
        print(var_trace[best_gen, i])
    print('有效进化代数：%s' % (obj_trace.shape[0]))
    print('最优的一代是第 %s 代' % (best_gen + 1))
    print('评价次数：%s' % (myAlgorithm.evalsNum))
    print('时间已过 %s 秒' % (myAlgorithm.passTime))
