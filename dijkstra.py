#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Алгоритм Дейкстры
#   Находит кратчайшее расстояние от одной из вершин графа до всех остальных. 
#   Алгоритм работает только для графов без рёбер отрицательного веса.
#   Матрица задается как список словарей смежности вершин
# Описание алгоритма http://goo.gl/KsqC


def dijkstra_shortest_path(graph, start_v):

    p = {} # наименьшие пути обхода
    u = [] # обработанные вершины
    p[start_v] = 0 # инициализация начального пути
    
    while len(u) <= len(graph) and start_v != None:
        # поиск минимальных путей ко всем ближайшим вершинам
        for x in graph[start_v]:
            if (x not in u and x != start_v):
                if (x not in p.keys() or (graph[start_v][x] + p[start_v]) < p[x]):
                    p[x] = graph[start_v][x] + p[start_v]
        
        u.append(start_v)
        
        # поиск следующей вершины с минимальным путем
        min_v = None
        for x in p:
            if ( (min_v is not None and p[x] < p[min_v]) or min_v == None) and x not in u:
                    min_v = x
        start_v = min_v
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
