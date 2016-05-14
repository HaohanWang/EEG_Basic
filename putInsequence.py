import os

def getSeq():
    seq = [line.strip() for line in open('reTag/seq')]
    s = []
    a = []
    for i in range(len(seq)):
        if i%10==0:
            if len(a)>0:
                s.append(a)
            a = []
        a.append(seq[i])
    c = []
    d = []
    for user in s:
        for f in user:
            if f[0] == 'e':
                label = int(f[-1])-1
            else:
                label = int(f[-1])+4
            d.append(str(label))
        c.append(d)
        d=[]
    return c

def findpassage(path):
    f = []
    for (d, p, fl) in os.walk(path):
        f.extend(fl)
        break
    return f

def copyFile(i, j, path, fi):
    names = ['Haohan', 'Xiaobo', 'Zhu', 'Jason','Martin','Peiyun','Varuni','Yifei', 'Yucong', 'Zeyuan']
    outfolder = 'seqData/'
    seq = getSeq()
    f = open(outfolder+names[i]+'/'+seq[i][j]+'.txt', 'w')



def putInSequence():
    names = ['Haohan', 'Xiaobo', 'Zhu', 'Jason','Martin','Peiyun','Varuni','Yifei', 'Yucong', 'Zeyuan']
    infolder = 'finalData/'
    for i in range(len(names)):
        path = infolder+names[i]+'/'
        f = findpassage(path)
        fi = sorted(f)
        for j in range(len(fi)):
            copyFile(i, j, path, fi)




putInSequence()