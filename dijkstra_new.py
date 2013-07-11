#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Алгоритм Дейкстры
#   Находит кратчайшее расстояние от одной из вершин графа до всех остальных. 
#   Алгоритм работает только для графов без рёбер отрицательного веса.
# Описание алгоритма http://goo.gl/KsqC
# Более красивый алгоритм
# http://gliffer.ru/articles/algoritmi--opisanie-algoritmov-%E2%80%94-vmesto-psevdokoda-luchshe-python/
# 
def Dijkstra(graph, v0):
    distance = dict(((v, float('inf')) for v in graph.iterkeys()))
    distance[v0] = 0
    vertex = set(graph.iterkeys())
    while vertex:
        d1, v1 = min(((distance[v], v) for v in vertex))
        vertex.remove(v1)
        for v, d in graph[v1].iteritems():
            if distance[v] > distance[v1] + d:
                distance[v] = distance[v1] + d
                print v1, distance
    return distance

if __name__ == '__main__':
    # инициализация графа с помощью словаря смежности
    # 
    G = {
        'a': {'b': 7, 'c': 9, 'f': 14},
        'b': {'a': 7, 'c': 10, 'd': 15},
        'c': {'a': 9, 'b': 10, 'd': 11, 'f': 2},
        'd': {'b': 15, 'c': 11, 'e': 6},
        'e': {'d': 6, 'f': 9},
        'f': {'a': 14, 'c': 2, 'e': 9}
    }
    print Dijkstra(G, 'a')
    # print convert_adjacency_matrix(G)

    # for i in range(1):
        # print dijkstra_shortest_path(N, a)
# b in N[a] - смежность
# len(N[f]) - степень
# N[a][b] - вес (a,b)
# print N[a][b]
