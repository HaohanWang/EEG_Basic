import sys
import newFormat as f
import call as c
import operator

command = sys.argv[1]
user = ""
path = "finalData/"
names = ['Haohan', 'Jason','Martin','Peiyun','Varuni','Xiaobo', 'Yifei', 'Yucong', 'Zeyuan', 'Zhu']
#names = ['Haohan', 'Jason','Martin','Varuni','Xiaobo', 'Yucong', 'Zeyuan', 'Zhu']
video = f.getEasyVideo()
label = 'pre'
history = 20
def runwithfilter():
    filt = [line.strip() for line in open('filter.txt')]
    result = {}
    step = len(filt)*0.05
    count = 0
    ms = 1
    print "let's go"
    for line in filt:
        #print line
        count+=1
        if count>=ms*step:
            print 'Finished', ms*5, '%'
            ms+=1
        temp = 0.0
        if command == '1':
            s = 0.0
            r = 0.0
            for n in names:
                f.getIndependend(path, n, label, line)
                s+=100.0
                t=c.runCommand()
                t=c.evaluate(history)
                #print n, t/100
                r+=t
            #print r/s
            temp = r/s

        if command == '2':
            st = 0.0
            rt = 0.0
            for user in names:
                s = 0.0
                r = 0.0
                for i in range(0, 5):
                    for j in range(5, 10):
                        fl = [str(i)+'.txt', str(j)+'.txt']
                        f.getDependent(path, user, fl, label)
                        t=c.runCommand()
                        t=c.evaluate(history)
                        s+=100.0
                        st+=100.0
                        r+=t
                        rt+=t
                print user, r/s
            print 'average', rt/st

        if command == '3':
            for user in names:
                print "************"
                for i in range(0, 10):
                    fl = [str(i)+'.txt']
                    f.getDependent(path, user, fl, label)
                    t=c.runCommand()
                    con = t/100.0
                    if i <= 4:
                        con = 1-t/100.0
                    p = 1.0/7.0
                    score = round(con/p)+1
                    print user, 'session', i, score

        if command == '4':
            st = 0.0
            rt = 0.0
            for user in names:
                s = 0.0
                r = 0.0
                for i in range(0, 10):
                    fl = [str(i)+'.txt']
                    f.getDependent(path, user, fl, label, line)
                    t=c.runCommand()
                    t=c.evaluate(history)
                    s+=100.0
                    st+=100.0
                    r+=t
                    rt+=t
                #print user, r/s
            #print 'average', rt/st
            temp = rt/st
        result[line]=temp
    output = open('Result'+str(label)+str(command), 'w')
    rank = sorted(result.iteritems(), key=operator.itemgetter(1))
    rank.reverse()
    for line in rank:
        output.writelines(str(line[0])+'\t'+str(line[1])+'\n')

def singleRun():
    line = '11111111111'
    if command == '1':
        s = 0.0
        r = 0.0
        for n in names:
            f.getIndependend(path, n, label, line)
            s+=100.0
            t=c.runCommand()
            t=c.evaluate(history)
            print n, t/100
            r+=t
        print 'average', r/s

    if command == '2':
        st = 0.0
        rt = 0.0
        for user in names:
            s = 0.0
            r = 0.0
            for i in range(0, 5):
                for j in range(5, 10):
                    fl = [str(i)+'.txt', str(j)+'.txt']
                    f.getDependent(path, user, fl, label)
                    t=c.runCommand()
                    t=c.evaluate(history)
                    s+=100.0
                    st+=100.0
                    r+=t
                    rt+=t
            print user, r/s
        print 'average', rt/st

    if command == '3':
        for user in names:
            print "************"
            for i in range(0, 10):
                fl = [str(i)+'.txt']
                f.getDependent(path, user, fl, label)
                t=c.runCommand()
                con = t/100.0
                if i <= 4:
                    con = 1-t/100.0
                p = 1.0/7.0
                score = round(con/p)+1
                print user, 'session', i, score

    if command == '4':
        st = 0.0
        rt = 0.0
        for user in names:
            s = 0.0
            r = 0.0
            for i in range(0, 10):
                fl = [str(i)+'.txt']
                f.getDependent(path, user, fl, label, line)
                t=c.runCommand()
                t=c.evaluate(history)
                s+=100.0
                st+=100.0
                r+=t
                rt+=t
            print user, r/s
        print 'average', rt/st

singleRun()