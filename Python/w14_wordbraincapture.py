# AUTHOR AkashMehta amehta22@bu.edu
# AUTHOR Bharath Ananth abharath@bu.edu
# AUTHOR MuhammadZuhayrRaghib mzraghib@bu.edu
import numpy as np
import json
import skimage.io
import skimage.transform
from os import listdir
import re
import numpy as np
import hashlib
import PIL
import scipy.spatial
from PIL import Image, ImageFilter
import collections
import sys

dictEnergy = {'3': {'a': [6801.0], 'w': [9593.0], 'p': [6679.0], 'd': [8600.0],
                    'u': [7371.0], 'q': [9837.0], 'm': [9670.0], 'l': [4481.0],
                    'y': [5103.0],
                    't': [4793.0], 'j': [4060.0], 'b': [8543.0], 'g': [8117.0],
                    'n': [8481.0],
                    'e': [7146.0], 'o': [8768.0], 's': [6349.0], 'c': [6684.0],
                    'f': [5792.0],
                    'k': [7459.0], 'r': [8338.0], 'x': [7172.0], 'i': [3310.0],
                    'h': [8040.0], 'v': [6003.0]},
              '4': {'a': [3838.0], 'w': [5403.0], 'p': [3773.0], 'd': [4847.0],
                    'u': [4143.0], 'm': [5437.0], 'l': [2519.0], 'y': [2886.0],
                    't': [2683.0],
                    'j': [2288.0], 'b': [4816.0], 'g': [4567.0], 'n': [4774.0],
                    'e': [4029.0],
                    'o': [4933.0], 's': [3561.0], 'c': [3764.0], 'f': [3260.0],
                    'k': [4195.0],
                    'r': [4692.0], 'x': [4030.0], 'i': [1852.0], 'h': [4491.0],
                    'z': [3474.0], 'v': [3372.0]},
              '5': {'a': [2442.0], 'w': [3457.0], 'p': [2415.0], 'd': [3091.0],
                    'u': [2666.0], 'm': [3483.0], 'l': [1621.0], 'y': [1829.0],
                    't': [1722.0],
                    'j': [1457.0], 'b': [3060.0], 'g': [2919.0], 'n': [3055.0],
                    'e': [2593.0],
                    'o': [3152.0], 's': [2281.0], 'c': [2406.0], 'f': [2080.0],
                    'k': [2676.0],
                    'r': [3003.0], 'i': [1187.0], 'h': [2884.0], 'v': [2162.0],
                    'x': [2569.0]}}

positionsX = {'3': [[601, 388], [1063, 388], [1526, 388], [601, 850],
              [1063, 850],
              [1526, 850], [601, 1313], [1063, 1313], [1526, 1313]],
              '4': [[586, 373], [934, 373], [1280, 373], [1627, 373],
                    [586, 720], [934, 720], [1280, 720], [1627, 720],
                    [586, 1067], [934, 1067], [1280, 1067], [1627, 1067],
                    [586, 1414], [934, 1414], [1280, 1414], [1627, 1414]],
              '5': [[579, 365], [856, 365], [1133, 365], [1410, 365],
                    [1687, 365], [579, 642], [856, 642], [1133, 642],
                    [1410, 642], [1687, 642], [579, 919], [856, 919],
                    [1133, 919], [1410, 919], [1687, 919],
                    [579, 1196], [856, 1196], [1133, 1196], [1410, 1196],
                    [1687, 1196],
                    [579, 1473], [856, 1473], [1133, 1473], [1410, 1473],
                    [1687, 1473]]}
positionsY = {'3': [[949, 735], [1411, 735], [1874, 735], [949, 1197],
                    [1411, 1197], [1874, 1197], [949, 1660], [1411, 1660],
                    [1874, 1660]],
              '4': [[846, 633], [1194, 633], [1540, 633], [1887, 633],
                    [846, 980],
                    [1194, 980],
                    [1540, 980], [1887, 980], [846, 1327], [1194, 1327],
                    [1540, 1327],
                    [1887, 1327], [846, 1674], [1194, 1674], [1540, 1674],
                    [1887, 1674]],
              '5': [[786, 572], [1063, 572], [1340, 572], [1617, 572],
                    [1894, 572],
                    [786, 849], [1063, 849], [1340, 849], [1617, 849],
                    [1894, 849],
                    [786, 1126], [1063, 1126], [1340, 1126], [1617, 1126],
                    [1894, 1126],
                    [786, 1403], [1063, 1403], [1340, 1403], [1617, 1403],
                    [1894, 1403],
                    [786, 1680], [1063, 1680], [1340, 1680], [1617, 1680],
                    [1894, 1680]]}
