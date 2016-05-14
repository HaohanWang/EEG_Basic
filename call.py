import commands
import re

match=re.compile("Accuracy = (.*)%", re.DOTALL)

c1 = "lib/./svm-train -s 2 -t 0 file/train.txt model/model.model"
c2 = "lib/./svm-predict file/test.txt model/model.model file/output"

def runCommand():
    r1 = commands.getstatusoutput(c1)[1]
    r2 = commands.getstatusoutput(c2)[1]
    r = float(match.findall(r2)[0])
    return r

def evaluate(history):
    voteResult(history)
    output = [line.strip() for line in open('file/vote')]
    test = [line.strip().split(' ')[0] for line in open('file/test.txt')]
    correct = 0.0
    count = 0.0
    for i in range(len(output)):
        count+=1.0
        #print test[i], output[i]
        if int(test[i])==int(output[i]):
            correct+=1.0
    return correct*100/count

def voteResult(history):
    output = [line.strip() for line in open('file/output')]
    result = []
    f = open('file/vote', 'w')
    for i in range(len(output)):
        if i <=history:
            result.append(int(output[i]))
        else:
            sum = 0
            for j in range(i-history, i+1):
                sum += int(result[j-1])
            if sum>=0:
                result.append(1)
            else:
                result.append(-1)
    for line in result:
        f.writelines(str(line)+'\n')
    f.close()
