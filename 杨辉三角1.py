def yanghui(line,type):
    yang=[[1]]
    for h in range(1,line):
        hang=[1]
        for c in range(1,h):
            hang.append(yang[h-1][c]+yang[h-1][c-1])
        hang.append(1)
        yang.append(hang)
    space=line-1
    for h in yang:
        print(' '*space*type,end=' ')
        for c in h:
            print(c,end=' ')
        print()
        space-=1

yanghui(5,1)