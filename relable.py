import format

# for title in format.findpassage(npath):
#     i = int(title[0])
#     if i>=1 and i <=5:
#         label = 0
#     else:
#         label = 1
#     text = [line.strip() for line in open(npath+title)]
#     f = open(nnpath+str(i)+'.txt', 'w')
#     for line in text:
#         first = line[:-7]
#         second = line[-7:]
#         f.writelines(first+str(label)+','+second+'\n')

def qualify(title, sym):
    tag = int(title[0])
    if tag<=4 and sym=='e':
        return True
    elif tag>=5 and sym=='c':
        return True
    return False

def addLine(title, name, line):
    f = open('finalData/'+name+'/'+title, 'w')
    text = [l.strip() for l in open(input_folder+name+'/'+title)]
    # if text[0][-1]=='0':
    #     print 2
    # else:
    #     print 6
    for l in text:
        l = l+line
        f.writelines(l+'\n')


input_folder = 'OriginData/'
#names = ['Haohan', 'Xiaobo', 'Zhu', 'Jason','Martin','Peiyun','Varuni', 'Yifei', 'Yucong', 'Zeyuan']

names = ['Yucong', 'Yifei']

seq = [line.strip() for line in open('reTag/sequenceY')]
score = [line.strip() for line in open('reTag/rawScoreY')]
SA = [line.strip() for line in open('reTag/SAY')]
SB = [line.strip() for line in open('reTag/SBY')]
SC = [line.strip() for line in open('reTag/SCY')]

for i in range(len(score)):
    score[i] = ','+score[i]+','+SA[i]+','+SB[i]+','+SC[i]

def run():
    fin = []

    for i in range(len(seq)):
        if i%10==0:
            fin = []
        line = score[i]
        name = names[i/10]
        path = input_folder+name+'/'
        titles = format.findpassage(path)
        lists = sorted(titles)
        for title in lists:
            if title not in fin:
                addLine(title, name, line)
                fin.append(title)
                break

run()