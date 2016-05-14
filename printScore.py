seq = [line.strip() for line in open('reTag/seq')]
score = [line.strip() for line in open('reTag/rawScore')]

names = ['Haohan', 'Xiaobo', 'Zhu', 'Jason','Martin','Peiyun','Varuni', 'Yifei', 'Yucong', 'Zeyuan']

result = {}

def printScore():
    for i in range(len(seq)):
        name = names[i/10]
        if name not in result:
            result[name] = {}
            for j in range(1,11):
                str1 = 'easy'+str(j)
                str2 = 'con'+str(j)
                result[name][str1]=0
                result[name][str2]=0
        result[name][seq[i]] = int(score[i])

    for name in names:
        for i in range(1, 11):
            str1 = 'easy'+str(i)
            print name, str1, result[name][str1]
        for i in range(1, 11):
            str2 = 'con'+str(i)
            print name, str2, result[name][str2]

def getClassify():
    for i in range(len(seq)):
        name = names[i/10]
        if name not in result:
            result[name]=[]
        if seq[i].startswith('easy'):
            result[name].append(i%10)
    for name in names:
        print name,
        for i in result[name]:
            print i,
        print ''

getClassify()