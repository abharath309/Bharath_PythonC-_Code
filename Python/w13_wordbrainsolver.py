# AUTHOR Bharath Ananth abharath@bu.edu
import collections
import sys
import numpy as np
from collections import Counter
from collections import defaultdict as cdict
import copy
from ast import literal_eval as litev


def validWord(word, letterList):
    word2, word1 = Counter(word), Counter(letterList)
    return all(word2[k] <= word1.get(k, 0) for k in word2)
str2 = open(sys.argv[1], 'r')
sortwords = cdict(list)
a = cdict(list)
for line in sorted(str2):
    if(line != '\n'):
        lenw = str(len(line[:-1]))
        sortwords[line[0]+lenw].append(line[:-1])
str2 = open(sys.argv[2], 'r')
sortwords2 = cdict(list)
a = cdict(list)
for line in sorted(str2):
    if(line != '\n'):
        lenw = str(len(line[:-1]))
        sortwords2[line[0] + lenw].append(line[:-1])


def gravity(matrix):
    matrix2 = []
    m = np.transpose(matrix)
    for row in m:
        d = sorted(row, key=lambda x: x != '0', reverse=False)
        matrix2.append(d)
    matrix2 = np.transpose(matrix2)
    return matrix2


def newGrid(indeces, matrix2):
    m = copy.copy(matrix2)
    for i in indeces:
        m[i[0]][i[1]] = '0'
    return gravity(m)


def nbr(x, y, Y, X):
    se1 = [(x2, y2) for x2 in range(x-1, x+2)
           for y2 in range(y-1, y+2)
           if (-1 < x < X and -1 < y < Y and
               (x != x2 or y != y2) and
               (0 <= x2 < X) and (0 <= y2 < Y))]
    return se1
for line in sys.stdin:
    if(line != '\n'):
        if(line[0] == '{'):
            grid = litev(line)["grid"]
            grid1 = []
            for lin in grid:
                grid1.append(list(lin))
            grid = np.transpose(grid1)
            lengths = litev(line)["lengths"]
            size = litev(line)["size"]
        wordlist = cdict(list)
        dict4 = {'0': grid}
        for l in lengths:
            dict3 = cdict(list)
            for ngrid in dict4.keys():
                for x in range(len(dict4[ngrid])):
                    for y in range(len(dict4[ngrid][x])):
                        X = len(dict4[ngrid])
                        Y = len(dict4[ngrid][x])
                        if dict4[ngrid][x][y] != '0':
                            for k in sortwords[dict4[ngrid][x][y] + str(l)]:
                                if validWord(k, dict4[ngrid].flatten()):
                                    dict1 = cdict(list)
                                    dict1.update({str([dict4[ngrid][x][y],
                                                       [(x, y)]]):
                                                           nbr(x, y, X, Y)})
                                    i = 1
                                    for i in range(1, l):
                                        dict2 = cdict(list)
                                        for key in dict1.keys():
                                            for pos in dict1[key]:
                                                if (k[i] == dict4[ngrid]
                                                    [pos[0]][pos[1]] and
                                                    (pos
                                                    not in
                                                        litev(key)[1])):
                                                    dict2.update
                                                    ({str([litev(key)[0] +
                                                      dict4[ngrid][pos[0]]
                                                      [pos[1]],
                                                      litev(key)[1] +
                                                      [(pos[0], pos[1])]]):
                                                        nbr(pos[0], pos[1],
                                                            X, Y)})
                                        dict1 = dict2
                                    for dkey in dict2.keys():
                                        dict3.update({ngrid + " " +
                                                      litev(dkey)[0] + " " +
                                                      str(litev(dkey)[1]):
                                                      newGrid(litev(dkey)[1],
                                                              dict4[ngrid])})
            dict4 = dict3
        if(dict4 == {}):
            dict4 = {'0': grid}
            for l in lengths:
                dict3 = cdict(list)
                for ngrid in dict4.keys():
                    for x in range(len(dict4[ngrid])):
                        for y in range(len(dict4[ngrid][x])):
                            X = len(dict4[ngrid])
                            Y = len(dict4[ngrid][x])
                            if dict4[ngrid][x][y] != '0':
                                for k in sortwords2[dict4[ngrid][x][y]+str(l)]:
                                    if validWord(k, dict4[ngrid].flatten()):
                                        dict1 = cdict(list)
                                        dict1.update({str([dict4[ngrid][x][y],
                                                          [(x, y)]]):
                                                     nbr(x, y, X, Y)})
                                        i = 1
                                        for i in range(1, l):
                                            dict2 = cdict(list)
                                            for key in dict1.keys():
                                                for pos in dict1[key]:
                                                    if (k[i] == dict4[ngrid]
                                                       [pos[0]][pos[1]] and
                                                       (pos not in
                                                       litev(key)[1])):
                                                        dict2.update(
                                                         {str([litev(key)[0] +
                                                          dict4[ngrid]
                                                               [pos[0]]
                                                               [pos[1]],
                                                          litev(key)[1] +
                                                               [(pos[0],
                                                                 pos[1])]]):
                                                          nbr(pos[0],
                                                              pos[1], X, Y)})
                                            dict1 = dict2
                                        for dkey in dict2.keys():
                                            dict3.update({ngrid + " " +
                                                         litev(dkey)[0] + " " +
                                                         str(litev(dkey)[1]):
                                                          newGrid(
                                                               litev(dkey)[1],
                                                               dict4[ngrid])})
                dict4 = dict3
        str4 = []
        for key in dict4.keys():
            str3 = []
            flag = 1
            for pos in key:
                try:
                    if((pos != '(') & (pos != ')') & (pos != '[') &
                       (pos != ']') & (pos != ',') & (pos != ' ') &
                       (pos != '0')):
                        s = int(pos)
                        flag = 0
                    if((pos == '(') & (pos == ')') &
                        (pos == '[') & (pos == ']') & (pos == ',') &
                       (pos == ' ')):
                        flag = 0
                except:
                    if(flag == 0):
                        str3.append(" ")
                    str3.append(pos)
                    flag = 1
            if(''.join(str3) not in str4):
                str4.append(''.join(str3))
        sys.stdout
        print(*sorted(str4), sep='\n')
        print('.')
