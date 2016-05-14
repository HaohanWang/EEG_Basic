import os

tr = []
te = []

def getTrain(f, att, filt):
    text = [line.strip() for line in open(f)]
    for i in range(len(text)/4, 3*len(text)/4):
        item = text[i].split(',')
        ins = ""
        if att=='pre':
            if item[-5]=='0':
                ins = '-1 '
            else:
                ins = '+1 '
        elif att =='own':
            if float(item[-4])<=3:
                ins = '-1 '
            else:
                ins = '+1 '
        else:
            print 'WARNING, NO ATTRIBUTE SELECTED'
        attri = getAttribute(filt)
        order = 1
        for j in range(3, len(item)-5):
            if j in attri:
                ins+=str(order)+':'+str(item[j])+' '
                order+=1
        tr.append(ins)
def getTest(f, att, filt):
    text = [line.strip() for line in open(f)]
    for i in range(len(text)/4, 3*len(text)/4):
        item = text[i].split(',')
        ins = ""
        if att=='pre':
            if item[-5]=='0':
                ins = '-1 '
            else:
                ins = '+1 '
        elif att =='own':
            if float(item[-4])<=3:
                ins = '-1 '
            else:
                ins = '+1 '
        else:
            print 'WARNING, NO ATTRIBUTE SELECTED'
        attri = getAttribute(filt)
        order = 1
        for j in range(3, len(item)-5):
            if j in attri:
                ins+=str(order)+':'+str(item[j])+' '
                order+=1
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


def getIndependend(path, user, att, line):
    global tr, te
    tr = []
    te = []
    folder = findFolder(path)
    for f in folder:
        if f != user:
            titles = findpassage(path+f+'/')
            for t in titles:
                getTrain(path+f+'/'+t, att, line)
        else:
            titles = findpassage(path+f+'/')
            for t in titles:
                getTest(path+f+'/'+t, att, line)
    output()

def getDependent(path, user, fl, att, line):
    global tr, te
    tr = []
    te = []
    for t in findpassage(path+user+'/'):
        if t in fl:
            getTest(path+user+'/'+t, att, line)
        else:
            getTrain(path+user+'/'+t, att, line)
    output()

def output():
    train = open('file/train.txt', 'w')
    test = open('file/test.txt', 'w')
    for line in tr:
        train.writelines(line+'\n')
    for line in te:
        test.writelines(line+'\n')
def getEasyVideo():
    easy = {}
    data = [line.strip() for line in open('reTag/easyVideo')]
    for line in data:
        item = line.split()
        easy[item[0]]=[]
        for i in range(1, len(item)):
            easy[item[0]].append(int(item[i]))
    return easy
def getAttribute(filt):
    att = []
    for i in range(len(filt)):
        if filt[i]=='1':
            att.append(i+3)
    return att