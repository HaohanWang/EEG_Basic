import format

names = ['Haohan', 'Xiaobo', 'Zhu', 'Jason','Martin','Peiyun','Varuni', 'Yifei', 'Yucong', 'Zeyuan']

inFolder = 'finalData/'
easy = 'easyData/'
con = 'conData/'

def checkEasy(name, t):
    data = [line.strip() for line in open(inFolder+name+'/'+t)]
    item = data[0].split(',')
    if item[14] == '0':
        return True
    else:
        return False

def putInto(cls, name, t):
    data = [line.strip() for line in open(inFolder+name+'/'+t)]
    f = open(cls+name+'/'+t, 'w')
    for line in data:
        f.writelines(line+'\n')
    f.close()

def findEasyAndCon():
    for name in names:
        path = inFolder+name+'/'
        l = format.findpassage(path)
        for t in l:
            if checkEasy(name,t):
                putInto(easy, name, t)
            else:
                putInto(con, name, t)

findEasyAndCon()
