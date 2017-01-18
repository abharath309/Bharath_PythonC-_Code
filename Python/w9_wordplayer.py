import collections
import sys


def main():
    word_search()


def word_search():
    str2 = open(sys.argv[1], 'r')
    sortwords = collections.defaultdict(list)
    for line in sorted(str2):
        print ("line is",line)
        sortw = ''.join(sorted(line[:-1]))
        print ("sortw is",sortw)
        lenw = str(len(line[:-1]))
        print ("length",lenw)
        sortwords[sortw].append(line[:-1])
        sortwords[lenw].append(line[:-1])
    while(1):
        inp = list(input())
        if inp[len(inp)-1] == '0':
            if inp[len(inp)-2] == ' ':
                break
        l = int(inp.pop(len(inp)-1))
        print (l)
        while(inp[len(inp)-1] != ' '):
            l = l + 10*int(inp.pop(len(inp)-1))
        if (len(inp[:-1]) == l) & (''.join(sorted(inp[:-1])) in sortwords):
            print(*sortwords[''.join(sorted(inp[:-1]))], sep='\n'),
        else:
            for key in sortwords[str(l)]:
                print ("Key is",key)
                string1 = sorted(inp[:-1])
                print ("String 1 is", string1)
                word = list(key)
                print (word)
                for i in range(len(word)):
                    if word[i] in string1:
                        string1.remove(word[i])
                        flag = 1
                    else:
                        flag = 0
                        break
                if flag == 1:
                        print(key)
        if (int(l) != 0):
            print("."),


main()
