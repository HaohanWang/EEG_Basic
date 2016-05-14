score = [line.strip() for line in open('reTag/rawScore')]

def map(t):
    if len(t)==0:
        return []
    upp= max(t)
    low = min(t)
    diff = low - 1
    scale = 7.0/(upp-diff)
    n = []
    for i in t:
        n.append(scale*(i-diff))
    return n

def run(score):
    s = []
    t = []
    f = open('reTag/score', 'w')
    for i in range(len(score)):
        if i%10==0:
            for j in map(t):
                s.append(j)
            t = []
        t.append(int(score[i]))
    for j in map(t):
        s.append(j)
    for i in s:
        f.writelines(str(i)+'\n')

def statistics(score):
    s = 0.0
    n = {}
    for i in score:
        if i not in n:
            n[i]=1.0
        else:
            n[i]+=1.0
        s +=1.0
    for i in range(1, 8):
        print i, n[str(i)]/s

statistics(score)