import os

tr = []
te = []

def getTrain(f):
    text = [line.strip() for line in open(f)]
    for i in range(len(text)/4, 3*len(text)/4):
        item = text[i].split(',')
        ins = ""
        if item[-1]=='0':
            ins = '-1 '
        else:
            ins = '+1 '
        for j in range(3, len(item)-1):
            ins+=str(j-2)+':'+str(item[j])+' '
        tr.append(ins)
def getTest(f):
    text = [line.strip() for line in open(f)]
    for i in range(len(text)/4, 3*len(text)/4):
        item = text[i].split(',')
        ins = ""
        if item[-1]=='0':
            ins = '-1 '
        else:
            ins = '+1 '
        for j in range(3, len(item)-1):
            ins+=str(j-2)+':'+str(item[j])+' '
        te.append(ins)

def findpassage(path):
    f = []
    for (d, p, fl) in os.walk(path):
        f.extend(fl)
        break
    return f
def findFolder(path):
    f = []
    for (d, p, fl) in os.walk(path):
        f.extend(p)
        break
    return f


def getIndependend(path, user):
    global tr, te
    tr = []
    te = []
    folder = findFolder(path)
    for f in folder:
        if f != user:
            titles = findpassage(path+f+'/')
            for t in titles:
                getTrain(path+f+'/'+t)
        else:
            titles = findpassage(path+f+'/')
            for t in titles:
                getTest(path+f+'/'+t)
    output()

def getDependent(path, user, fl):
    global tr, te
    tr = []
    te = []
    for t in findpassage(path+user+'/'):
        if t in fl:
            getTest(path+user+'/'+t)
        else:
            getTrain(path+user+'/'+t)
    output()

def output():
    train = open('file/train.txt', 'w')
    test = open('file/test.txt', 'w')
    for line in tr:
        train.writelines(line+'\n')
    for line in te:
        test.writelines(line+'\n')
