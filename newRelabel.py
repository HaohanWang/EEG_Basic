
folder = 'finalData'
def inverse(name, d):
    data = [line.strip() for line in open('finalData/'+name+'/'+d)]
    f = open('finalData/'+name+'/r'+d, 'w')
    for line in data:
        item = line.split(',')
        if item[14] == '1':
            item[14] = '0'
        else:
            item[14] = '1'
        nline = ','.join(item)
        f.writelines(nline+'\n')
    f.close()

name = 'Yifei'
dd = ['4.txt', '3.txt', '7.txt', '9.txt']
for d in dd:
    inverse(name, d)