dictCheck = {'3': {'e': [(167, 205, 0)], 'x': [(133, 193, 0)],
                   'c': [(236, 188, 0)],
                   'p': [(178, 197, 0)], 'd': [(168, 228, 0)],
                   'b': [(169, 177, 0)]},
             '4': {'e': [(80, 134, 0)], 'x': [(106, 137, 0)],
                   'a': [(154, 144, 0)],
                   'c': [(176, 136, 0)], 'p': [(106, 167, 0)],
                   'w': [(170, 163, 0)],
                   'm': [(97, 163, 0)], 'u': [(115, 163, 0)],
                   'k': [(126, 120, 0)],
                   'h': [(110, 170, 0)], 'g': [(80, 135, 0)],
                   'n': [(80, 173, 0)],
                   'b': [(126, 166, 0.752621568627451)],
                   'd': [(130, 117, 0.752621568627451)], 'r': [(182, 159, 0)]},
             '5': {'m': [(60, 135, 0)],
                   'w': [(140, 128, 0)],
                   'k': [(100, 100, 0)],
                   'u': [(100, 135, 0)],
                   'a': [(145, 143, 0)],
                   'c': [(145, 110, 0)],
                   'p': [(60, 80, 0)],
                   'e': [(100, 117, 0)],
                   'x': [(84, 111, 0)],
                   'o': [(102, 58, 0), (143, 69, 0.752621568627451),
                         (104, 62, 0)],
                   'n': [(90, 100, 0), (144, 66, 0),
                         (58, 80, 0.752621568627451),
                         (99, 121, 0.752621568627451),
                         (104, 87, 0.752621568627451)],
                   'g': [(131, 95, 0), (91, 142, 0.752621568627451)],
                   'h': [(99, 121, 0), (62, 106, 0.752621568627451),
                         (116, 123, 0.752621568627451),
                         (135, 102, 0.752621568627451)],
                   'b': [(70, 113, 0), (84, 118, 0), (139, 115, 0),
                         (102, 135, 0.752621568627451),
                         (84, 69, 0.752621568627451),
                         (99, 140, 0.752621568627451)],
                   'd': [(109, 120, 0.752621568627451),
                         (104, 62, 0.752621568627451),
                         (99, 140, 0), (63, 110, 0), (142, 100, 0),
                         (98, 99, 0.752621568627451)],
                   'r': [(107, 114, 0), (142, 128, 0),
                         (62, 140, 0.752621568627451),
                         (89, 96, 0.752621568627451),
                         (141, 102, 0.752621568627451)]
                   }}

dictThresh = {'3': 60,
              '4': 68,
              '5': 65}
dictLocations = {}


def checkSize(a):
    x = 0
    box = collections.OrderedDict()
    j = a[610].flatten()
    for index in j:
        index = round(index, 3)
        if index != 0.113:
            if x in box.keys():
                box[x].append(index)
            else:
                box.update({x: [index]})
        if index == 0.113:
            x += 1
    s = len(box)
    return s


def checkWords(a, size, loc):
    box = 0
    nos = []
    j = a[loc].flatten()
    p = 0
    line = 0
    while(p < len(j)):
        index = round(j[p], 3)
        space = 0
        while (index == 0.113) & (p < len(j)):
            index = round(j[p], 3)
            p += 1
            space += 1
        while (index != 0.113) & (p < len(j)):
            index = round(j[p], 3)
            p += 1
        line += 1
        if(np.mod(line, 2) == 0):
            box += 1
        if((line > 1) & (space > 150) & (size == 3)):
            nos.append(box)
            box = 0
        if((line > 1) & (space > 125) & (size == 5)):
            nos.append(box)
            box = 0
        if((line > 1) & (space > 137) & (size == 4)):
            nos.append(box)
            box = 0
    if(box != 0):
            nos.append(box)
            box = 0
    return nos


fList = collections.OrderedDict()

r = re.compile('(\d+)')

for file in sys.stdin:
    if file[len(file)-1] == '\n':
        file = file[:len(file)-1]
    if file != 'cat':
        i = r.split(file)
        fList.update({int(i[1]): file})

for num in fList.keys():
    a = skimage.io.imread(fList[num], as_grey=False)
    output = collections.defaultdict(list)
    row = ""
    w = skimage.color.rgb2grey(a)
    size = checkSize(w)
    if(size == 3):
        words = checkWords(w, size, 2140)
    if(size == 5) & (round(sum(w[2376]), 0) != 232.0):
        words = checkWords(w, size, 2029)
        words1 = checkWords(w, size, 2158)
        words2 = checkWords(w, size, 2327)
        words += (words1 + words2)

    if(size == 5) & (round(sum(w[2376]), 0) == 232.0):
        words = checkWords(w, size, 2070)
        words1 = checkWords(w, size, 2200)
        words += (words1)

    if(size == 4):
        words = checkWords(w, size, 2138)
        words1 = checkWords(w, size, 2300)
        words += words1
    l = 0
    for pos in range(len(positionsX[str(size)])):
        b = a[positionsX[str(size)][pos][0]:positionsY[str(size)][pos][0],
              positionsX[str(size)][pos][1]:
              positionsY[str(size)][pos][1]]
        b = np.invert(b)
        b = skimage.color.rgb2grey(b)
        b = b-0.022509803921568629
        energy = sum(sum(b))
        energy = round(energy, 0)
        for key in dictEnergy[str(size)]:
            if (np.absolute(energy - dictEnergy[str(size)][key]) <
               dictThresh[str(size)]):
                if key in dictCheck[str(size)]:
                    for val in dictCheck[str(size)]:
                        if val == key:
                            flag = 0
                            for place in range(len(dictCheck[str(size)][val])):
                                if (b[dictCheck[str(size)][val][place][0]]
                                     [dictCheck[str(size)][val][place][1]] ==
                                   dictCheck[str(size)][val][place][2]):
                                    flag = 1
                                    break
                            if flag == 0:
                                row += key
                                l += 1
                else:
                    row += key
                    l += 1
        if l == size:
            output['grid'].append(row)
            row = ""
            l = 0
    output['size'] = size
    output['lengths'] = words
    print(dict(output))
