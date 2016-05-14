import operator
# for i in range(1, pow(2, 11)):
#     s = '00000000000'+bin(i)[2:]
#     print s[-11:]

def getAttribute():
    so = open('other/specific.txt', 'w')
    do = open('other/dependent.txt', 'w')
    data = [line.strip() for line in open('other/rrrr.txt')]
    s = {}
    d = {}
    for line in data:
        item = line.split()
        seq = ('00000000000'+bin(int(item[0]))[2:])[-11:]
        s[seq] = item[1]
        d[seq] = item[2]
    ss = sorted(s.iteritems(), key=operator.itemgetter(1))
    sd = sorted(d.iteritems(), key=operator.itemgetter(1))
    ss.reverse()
    sd.reverse()
    for line in ss:
        so.writelines(str(line[0])+'\t'+str(line[1])+'\n')
    for line in sd:
        do.writelines(str(line[0])+'\t'+str(line[1])+'\n')

getAttribute()
