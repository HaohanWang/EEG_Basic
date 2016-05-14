import format

names = ['Haohan', 'Xiaobo', 'Zhu', 'Jason','Martin','Peiyun','Varuni', 'Yucong', 'Yifei', 'Zeyuan']
folder1 = 'finalData/'
folder2 = 'NewNewData/'

def checkFile(name, l1, l2):
    data1 = [line.strip() for line in open(folder1+name+'/'+l1)]
    data2 = [line.strip() for line in open(folder2+name+'/'+l2)]
    for i in range(len(data1)):
        if data1[i][:-8]!=data2[i][:-8]:
            return False
    print l1, l2
    return True

def checkList(name,list1, list2):
    count = 0
    for l1 in list1:
        for l2 in list2:
            if checkFile(name,l1, l2):
                count+=1
    if count==10:
        return True


def check():
    count = 0
    for name in names:
        path1 = folder1+name+'/'
        path2 = folder2+name+'/'
        list1 = format.findpassage(path1)
        list2 = format.findpassage(path2)
        if checkList(name, list1, list2):
            print name, True
            count+=1
        else:
            print name, False
    if count==10:
        print 'INTACT'

check()