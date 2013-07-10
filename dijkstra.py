#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Алгоритм Дейкстры
#   Находит кратчайшее расстояние от одной из вершин графа до всех остальных. 
#   Алгоритм работает только для графов без рёбер отрицательного веса.
#   Матрица задается как список словарей смежности вершин
# Описание алгоритма http://goo.gl/KsqC


def dijkstra_shortest_path(graph, start):

    p = {} # наименьшие пути обхода
    u = [] # обработанные вершины
    p[start] = 0 # инициализация начального пути
    min_x = None # 
    
    while len(u) <= len(graph) and (min_x or len(p) == 1):
        print "start V: %d, " % (start)
        for x in graph[start]:
            if (x not in u and x != start):
                if (x not in p.keys() or (graph[start][x] + p[start]) < p[x]):
                    p[x] = graph[start][x] + p[start]

        u.append(start)

        min_v = 0
        min_x = None
        for x in p:
            # print "x: %d, p[x]: %d, mv %d" % (x, p[x], min_v)
            if (p[x] < min_v or min_v == 0) and x not in u:
                    min_x = x
                    min_v = p[x]
        start = min_x
        
    return p

if __name__ == '__main__':
    # инициализация графа с помощью словаря смежности
    a, b, c, d, e, f, g, h = range(8)
    N = [
        {b: 7, c: 9, f: 14},
        {a: 7, c: 10, d: 15},
        {a: 9, b: 10, d: 11, f: 2},
        {b: 15, c: 11, e: 6},
        {d: 6, f: 9},
        {a: 14, c: 2, e: 9},
        {h: 2},
        {g: 2},
    ]
    for i in range(1):
        print dijkstra_shortest_path(N, a)
# b in N[a] - смежность
# len(N[f]) - степень
# N[a][b] - вес (a,b)
# print N[a][b]
